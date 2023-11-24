FROM python:3.10.13-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip && pip3 install -r /app/requirements.txt --no-cache-dir

COPY backend .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]