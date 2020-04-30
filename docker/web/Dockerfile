FROM python:3.8.0-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /app/

RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/
