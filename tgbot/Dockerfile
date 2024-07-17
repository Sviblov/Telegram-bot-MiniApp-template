FROM python:3.11-slim

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY requirements.txt /usr/src
COPY bot.py /usr/src
COPY alembic.ini /usr/src
COPY docker-entrypoint.sh /usr/src

RUN apt-get update
RUN apt-get -y install python3-brotli libpango-1.0-0 libpangoft2-1.0-0

RUN pip install -r /usr/src/requirements.txt

