FROM jfloff/alpine-python:latest

RUN mkdir -p ./templates
ADD requirements.txt .
ADD rabbitmqdemo.py .
ADD templates/index.html ./templates

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=rabbitmqdemo.py
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]