from aiogram import Router, F, types
from aiogram.filters import Command

books_router = Router()


@books_router.message(Command("books"))
async def show_all_books(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Роман"),
                types.KeyboardButton(text="Детектив"),
            ],
            [
                types.KeyboardButton(text="Драма"),
                types.KeyboardButton(text="Фэнтэзи"),
            ],
            [
                types.KeyboardButton(text="Комиксы"),
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(f"Выберите жанр книги из меню ниже", reply_markup=kb)

    @books_router.message(F.text == "Роман")
    async def show_romance(message: types.Message):
        kb = types.ReplyKeyboardRemove()
        await message.answer("Жанр:Роман\n"
                             "Рекомендуемые книги:\n"
                             "Сломанная кукла. Автор:Янка Рам\n"
                             "Не твой сын. Автор:Екатерина Кариди\n"
                             "Есть, молиться, любить. Автор:Элизабет Гилберт", reply_markup=kb)

    @books_router.message(F.text == "Детектив")
    async def show_detective(message: types.Message):
        kb = types.ReplyKeyboardRemove()
        await message.answer("Жанр:Детектив\n"
                             "Рекомендуемые книги:\n"
                             "Морозный ветер атаки. Автор:Александр Тамоников\n"
                             "Путешествие дилетанта. Автор:Сергей Петросян\n"
                             "Мистер Х. Автор:Рубенс", reply_markup=kb)

    @books_router.message(F.text == "Драма")
    async def show_drama(message: types.Message):
        kb = types.ReplyKeyboardRemove()
        await message.answer("Жанр:Драма\n"
                             "Рекомендуемые книги:\n"
                             "Дубровский. Автор:Александр Пушкин\n"
                             "Вишневый сад. Автор:Антон Чехов\n"
                             "На дне. Автор:Максим Горький", reply_markup=kb)

    @books_router.message(F.text == "Фэнтэзи")
    async def show_fantasy(message: types.Message):
        kb = types.ReplyKeyboardRemove()
        await message.answer("Жанр:Фэнтэзи\n"
                             "Рекомендуемые книги:\n"
                             "Властелин колец. Автор:Джон Толкин\n"
                             "Гарри Поттер. Автор:Джоан Роулинг\n"
                             "Алиса в стране чудес. Автор:Льюис Кэрролл", reply_markup=kb)

    @books_router.message(F.text == " Комиксы")
    async def show_comics(message: types.Message):
        kb = types.ReplyKeyboardRemove()
        await message.answer("Жанр:Комиксы\n"
                             "Рекомендуемые книги:\n"
                             "Пес, смотрящий на звезды. Автор:Такаси Мураками\n"
                             "Город надгробий. Автор:Дзюндзи Ито\n"
                             "Говори. Автор:Лори Холс Андерсон", reply_markup=kb)
