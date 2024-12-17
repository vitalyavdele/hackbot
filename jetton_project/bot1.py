import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram import Router

API_TOKEN = '7667200456:AAHEIcix2E6LgEwVsq62wdWa9_fZw-M1qAQ'  # Токен бота

# Инициализация бота, диспетчера и роутера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Клавиатура для команд
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="⭐️ Получить сигнал")]],
    resize_keyboard=True
)

# Веб-приложение кнопка
web_app_url = "https://hackbot-ctyu.onrender.com"  # Обновленный адрес мини-апки
web_app_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📊 Открыть мини-апку", web_app=WebAppInfo(url=web_app_url))]
    ]
)

# Функция генерации "сигнала" для Mines
def generate_mines_signal():
    grid = [["\U0001f536" for _ in range(5)] for _ in range(5)]  # Пустое поле 5x5
    safe_cells = random.sample(range(25), 7)  # 7 безопасных клеток
    for idx in safe_cells:
        row, col = divmod(idx, 5)
        grid[row][col] = "⭐️"  # Звезда для безопасной клетки
    return grid

# Команда /start
@router.message(Command('start'))
async def start_command(message: types.Message):
    await message.answer(
        "Привет! 👋\n"
        "Это **JetSoft AI** – софт, построенный на AI-модели, выдающий точные сигналы для популярных игр с высокой проходимостью.\n\n"
        "🎯 **Что делать дальше?**\n"
        "1. Нажми кнопку **\"Зарегистрироваться и начать играть\"** для запуска приложения.\n"
        "2. Забери бонусы и начни использовать софт!\n\n"
        "🧩 **Публикация бонусов:**\n"
        "Получай промокоды и актуальные бонусы в боте и нашем Telegram-канале. Жми на кнопку ниже, чтобы забрать первый бонус.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(
                    text="🎲 Зарегистрироваться и начать играть", 
                    url="https://t.me/jeton_games/bonus?startapp=cd2HpSuF9kC"
                )],
                [InlineKeyboardButton(text="🤖 Забрать софт", callback_data="get_software")],
                [InlineKeyboardButton(text="🎁 Забрать бонус", callback_data="get_bonus")]
            ]
        )
    )


# Обработка callback для "получить сигнал"
@router.callback_query(lambda c: c.data == "get_signal")
async def callback_get_signal(callback: types.CallbackQuery):
    grid = generate_mines_signal()
    response = "💡 Вот сигнал на следующий ход:\n\n"
    for row in grid:
        response += " ".join(row) + "\n"
    await callback.message.answer(response)
    await callback.answer()

# Команда получения сигнала
@router.message(lambda message: message.text == "⭐️ Получить сигнал")
async def send_signal(message: types.Message):
    grid = generate_mines_signal()
    response = "💡 Вот сигнал на следующий ход:\n\n"
    for row in grid:
        response += " ".join(row) + "\n"
    await message.answer(response)

# Команда открытия мини-апки
@router.message(Command("webapp"))
async def send_web_app_link(message: types.Message):
    await message.answer("Открой мини-апку для сигналов:", reply_markup=web_app_button)

# Запуск бота
async def main():
    print("🚀 Bot started...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
