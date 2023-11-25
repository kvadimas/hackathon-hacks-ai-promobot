FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip && pip3 install -r /app/requirements.txt --no-cache-dir && python3 -m spacy download ru_core_news_lg

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]