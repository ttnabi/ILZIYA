# from aiogram import Router, types
from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start_command(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш адрес", callback_data="Ибраимова 5"),
                types.InlineKeyboardButton(text="Наши контакты", callback_data="0999887070")
            ],
            [
                types.InlineKeyboardButton(text="Наш instagram", url="https://www.instagram.com/book_shop.kg"),
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ]
        ]
    )
    await message.answer(f"Добро пожаловать, {message.from_user.first_name}", reply_markup=kb)


@start_router.callback_query(F.data == "about_us")
async def show_about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Наша книжная лавка на рынке с 2018 года.\n"
                                  "Мы дорожим каждым нашим клиентом,поэтому высокое качество сервиса-\n"
                                  "приоритет для нас.Вы всегда можете задать интересующие вас вопросы\n"
                                  "в онлайн-режиме или по телефону и получить подробную информацию ")


@start_router.callback_query(F.data == "Ибраимова 5")
async def snow_ibraimova_5(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Ибраимова 5")


@start_router.callback_query(F.data == "0999887070")
async def snow_0999887070(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("0999887070")

