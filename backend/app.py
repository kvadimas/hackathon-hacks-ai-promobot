import os
import timeit
import logging
import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates


from serializers import ForecastRequest, ForecastResponse
from model import forecast
#from chat import chat_forecast -проверка концепции генеративной системы
from ner import get_location


logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

app = FastAPI(version="1.0")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    ''' Демо страница '''
    logger.info(f'Start index.html')
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/v1/send/", response_model=ForecastResponse)
async def create_forecast(message: ForecastRequest):
    '''Запуск системы ml'''
    start_time = timeit.default_timer()
    logger.debug(f'Message: {message.text.strip()}')
    try:
        sub = forecast(message.text.strip())
        group = department = 'Пока не работает'
        location = get_location(message.text.strip())
        result: dict = {
            'group': group,
            'sub': sub,
            'location': location,
            'department': department,
            'text': message.text.strip(),
        }
        elapsed_time = timeit.default_timer() - start_time
        logger.info(f'Elapsed time: {elapsed_time}')
        return JSONResponse(content=result, status_code=200)
    except:
        logger.error(f'Error forecast')
        return JSONResponse(content={"error": "error forecast"}, status_code=500)


if __name__ == "__main__":
    port = int(os.environ['VCAP_APP_PORT'])
    uvicorn.run(app, host="0.0.0.0", port=port)
