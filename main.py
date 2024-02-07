import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(f"Привет,{message.from_user.first_name} я бот. Напиши мне что-нибудь")


@dp.message(Command("my_info"))
async def my_info_command(message: types.Message):
    await message.answer(f"Ваш id,{message.from_user.id}\n"
                         f"Ваш username,{message.from_user.username}\n"
                         f"Ваш first_name,{message.from_user.first_name}")

@dp.message(Command("pic"))
async def send_picture(message: types.Message):
    photo = types.FSInputFile("images/cat.jpg")
    photo2 = types.FSInputFile("images/ dog.jpg")
    await message.answer_photo(photo=photo, caption="Котик")
    await message.answer_photo(photo=photo2, caption="Щенок")


@dp.message()
async def echo(message: types.Message):
    # print(message)
    await message.reply(message.text)


async def main():
        await bot.set_my_commands([
            types.BotCommand(command="start", description="Начало"),
            types.BotCommand(command="pic", description="Получить картинку")
            ])

        # запуск бота
        await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
