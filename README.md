<div align="center">

# CI/CD with Kubeflow Pipelines on EKS with GPU and External Domain

</div>

# Overview
In this session, we deploy an end-to-end CI/CD pipeline in Kubeflow provisioned inside EKS. This pipeline builds a docker image, pushes it to ECR, trains a model on GPU and deploys it on GPU as well. All of these steps are run as part of GitHub Actions, which required setting up a domain and a load balancer. Inference is run on a machine independent of the EKS cluster itself. 


# Setup

All of these steps are mentioned in the [setup guide](./setup.md).



# Running the CI/CD Pipeline
The GitHub Action has been configured to run manually, although we can modify it to run on push.

To ensure that the action workflow can commit to the repository during a run, enable 'Read and write permissions' in the repository settings. Also, set the action secrets with a the access key and secret access key of a user that has read/write permissions to Public ECR.

![](./images/01_actions_perm.png)

# Runs
Once the workflow completes, we can see a successful run
![](./images/02_runs.png)

as well as all the steps.
![](./images/03_workflow.png)


# Serving

In the logs, we can see that GPU is indeed being used for serving
![](./images/04_gpu_serve.png)

Also, during inference, we can see GPU utilization metrics.

![](./images/05_gpu_use.png)

The complete logs can be seen [here](./logs/kserve_log.md)
# Inference Demo

[![Demo](https://img.youtube.com/vi/0cRaHH-2Tu4/hqdefault.jpg)](https://www.youtube.com/embed/0cRaHH-2Tu4)


