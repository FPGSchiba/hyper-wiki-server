FROM python:3.11-slim

WORKDIR /app

COPY ./data data
COPY ./requirements.txt requirements.txt
COPY ./src src
COPY ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y supervisor
RUN apt-get install -y gcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/bin/supervisord"]