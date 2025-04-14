# Build stage
FROM node:18 AS builder

WORKDIR /app
COPY webapp_frontend /app
# 👇 Подменяем .env.prod на .env перед запуском сборки
COPY webapp_frontend/.env.prod /app/.env

RUN npm install && npm run build

# Nginx stage
FROM nginx:stable-alpine

COPY --from=builder /app/dist /usr/share/nginx/html
COPY webapp_frontend/nginx.conf /etc/nginx/conf.d/default.conf