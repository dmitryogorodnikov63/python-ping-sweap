FROM python:3.8-slim-buster

COPY . .

RUN python -m pip install -r requirements.txt