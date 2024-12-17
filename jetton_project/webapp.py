# Обновленная логика кнопок
from aiogram.types import CallbackQuery

@router.callback_query(lambda c: c.data == "get_signal")
async def send_signal_callback(callback: CallbackQuery):
    grid = generate_mines_signal()
    response = "💡 Вот сигнал на следующий ход:\n\n"
    for row in grid:
        response += " ".join(row) + "\n"

    await callback.message.edit_text(
        response,
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="🔄 Обновить сигнал", callback_data="get_signal")]
            ]
        )
    )
