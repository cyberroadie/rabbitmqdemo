FROM jfloff/alpine-python:latest

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENV FLASK_APP=rabbitmqdemo.py
ENTRYPOINT ["flask", "run", "-h", "0.0.0.0"]