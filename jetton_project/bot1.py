import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, WebAppInfo,
    InlineKeyboardButton, InlineKeyboardMarkup
)
from aiogram.filters import Command
from aiogram import Router

# Токен бота
API_TOKEN = '7667200456:AAHEIcix2E6LgEwVsq62wdWa9_fZw-M1qAQ'

# Инициализация бота, диспетчера и роутера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Ссылки
casino_url = "https://t.me/jeton_games/bonus?startapp=cd2HpSuF9kC"
web_app_url = "https://hackbot-ctyu.onrender.com"

# Клавиатура с двумя кнопками
welcome_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Забрать бонус", url=casino_url)],
        [InlineKeyboardButton(text="🤖 Запустить софт", web_app=WebAppInfo(url=web_app_url))]
    ]
)

# Хэндлер для команды /start
@router.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать в **JetSoft AI**!\n\n"
        "Это AI-софт для точных прогнозов игр с высокой проходимостью.\n\n"
        "🚀 Нажми на одну из кнопок ниже, чтобы начать прямо сейчас:",
        reply_markup=welcome_buttons
    )

# Генерация сигналов для игры Mines
def generate_mines_signal():
    grid = [["⬛" for _ in range(5)] for _ in range(5)]  # Создание 5x5 сетки
    safe_cells = random.sample(range(25), 7)  # 7 безопасных клеток
    for idx in safe_cells:
        row, col = divmod(idx, 5)
        grid[row][col] = "⭐️"  # Пометка безопасной клетки
    return grid

# Callback для "получить сигнал"
@router.callback_query(lambda c: c.data == "get_signal")
async def callback_get_signal(callback: types.CallbackQuery):
    grid = generate_mines_signal()
    response = "💡 Вот сигнал на следующий ход:\n\n"
    for row in grid:
        response += " ".join(row) + "\n"
    await callback.message.answer(response)
    await callback.answer()

# Запуск бота
async def main():
    print("🚀 JetSoft AI бот запущен и работает!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
