FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip && pip3 install -r /app/requirements.txt --no-cache-dir && python3 -m spacy download ru_core_news_lg

COPY . .

ENV VCAP_APP_PORT=9000

CMD ["python", "app.py"]