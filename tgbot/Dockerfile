FROM python:3.11-slim

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./tgbot /usr/src/tgbot
COPY ./infrastructure /usr/src/infrastructure
COPY requirements.txt /usr/src

COPY alembic.ini /usr/src
COPY ./tgbot/docker-entrypoint-bot.sh /usr/src
# Копируем код бота



# Копируем entrypoint-скрипт (если он нужен)

RUN chmod +x /usr/src/docker-entrypoint-bot.sh

# RUN apt-get update
# RUN apt-get -y install python3-brotli libpango-1.0-0 libpangoft2-1.0-0

RUN pip install -r /usr/src/requirements.txt

CMD ["bash", "/usr/src/docker-entrypoint-bot.sh"]

