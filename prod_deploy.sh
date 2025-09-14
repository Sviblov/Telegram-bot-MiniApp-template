#!/bin/bash

# === Create network if it doesn't exist ===
docker network inspect tgbotnetwork >/dev/null 2>&1 || docker network create tgbotnetwork
docker network connect tgbotnetwork redis
docker network connect postgres_dev redis

# # === TG BOT ===
docker rm -f tg_bot 2>/dev/null || true
docker build -t tg_bot_image -f tgbot/Dockerfile .
docker run -d \
  --name tg_bot \
  --env-file .env.prod \
  --network tgbotnetwork \
  tg_bot_image

# # === BACKEND ===
docker rm -f webapp_backend 2>/dev/null || true
docker build -t webapp_backend_image -f webapp_backend/Dockerfile .
docker run -d \
  --name webapp_backend \
  --env-file .env.prod \
  --network tgbotnetwork \
  -p 8000:8000 \
  webapp_backend_image

# # === FRONTEND ===
docker rm -f webapp_frontend 2>/dev/null || true
docker build -t webapp_frontend_image -f webapp_frontend/Dockerfile .
docker run -d \
  --name webapp_frontend \
  --network tgbotnetwork \
  -p 4001:4001 \
  webapp_frontend_image

# # === NGINX ===
docker rm -f nginx_proxy 2>/dev/null || true
docker build -t nginx_proxy_image -f nginx/Dockerfile .
docker run -d \
  --name nginx_proxy \
  --network tgbotnetwork \
  -p 4000:443 \
  nginx_proxy_image