FROM python:2.7.15-alpine3.6

ADD ./requirements.txt /hackapi/requirements.txt

RUN apk update \
    && pip install -r /hackapi/requirements.txt

ADD . /hackapi

WORKDIR /hackepi
CMD ["python", "/hackapi/main.py"]