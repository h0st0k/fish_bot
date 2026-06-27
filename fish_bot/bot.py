import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик вебхуков от GitHub
async def github_webhook(request):
    data = await request.json()
    if "commits" in data:
        repo_name = data["repository"]["full_name"]
        for commit in data["commits"]:
            message = f"🚀 **Новый пуш в репозиторий!**\n📦 Проект: {repo_name}\n✍️ Автор: {commit['author']['name']}\n💬 Коммит: {commit['message']}"
            # Отправляем сообщение лично вам (замените 111111 на ваш реальный Telegram ID)
            await bot.send_message(chat_id=YOUR_TELEGRAM_ID, text=message, parse_mode="Markdown")
    return web.Response(status=200)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Привет! Ваш Telegram ID: {message.from_user.id}. Скопируйте его.")

async def main():
    # Запуск бота и веб-сервера параллельно
    app = web.Application()
    app.router.add_post('/webhook', github_webhook)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 80)
    asyncio.create_task(site.start())
    
    print("Бот и вебхук-сервер запущены...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
