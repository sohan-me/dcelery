FROM python:alpine

RUN apk update

WORKDIR /celeryworker


RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
