FROM python:3.11-slim

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src

COPY ./infrastructure /usr/src/infrastructure
COPY ./webapp_backend /usr/src/webapp_backend


RUN pip install -r /usr/src/requirements.txt --pre

CMD ["uvicorn", "webapp_backend.webapp:app", "--host", "0.0.0.0", "--port", "8000"]

