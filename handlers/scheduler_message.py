from aiogram import Router, types
from aiogram.filters import Command
from datetime import datetime

from bot import bot, scheduler

scheduler_message_router = Router()


@scheduler_message_router.message(Command('remain'))
async def send_message(message: types.Message):
    user_id = str(message.from_user.id)
    if user_id in scheduler.get_jobs():
        await message.answer('У вас уже есть запланированное напоминание')
    else:
        text = message.text.replace("/remain ", '')
        scheduler.add_job(send_my_message,
                          'interval',
                          seconds=10,
                          id=user_id,
                          kwargs={'chat_id': user_id,
                                  'text': text})
        await message.answer('Напомни')


async def send_my_message(chat_id: int, text: str):
    await bot.send_message(chat_id=chat_id, text=text)
