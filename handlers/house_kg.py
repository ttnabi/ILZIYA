from aiogram import Router, F, types
from aiogram.filters import Command
from parser_house.house_kg import get_house_links, get_page, MAIN_URL

house_router = Router()


@house_router.callback_query(F.data == 'house')
async def house_kg(call: types.CallbackQuery):
    page = get_page(MAIN_URL)
    houses = get_house_links(page)
    for house in houses:
        await call.message.answer(house)

