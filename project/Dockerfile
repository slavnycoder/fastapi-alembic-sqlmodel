FROM python:3.10-slim-bullseye

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --disable-pip-version-check --no-cache-dir

COPY . /usr/src/fastapi_be/
WORKDIR /usr/src/fastapi_be/
