import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Ваш проверенный Telegram ID
USER_CHAT_ID = 8267281287

# Обработчик уведомлений от GitHub вебхука
async def github_webhook(request):
    try:
        data = await request.json()
        if "commits" in data:
            repo_name = data["repository"]["full_name"]
            for commit in data["commits"]:
                message = f"🚀 **Новый пуш в GitHub!**\n📦 Репозиторий: {repo_name}\n✍️ Автор: {commit['author']['name']}\n💬 Коммит: {commit['message']}"
                await bot.send_message(chat_id=USER_CHAT_ID, text=message, parse_mode="Markdown")
    except Exception as e:
        print(f"Ошибка вебхука: {e}")
    return web.Response(status=200)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Бот успешно принимает вебхуки от GitHub.")

async def main():
    # Настраиваем веб-сервер aiohttp на порт 8080 для Amvera
    app = web.Application()
    app.router.add_post('/webhook', github_webhook)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    asyncio.create_task(site.start())
    
    print("Бот и вебхук-приемник успешно запущены...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
