# Build stage
FROM node:18 AS builder

WORKDIR /app
COPY webapp_frontend /app
RUN npm install && npm run build

# Nginx stage
FROM nginx:stable-alpine
COPY --from=builder /app/dist /usr/share/nginx/html