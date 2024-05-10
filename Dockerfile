FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt update && apt install python3-dev gcc -y

RUN pip install --upgrade pip

COPY requirements.txt requirements-dev.txt /app/

RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

COPY . /app/

ENV EMAIL_HOST=smtp4dev
ENV EMAIL_PORT=25
ENV RABBITMQ_HOST=rabbitmq
ENV REDIS_HOST=redis

EXPOSE 8000
