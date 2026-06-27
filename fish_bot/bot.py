import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Бот успешно запущен в облаке и работает без прокси!")

@dp.message()
async def echo_message(message: types.Message):
    if message.text:
        await message.answer(f"Вы написали: {message.text}")

async def main():
    print("Бот запущен в облаке...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
