import json
import re
import requests
import kfp
import os
import kubernetes as k8s

from urllib.parse import urlsplit
from kfp.onprem import use_k8s_secret
from kfp import components
from kfp.components import load_component_from_file
from kfp import dsl
from kfp import compiler


def get_istio_auth_session(url: str, username: str, password: str) -> dict:
    """
    Determine if the specified URL is secured by Dex and try to obtain a session cookie.
    WARNING: only Dex `staticPasswords` and `LDAP` authentication are currently supported
             (we default default to using `staticPasswords` if both are enabled)

    :param url: Kubeflow server URL, including protocol
    :param username: Dex `staticPasswords` or `LDAP` username
    :param password: Dex `staticPasswords` or `LDAP` password
    :return: auth session information
    """
    # define the default return object
    auth_session = {
        "endpoint_url": url,  # KF endpoint URL
        "redirect_url": None,  # KF redirect URL, if applicable
        "dex_login_url": None,  # Dex login URL (for POST of credentials)
        "is_secured": None,  # True if KF endpoint is secured
        # Resulting session cookies in the form "key1=value1; key2=value2"
        "session_cookie": None,
    }

    # use a persistent session (for cookies)
    with requests.Session() as s:
        ################
        # Determine if Endpoint is Secured
        ################
        resp = s.get(url, allow_redirects=True)
        if resp.status_code != 200:
            raise RuntimeError(
                f"HTTP status code '{resp.status_code}' for GET against: {url}"
            )

        auth_session["redirect_url"] = resp.url

        # if we were NOT redirected, then the endpoint is UNSECURED
        if len(resp.history) == 0:
            auth_session["is_secured"] = False
            return auth_session
        else:
            auth_session["is_secured"] = True

        ################
        # Get Dex Login URL
        ################
        redirect_url_obj = urlsplit(auth_session["redirect_url"])

        # if we are at `/auth?=xxxx` path, we need to select an auth type
        if re.search(r"/auth$", redirect_url_obj.path):
            #######
            # TIP: choose the default auth type by including ONE of the following
            #######

            # OPTION 1: set "staticPasswords" as default auth type
            redirect_url_obj = redirect_url_obj._replace(
                path=re.sub(r"/auth$", "/auth/local", redirect_url_obj.path)
            )
            # OPTION 2: set "ldap" as default auth type
            # redirect_url_obj = redirect_url_obj._replace(
            #     path=re.sub(r"/auth$", "/auth/ldap", redirect_url_obj.path)
            # )

        # if we are at `/auth/xxxx/login` path, then no further action is needed (we can use it for login POST)
        if re.search(r"/auth/.*/login$", redirect_url_obj.path):
            auth_session["dex_login_url"] = redirect_url_obj.geturl()

        # else, we need to be redirected to the actual login page
        else:
            # this GET should redirect us to the `/auth/xxxx/login` path
            resp = s.get(redirect_url_obj.geturl(), allow_redirects=True)
            if resp.status_code != 200:
                raise RuntimeError(
                    f"HTTP status code '{resp.status_code}' for GET against: {redirect_url_obj.geturl()}"
                )

            # set the login url
            auth_session["dex_login_url"] = resp.url

        ################
        # Attempt Dex Login
        ################
        resp = s.post(
            auth_session["dex_login_url"],
            data={"login": username, "password": password},
            allow_redirects=True,
        )
        if len(resp.history) == 0:
            raise RuntimeError(
                f"Login credentials were probably invalid - "
                f"No redirect after POST to: {auth_session['dex_login_url']}"
            )

        # store the session cookies in a "key1=value1; key2=value2" string
        auth_session["session_cookie"] = "; ".join(
            [f"{c.name}={c.value}" for c in s.cookies]
        )

    return auth_session


KUBEFLOW_ENDPOINT = os.environ.get(
    "KUBEFLOW_ENDPOINT", "https://kubeflow.ui.kubeflow.awsuser.cloudns.ph/"
)
KUBEFLOW_USERNAME = os.environ.get("KUBEFLOW_USERNAME", "user@example.com")
KUBEFLOW_PASSWORD = os.environ.get("KUBEFLOW_PASSWORD", "12341234")

print(f"fetching auth session from {KUBEFLOW_ENDPOINT}")

auth_session = get_istio_auth_session(
    url=KUBEFLOW_ENDPOINT, username=KUBEFLOW_USERNAME, password=KUBEFLOW_PASSWORD
)

INGRESS_GATEWAY = KUBEFLOW_ENDPOINT
NAMESPACE = "kubeflow-user-example-com"
COOKIE = auth_session["session_cookie"]
EXPERIMENT = "Default"

MINIO_ENDPOINT = "s3.amazonaws.com"
LOG_BUCKET = "emlo-s21c"

print(f"creating kfp pipeline client")

client = kfp.Client(host=INGRESS_GATEWAY + "/pipeline", cookies=COOKIE)

# client.create_experiment(EXPERIMENT)
experiments = client.list_experiments(namespace=NAMESPACE)
my_experiment = experiments.experiments[0]


DEPLOY_NAME = "torchserve"
MODEL_NAME = "cifar10"
ISVC_NAME = DEPLOY_NAME + "." + NAMESPACE + "." + "example.com"
INPUT_REQUEST = "https://raw.githubusercontent.com/kubeflow/pipelines/master/samples/contrib/pytorch-samples/cifar10/input.json"

prepare_tensorboard_op = load_component_from_file("yaml/tensorboard_component.yaml")
prep_op = load_component_from_file("yaml/preprocess_component.yaml")
train_op = load_component_from_file("yaml/train_component.yaml")
deploy_op = load_component_from_file("yaml/deploy_component.yaml")
pred_op = load_component_from_file("yaml/prediction_component.yaml")
minio_op = load_component_from_file("yaml/minio_component.yaml")


@dsl.pipeline(name="Training Cifar10 pipeline", description="Cifar 10 dataset pipeline")
def pytorch_cifar10(  # pylint: disable=too-many-arguments
    minio_endpoint=MINIO_ENDPOINT,
    log_bucket=LOG_BUCKET,
    log_dir=f"tensorboard/logs/{dsl.RUN_ID_PLACEHOLDER}",
    mar_path=f"mar/{dsl.RUN_ID_PLACEHOLDER}/model-store",
    config_prop_path=f"mar/{dsl.RUN_ID_PLACEHOLDER}/config",
    model_uri=f"s3://{LOG_BUCKET}/mar/{dsl.RUN_ID_PLACEHOLDER}",
    deploy=DEPLOY_NAME,
    isvc_name=ISVC_NAME,
    model=MODEL_NAME,
    namespace=NAMESPACE,
    confusion_matrix_log_dir=f"confusion_matrix/{dsl.RUN_ID_PLACEHOLDER}/",
    checkpoint_dir="checkpoint_dir/cifar10",
    input_req=INPUT_REQUEST,
    cookie=COOKIE,
    ingress_gateway=INGRESS_GATEWAY,
):
    volume_train = dsl.PipelineVolume(
        volume=k8s.client.V1Volume(
            name="shm", empty_dir=k8s.client.V1EmptyDirVolumeSource(medium="Memory")
        )
    )

    def sleep_op(seconds):
        """Sleep for a while."""
        return dsl.ContainerOp(
            name="Sleep " + str(seconds) + " seconds",
            image="python:alpine3.6",
            command=["sh", "-c"],
            arguments=['python -c "import time; time.sleep($0)"', str(seconds)],
        )

    """This method defines the pipeline tasks and operations"""
    pod_template_spec = json.dumps(
        {
            "spec": {
                "containers": [
                    {
                        "env": [
                            {
                                "name": "AWS_ACCESS_KEY_ID",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "name": "mlpipeline-minio-artifact",
                                        "key": "accesskey",
                                    }
                                },
                            },
                            {
                                "name": "AWS_SECRET_ACCESS_KEY",
                                "valueFrom": {
                                    "secretKeyRef": {
                                        "name": "mlpipeline-minio-artifact",
                                        "key": "secretkey",
                                    }
                                },
                            },
                            {"name": "AWS_REGION", "value": "us-west-2"},
                            {
                                "name": "S3_ENDPOINT",
                                "value": f"{minio_endpoint}",
                            },
                            {"name": "S3_USE_HTTPS", "value": "1"},
                            {"name": "S3_VERIFY_SSL", "value": "0"},
                        ]
                    }
                ]
            }
        }
    )

    prepare_tb_task = prepare_tensorboard_op(
        log_dir_uri=f"s3://{log_bucket}/{log_dir}",
        image="public.ecr.aws/pytorch-samples/tboard:latest",
        pod_template_spec=pod_template_spec,
    ).set_display_name("Visualization")

    prep_task = (
        prep_op().after(prepare_tb_task).set_display_name("Preprocess & Transform")
    )
    confusion_matrix_url = f"minio://{log_bucket}/{confusion_matrix_log_dir}"
    script_args = (
        f"model_name=model.pth," f"confusion_matrix_url={confusion_matrix_url}"
    )
    # For GPU, set number of devices and strategy type
    ptl_args = f"max_epochs=1, accelerator=auto"
    train_task = (
        train_op(
            input_data=prep_task.outputs["output_data"],
            script_args=script_args,
            ptl_arguments=ptl_args,
        )
        .add_pvolumes({"/dev/shm": volume_train})
        .after(prep_task)
        .set_display_name("Training")
        # For allocating resources, uncomment below lines
        .set_memory_request("3000M")
        .set_memory_limit("3000M")
        .set_cpu_request("3000m")
        .set_cpu_limit("3000m")
        .set_gpu_limit(1)
        .add_node_selector_constraint("k8s.amazonaws.com/accelerator", "g4dn")
    )

    (
        minio_op(
            bucket_name=log_bucket,
            folder_name=log_dir,
            input_path=train_task.outputs["tensorboard_root"],
            filename="",
            endpoint="s3.amazonaws.com",
        )
        .after(train_task)
        .set_display_name("Tensorboard Events Pusher")
    )

    (
        minio_op(
            bucket_name=log_bucket,
            folder_name=checkpoint_dir,
            input_path=train_task.outputs["checkpoint_dir"],
            filename="",
            endpoint="s3.amazonaws.com",
        )
        .after(train_task)
        .set_display_name("checkpoint_dir Pusher")
    )

    minio_mar_upload = (
        minio_op(
            bucket_name=log_bucket,
            folder_name=mar_path,
            input_path=train_task.outputs["checkpoint_dir"],
            filename="cifar10_test.mar",
            endpoint="s3.amazonaws.com",
        )
        .after(train_task)
        .set_display_name("Mar Pusher")
    )

    (
        minio_op(
            bucket_name=log_bucket,
            folder_name=config_prop_path,
            input_path=train_task.outputs["checkpoint_dir"],
            filename="config.properties",
            endpoint="s3.amazonaws.com",
        )
        .after(train_task)
        .set_display_name("Conifg Pusher")
    )

    model_uri = str(model_uri)
    # pylint: disable=unused-variable
    isvc_yaml = """
    apiVersion: "serving.kserve.io/v1beta1"
    kind: "InferenceService"
    metadata:
      name: {}
      namespace: {}
    spec:
      predictor:
        volumes:
        - name: dshm
          emptyDir:
            medium: Memory
            sizeLimit: "1024Mi"
        serviceAccountName: sa
        pytorch:
          protocolVersion: v2
          volumeMounts:
          - mountPath: /dev/shm
            name: dshm
            readOnly: false
          storageUri: {}
          resources:
            requests: 
              cpu: 4
              memory: 8Gi
            limits:
              cpu: 4
              memory: 8Gi
    """.format(
        deploy, namespace, model_uri
    )

    # For GPU inference use below yaml with gpu count and accelerator
    gpu_count = "1"
    accelerator = "g4dn"
    isvc_gpu_yaml = """# pylint: disable=unused-variable
    apiVersion: "serving.kserve.io/v1beta1"
    kind: "InferenceService"
    metadata:
      name: {}
      namespace: {}
    spec:
      predictor:
        volumes:
        - name: dshm
          emptyDir:
            medium: Memory
            sizeLimit: "2048Mi"
        serviceAccountName: sa
        pytorch:
          protocolVersion: v2
          volumeMounts:
          - mountPath: /dev/shm
            name: dshm
            readOnly: false
          storageUri: {}
          resources:
            requests: 
              cpu: 3
              memory: 6Gi
            limits:
              cpu: 3
              memory: 6Gi
              nvidia.com/gpu: {}
            nodeSelector:
              k8s.amazonaws.com/accelerator: g4dn
""".format(
        deploy, namespace, model_uri, gpu_count, accelerator
    )
    # Update inferenceservice_yaml for GPU inference
    deploy_task = (
        deploy_op(action="apply", inferenceservice_yaml=isvc_gpu_yaml)
        .after(minio_mar_upload)
        .set_display_name("Deployer")
    )
    # Wait here for model to be loaded in torchserve for inference
    sleep_task = sleep_op(60).after(deploy_task).set_display_name("Sleep")

    dsl.get_pipeline_conf().add_op_transformer(
        use_k8s_secret(
            secret_name="mlpipeline-minio-artifact",
            k8s_secret_key_to_env={
                "secretkey": "MINIO_SECRET_KEY",
                "accesskey": "MINIO_ACCESS_KEY",
            },
        )
    )


print("compiling pipline to tar.gz")
compiler.Compiler().compile(pytorch_cifar10, "pytorch.tar.gz", type_check=True)

print("running pipeline")
run = client.run_pipeline(my_experiment.id, "pytorch-cifar10-ci-run", "pytorch.tar.gz")

print(f"pipeline run created: ", run)

print("waiting for run to finish...")
client.wait_for_run_completion(run.id, 60 * 60)  # wait for 1 hour to finish
print("run finished")
