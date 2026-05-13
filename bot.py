import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Токен берем из переменных окружения (как мы уже научились)
API_TOKEN = os.getenv("8718934345:AAHeySKN6WsrG9Yj2qudmCdbNm-m1QPAXkU")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "⏰ Я — бот-таймер.\n\n"
        "Напиши мне: `минуты текст`\n"
        "Пример: `5 проверить духовку`"
    )

@dp.message()
async def set_timer(message: types.Message):
    try:
        # Разбиваем сообщение: первое слово — минуты, остальное — текст
        parts = message.text.split(maxsplit=1)
        minutes = float(parts[0])
        text = parts[1] if len(parts) > 1 else "Время вышло!"

        await message.answer(f"✅ Понял, напомню через {minutes} мин: '{text}'")

        # Ждем нужное количество секунд
        await asyncio.sleep(minutes * 60)

        # Отправляем напоминание
        await message.answer(f"🔔 **НАПОМИНАНИЕ:**\n\n{text}")

    except (ValueError, IndexError):
        await message.answer("⚠️ Напиши в формате: `число текст`. Например: `2 чай готов`")

async def main():
    print("Бот-таймер запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
