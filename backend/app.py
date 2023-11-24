import timeit
import logging

import requests
import uvicorn
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse

# from ml import model


def setup_logging():
    app_logger = logging.getLogger(__name__)
    app_logger.setLevel(logging.INFO)
    app_handler = logging.StreamHandler()
    app_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s : %(message)s")
    app_handler.setFormatter(app_formatter)
    app_logger.addHandler(app_handler)


setup_logging()
_logger = logging.getLogger(__name__)

app = FastAPI(version="1.0")


@app.get("/")
def read_root():
    html_content = """
            <h1>Sales forecast system.</h1>
            <p><a href="http://127.0.0.1:9000/api/v1/send/">
              Запустить систему определения категорий
            </a></p>
            <p><a href="http://127.0.0.1:9000/docs/">
              Документация
            </a></p>
            """
    return HTMLResponse(content=html_content)

@app.post("/api/v1/send/")
async def create_forecast(text: dict):
    '''Запуск системы ml'''
    result = forecast(text)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)


def forecast(text: str) -> dict:
    '''Логика педсказания'''
    res = {
        'group': 'group',
        'sub': 'sub',
        'location': 'location',
        'department': 'department',
    }
    return res
