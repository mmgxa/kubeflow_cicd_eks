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

RUN python3 -m pip install -r \
    requirements.txt --quiet --no-cache-dir \
    && rm -f requirements.txt

WORKDIR /app

COPY kservedeployer.py /app

ENTRYPOINT ["python"]
CMD ["kservedeployer.py"]
