FROM python:3.8-slim-buster

COPY . .

RUN apt update

RUN apt -y install iputils-ping

RUN python -m pip install -r requirements.txt