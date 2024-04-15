# Setup Guide

## Setup Route53
For external access to the EKS cluster, we need a domain name. We can get a (free!) hosted zone from ClouDNS.  
We then create a hosted zone in Route53 (which is a subdomain of the one created in ClouDNS), and add the 'route to'  servers in Route53 to ClouDNS

## Create Cluster
We export a few environment variables before proceeding:

```bash
export PIPELINE_S3_CREDENTIAL_OPTION="irsa"
export CLUSTER_REGION=us-west-2
export CLUSTER_NAME==****
export S3_BUCKET==****
export MINIO_SERVICE_HOST=s3.amazonaws.com
export AWS_ACCOUNT_ID==****

```
>Note: For this deployment, a VPC (with public subnets only) is created manually and then used for the cluster.

```bash
envsubst < 00_cluster.yaml | eksctl create cluster -f -
```

## Install the Metrics API (Optional)

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

## Enable Cluster Autoscaling
```bash
aws iam create-policy --policy-name AWSClusterAutoScalerIAMPolicy --policy-document file://00a_cas-iam-policy.json

eksctl create iamserviceaccount \
--cluster=${CLUSTER_NAME} \
--namespace=kube-system \
--name=cluster-autoscaler \
--attach-policy-arn=arn:aws:iam::${AWS_ACCOUNT_ID}:policy/AWSClusterAutoScalerIAMPolicy \
--override-existing-serviceaccounts \
--region ${CLUSTER_REGION} \
--approve

envsubst < 00b_cluster-autoscaler-autodiscover.yaml | kubectl apply -f -
```

##  Enable S3 support only for Kubeflow in EKS

```bash
export OIDC_PROVIDER_URL=$(aws eks describe-cluster --name $CLUSTER_NAME \
    --region $CLUSTER_REGION --query "cluster.identity.oidc.issuer" \
    --output text | cut -c9-)

cat 01_backend-trust_src.json | envsubst > 01_backend-trust.json
export PIPELINE_BACKEND_ROLE_NAME=kf-pipeline-backend-role-$CLUSTER_NAME
aws --region $CLUSTER_REGION iam create-role --role-name $PIPELINE_BACKEND_ROLE_NAME --assume-role-policy-document file://01_backend-trust.json
export BACKEND_ROLE_ARN=$(aws --region $CLUSTER_REGION iam get-role --role-name $PIPELINE_BACKEND_ROLE_NAME --output text --query 'Role.Arn')

cat 02_profile-trust_src.json | envsubst > 02_profile-trust.json
export PROFILE_ROLE_NAME=kf-pipeline-profile-role-$CLUSTER_NAME
aws --region $CLUSTER_REGION iam create-role --role-name $PROFILE_ROLE_NAME --assume-role-policy-document file://02_profile-trust.json
export PROFILE_ROLE_ARN=$(aws --region $CLUSTER_REGION iam get-role --role-name $PROFILE_ROLE_NAME --output text --query 'Role.Arn')

cat 03_s3_policy_src.json | envsubst > 03_s3_policy.json
aws --region $CLUSTER_REGION iam put-role-policy --role-name $PIPELINE_BACKEND_ROLE_NAME --policy-name kf-pipeline-s3 --policy-document file://03_s3_policy.json
aws --region $CLUSTER_REGION iam put-role-policy --role-name $PROFILE_ROLE_NAME --policy-name kf-pipeline-s3 --policy-document file://03_s3_policy.json


# Modify the ARNs
yq e '.s3.roleArn = env(BACKEND_ROLE_ARN)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/rds-s3/values.yaml
yq e '.s3.roleArn = env(BACKEND_ROLE_ARN)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/s3-only/values.yaml
yq e '.awsIamForServiceAccount.awsIamRole = env(PROFILE_ROLE_ARN)' -i kubeflow-manifests/charts/common/user-namespace/values.yaml
```

## Install AWS Secrets & Configuration Provider with Kubernetes Secrets Store CSI driver

```bash
eksctl create iamserviceaccount  --name kubeflow-secrets-manager-sa --namespace kubeflow --cluster $CLUSTER_NAME --attach-policy-arn arn:aws:iam::aws:policy/AmazonSSMReadOnlyAccess --attach-policy-arn arn:aws:iam::aws:policy/SecretsManagerReadWrite --override-existing-serviceaccounts --approve --region $CLUSTER_REGION

kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/secrets-store-csi-driver/v1.3.2/deploy/rbac-secretproviderclass.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/secrets-store-csi-driver/v1.3.2/deploy/csidriver.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/secrets-store-csi-driver/v1.3.2/deploy/secrets-store.csi.x-k8s.io_secretproviderclasses.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/secrets-store-csi-driver/v1.3.2/deploy/secrets-store.csi.x-k8s.io_secretproviderclasspodstatuses.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/secrets-store-csi-driver/v1.3.2/deploy/secrets-store-csi-driver.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/secrets-store-csi-driver/v1.3.2/deploy/rbac-secretprovidersyncing.yaml
kubectl apply -f https://raw.githubusercontent.com/aws/secrets-store-csi-driver-provider-aws/main/deployment/aws-provider-installer.yaml

yq e '.s3.bucketName = env(S3_BUCKET)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/rds-s3/values.yaml
yq e '.s3.minioServiceRegion = env(CLUSTER_REGION)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/rds-s3/values.yaml
yq e '.s3.minioServiceHost = env(MINIO_SERVICE_HOST)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/rds-s3/values.yaml
yq e '.s3.bucketName = env(S3_BUCKET)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/rds-s3-static/values.yaml
yq e '.s3.minioServiceRegion = env(CLUSTER_REGION)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/rds-s3-static/values.yaml
yq e '.s3.minioServiceHost = env(MINIO_SERVICE_HOST)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/rds-s3-static/values.yaml
yq e '.s3.bucketName = env(S3_BUCKET)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/s3-only/values.yaml
yq e '.s3.minioServiceHost = env(MINIO_SERVICE_HOST)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/s3-only/values.yaml
yq e '.s3.minioServiceRegion = env(CLUSTER_REGION)' -i kubeflow-manifests/charts/apps/kubeflow-pipelines/s3-only/values.yaml

```
## Setup EBS Access

### Create IRSA for EBS

```bash
eksctl create iamserviceaccount \
  --name ebs-csi-controller-sa \
  --namespace kube-system \
  --cluster ${CLUSTER_NAME} \
  --role-name AmazonEKS_EBS_CSI_DriverRole \
  --role-only \
  --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
  --approve \
  --region ${CLUSTER_REGION}
```

### Create the EBS CSI Driver Addon


```bash
eksctl create addon --name aws-ebs-csi-driver --cluster ${CLUSTER_NAME} --service-account-role-arn arn:aws:iam::${AWS_ACCOUNT_ID}:role/AmazonEKS_EBS_CSI_DriverRole --region ${CLUSTER_REGION} --force

```


## Clone Kubeflow Repos

```bash
export KUBEFLOW_RELEASE_VERSION=v1.7.0
export AWS_RELEASE_VERSION=v1.7.0-aws-b1.0.3
git clone https://github.com/awslabs/kubeflow-manifests.git && cd kubeflow-manifests
git checkout ${AWS_RELEASE_VERSION}
git clone --branch ${KUBEFLOW_RELEASE_VERSION} https://github.com/kubeflow/manifests.git upstream
```

edit the following section in `Makefile`

```
install-helm: 
	wget <https://get.helm.sh/helm-v3.12.2-linux-amd64.tar.gz>
	tar -zxvf helm-v3.12.2-linux-amd64.tar.gz
	sudo mv linux-amd64/helm /usr/local/bin/helm
	helm version
```

## Install Pre-reqs for Kubeflow
```bash
make install-tools
```


## Install Kubeflow
```bash
make deploy-kubeflow INSTALLATION_OPTION=helm DEPLOYMENT_OPTION=s3-only PIPELINE_S3_CREDENTIAL_OPTION=$PIPELINE_S3_CREDENTIAL_OPTION
```

## Enable Kubeflow Pipelines access from Jupyter
```bash
kubectl apply -f 04_access_kfp_from_jupyter_notebook.yaml
```


## Configure Load Balancer
```bash
cd kubeflow-manifests/tests/e2e
export hostedzoneid=****
export hostedzone=****
export hostedzonesub=****
yq e '.cluster.name = env(CLUSTER_NAME)' -i utils/load_balancer/config.yaml
yq e '.cluster.region = env(CLUSTER_REGION)' -i utils/load_balancer/config.yaml
yq e '.route53.rootDomain.hostedZoneId = env(hostedzoneid)' -i utils/load_balancer/config.yaml
yq e '.route53.rootDomain.name = env(hostedzone)' -i utils/load_balancer/config.yaml
yq e '.route53.subDomain.name = env(hostedzonesub)' -i utils/load_balancer/config.yaml
PYTHONPATH=.. python3.8 utils/load_balancer/setup_load_balancer.py
```

## Enable S3 Access
For this part, you need to create a user with permissions to write to (a specific bucket in) S3. Create a key, and encode it using

```bash
echo -n {access_key} | base64 
echo -n {secret_access_key} | base64 
```

```bash
envsubst < 05_s3-secret-sa.yaml | kubectl apply -f -
```

## ConfigMap Patch
We update the Knative domain that is used for the KServe routes.

Example guides including the ones [here](https://knative.dev/docs/serving/using-a-custom-domain/#configuring-the-default-domain-for-all-knative-services-on-a-cluster) and [here](https://ibm.github.io/manifests/docs/deployment/authentication/#optional---kserve-configuration)

```bash
kubectl patch cm config-domain --patch '{"data":{"emlo.mmg":""}}' -n knative-serving
```
