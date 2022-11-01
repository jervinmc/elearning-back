FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install libmariadb-dev-compat libmariadb-dev build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl libpq-dev libevdev2 build-essential libev-dev
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app/ /app
