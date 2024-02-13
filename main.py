import asyncio
from aiogram import types
import logging
from bot import bot, dp, set_commands
from handlers import (
    start_router,
    echo_router,
    books_router,
    poll_about_books_router
    #  picture_router,
)


async def main():
    await set_commands()
    # добавляем роутеры
    dp.include_router(start_router)
    # dp.include_router(picture_router)
    dp.include_router(books_router)
    dp.include_router(poll_about_books_router)

    # в самом конце
    dp.include_router(echo_router)

    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    # включаем логи
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
