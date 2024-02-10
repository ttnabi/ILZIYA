from aiogram import Router, types
from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}, я бот. Напиши мне что-нибудь")
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text="Наш Инстаграм", url="https://instagram.com/")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ]
        ]
    )
    await message.answer(f"Привет, {message.from_user.first_name}, я бот.", reply_markup=kb)


@start_router.callback_query(F.data == "about_us")
async def show_about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Что-то о нас")
