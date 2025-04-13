#!/bin/bash

echo "🚀 Starting Telegram Bot..."
/home/ubuntu/TG_Bot_Boilerplate/.venv/bin/python /home/ubuntu/TG_Bot_Boilerplate/tgbot/__main__.py &
BOT_PID=$!

echo "🌐 Starting React Frontend..."
cd webapp_frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo "⚙️ Starting FastAPI Backend with Uvicorn..."

uvicorn webapp_backend.webapp:app --host 0.0.0.0 --port 8000 \
  --ssl-keyfile=./nginx/ssl/key.pem \
  --ssl-certfile=./nginx/ssl/cert.pem \
  --reload &
BACKEND_PID=$!


echo ""
echo "✅ All services are starting..."
echo "Bot PID: $BOT_PID"
echo "Frontend PID: $FRONTEND_PID"
echo "Backend PID: $BACKEND_PID"

# Wait for all to finish (CTRL+C will kill all)
wait $BOT_PID $FRONTEND_PID $BACKEND_PID