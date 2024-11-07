FROM python:alpine

RUN apk update

WORKDIR /dcelery


RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1


CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]