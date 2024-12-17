from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

# Генерация сигнала
def generate_signal():
    grid = [["🟦" for _ in range(5)] for _ in range(5)]
    safe_cells = random.sample(range(25), 7)
    for idx in safe_cells:
        row, col = divmod(idx, 5)
        grid[row][col] = "⭐️"
    return grid

# Главная страница
@app.get("/", response_class=HTMLResponse)
async def root():
    signal = generate_signal()
    grid_html = "<br>".join([" ".join(row) for row in signal])
    html_content = f"""
    <html>
        <head><title>Jetton Signals</title></head>
        <body>
            <h1>Сигнал для игры Mines</h1>
            <pre>{grid_html}</pre>
            <button onclick="window.location.reload()">Обновить сигнал</button>
        </body>
    </html>
    """
    return html_content
