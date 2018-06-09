FROM python:2.7.15-alpine3.6

ADD . /

RUN apk update && pip install -r requirements.txt

CMD ["python", "main.py"]