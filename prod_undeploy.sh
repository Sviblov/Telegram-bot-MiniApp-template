#!/bin/bash

# # === TG BOT ===
docker rm -f tg_bot 2>/dev/null || true


# # === BACKEND ===
docker rm -f webapp_backend 2>/dev/null || true


# # === FRONTEND ===
docker rm -f webapp_frontend 2>/dev/null || true


# # === NGINX ===
docker rm -f nginx_proxy 2>/dev/null || true

