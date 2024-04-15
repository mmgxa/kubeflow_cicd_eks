FROM python:3.10.13-slim-bullseye

RUN export DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && apt-get install -yq --no-install-recommends \
  bash \
  curl \
  git \
  sudo \
  unzip \
  vim \
  wget \
  zip \
  python3 \
  python3-pip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && rm -f requirements.txt

RUN sed -i 's/pl.Trainer.from_argparse_args(parser)/pl.Trainer(**trainer_args)/' /usr/local/lib/python3.10/dist-packages/pytorch_kfp_components/components/trainer/executor.py

RUN sed -i 's/trainer.test(model)/trainer.test(model, data_module)/' /usr/local/lib/python3.10/dist-packages/pytorch_kfp_components/components/trainer/executor.py

RUN sed -i 's/minio-service.kubeflow:9000/s3.amazonaws.com/' /usr/local/lib/python3.10/dist-packages/pytorch_kfp_components/components/visualization/executor.py

ENV PYTHONPATH /workspace

WORKDIR /workspace

COPY . .

ENTRYPOINT /bin/bash
