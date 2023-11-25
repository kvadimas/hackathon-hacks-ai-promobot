import timeit
import logging
import uvicorn

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from serializers import ForecastRequest, ForecastResponse
from model import forecast
#from chat import chat_forecast -проверка концепции генеративной системы
from ner import get_location


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

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    ''' Демо страница '''
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/v1/send/", response_model=ForecastResponse)
async def create_forecast(message: ForecastRequest):
    '''Запуск системы ml'''
    start_time = timeit.default_timer()
    group, sub, department = forecast(message.text.strip())
    location = get_location(message.text.strip())
    result: dict = {
        'group': group,
        'sub': sub,
        'location': location,
        'department': department,
        'text': message.text.strip(),
    }
    elapsed_time = timeit.default_timer() - start_time
    _logger.info(f'Elapsed time: {elapsed_time}')
    return JSONResponse(content=result, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
