#!/bin/bash

# Загрузка переменных окружения из .env
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

echo "🚀 Starting Telegram Bot..."
/home/ubuntu/TG_Bot_Boilerplate/.venv/bin/python tgbot &
BOT_PID=$!

echo "🌐 Starting React Frontend..."
cd webapp_frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo "⚙️ Starting FastAPI Backend with Uvicorn..."

uvicorn webapp_backend.webapp:app --host ${BACKEND_HOST} --port ${BACKEND_PORT} \
  --ssl-keyfile=${SSL_KEY} \
  --ssl-certfile=${SSL_CERT} \
  --reload &
BACKEND_PID=$!



echo ""
echo "✅ All services are starting..."
echo "Bot PID: $BOT_PID"
echo "Frontend PID: $FRONTEND_PID"
echo "Backend PID: $BACKEND_PID"

# Wait for all to finish (CTRL+C will kill all)
wait $BOT_PID $FRONTEND_PID $BACKEND_PID