FROM python:3.11-alpine

WORKDIR /app

COPY src /app

ENTRYPOINT ["python", "app.py"]