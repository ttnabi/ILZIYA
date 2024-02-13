from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def kb_gender():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Мужской"),
                KeyboardButton(text="Женский"),
            ],
        ],
        resize_keyboard=True
    )
    return kb


def kb_activities():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Учеба"),
                KeyboardButton(text="Работа"),
            ],
            [
                KeyboardButton(text="Бизнес"),
                KeyboardButton(text="Наука"),
            ],
            [
                KeyboardButton(text="Другое"),
            ],
        ],
        resize_keyboard=True
    )
    return kb


def kb_read():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Не так часто"),
                KeyboardButton(text="Очень часто"),
            ],
        ],
        resize_keyboard=True
    )
    return kb


def kb_genre():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Роман"),
                KeyboardButton(text="Детектив"),
            ],
            [
                KeyboardButton(text="Драма"),
                KeyboardButton(text="Фэнтэзи"),
            ],
            [
                KeyboardButton(text="Комиксы")
            ],
        ],
        resize_keyboard=True
    )
    return kb
