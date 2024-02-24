from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
from db.base import DB
from apscheduler.schedulers.asyncio import AsyncIOScheduler


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()
db = DB()
scheduler = AsyncIOScheduler()


async def set_commands():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        # types.BotCommand(command="pic", description="Получить картинку"),
        types.BotCommand(command="books", description="Получить книгу"),
        types.BotCommand(command="poll_about_books", description="Опрос про книги")
    ])

