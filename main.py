import asyncio
from aiogram import types
import logging
from bot import bot, dp, db, scheduler, set_commands
from handlers import (
    start_router,
    echo_router,
    books_router,
    poll_about_books_router,
    scheduler_message_router,
    house_router,
    group_admin_router
    #  picture_router,

)


async def on_startup():
    db.create_tables()
    # db.populate_tables()


async def main():
    await set_commands()
    # добавляем роутеры
    dp.include_router(start_router)
    dp.include_router(group_admin_router)
    # dp.include_router(picture_router)
    dp.include_router(books_router)
    dp.include_router(poll_about_books_router)
    dp.include_router(scheduler_message_router)
    dp.include_router(house_router)
    # в самом конце
    dp.include_router(echo_router)
    dp.startup.register(on_startup)
    scheduler.start()

    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    # включаем логи
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
