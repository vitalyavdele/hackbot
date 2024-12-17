from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Шаблоны для работы с HTML
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_game_signal(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
