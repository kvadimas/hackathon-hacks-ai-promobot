FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y nano && pip3 install --upgrade pip && pip3 install -r /requirements.txt --no-cache-dir

COPY .

CMD ["uvicorn", "backend.app:app", "--host", "127.0.0.1", "--port", "9000"]