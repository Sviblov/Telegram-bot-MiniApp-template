#!/bin/bash

# Загрузка переменных окружения из .env
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
else
  echo "⚠️ .env file not found. Some variables might be missing."
fi

# Функции запуска
start_bot() {
  echo "🚀 Starting Telegram Bot..."
  /home/ubuntu/TG_Bot_Boilerplate/.venv/bin/python tgbot &
  BOT_PID=$!
  echo "✅ Bot PID: $BOT_PID"
}

start_frontend() {
  echo "🌐 Starting React Frontend..."
  pushd webapp_frontend > /dev/null
  npm run dev &
  FRONTEND_PID=$!
  popd > /dev/null
  echo "✅ Frontend PID: $FRONTEND_PID"
}

start_backend() {
  echo "⚙️ Starting FastAPI Backend with Uvicorn..."
  : "${BACKEND_HOST:?BACKEND_HOST is not set}"
  : "${BACKEND_PORT:?BACKEND_PORT is not set}"
  : "${SSL_KEY:?SSL_KEY is not set}"
  : "${SSL_CERT:?SSL_CERT is not set}"
  
  uvicorn webapp_backend.webapp:app --host ${BACKEND_HOST} --port ${BACKEND_PORT} \
    --ssl-keyfile=${SSL_KEY} \
    --ssl-certfile=${SSL_CERT} \
    --reload &
  BACKEND_PID=$!
  echo "✅ Backend PID: $BACKEND_PID"
}

# Меню выбора
echo ""
echo "Chose component to start:"
echo "1) Telegram Bot"
echo "2) Frontend (React)"
echo "3) Backend (FastAPI)"
echo "4) All"
echo ""

read -p "Your selection (1-4, Enter to start all): " choice
echo ""

# Если пользователь просто нажал Enter, ставим choice=4
if [ -z "$choice" ]; then
  choice=4
fi

case "$choice" in
  1)
    start_bot
    wait $BOT_PID
    ;;
  2)
    start_frontend
    wait $FRONTEND_PID
    ;;
  3)
    start_backend
    wait $BACKEND_PID
    ;;
  4)
    start_bot
    start_frontend
    start_backend
    echo ""
    echo "🔄 Все компоненты запущены."
    wait $BOT_PID $FRONTEND_PID $BACKEND_PID
    ;;
  *)
    echo "❌ Неверный выбор. Завершение работы."
    exit 1
    ;;
esac
