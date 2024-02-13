from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.poll_about_books_kb import kb_gender, kb_activities, kb_read, kb_genre


# FSM - Finite State Machine, конечный автомат
class PollAboutBooks(StatesGroup):
    name = State()
    age = State()
    gender = State()
    activities = State()
    education = State()
    read = State()
    genre = State()
    author = State()
    artwork = State()
    advice = State()


poll_about_books_router = Router()


@poll_about_books_router.message(Command("poll_about_books"))
async def start_poll(message: types.Message, state: FSMContext):
    await state.set_state(PollAboutBooks.name)
    await message.answer("Ответьте на вопросы для регистрации.Для завершения введите /stop")
    await message.answer("Как вас зовут?")


@poll_about_books_router.message(Command("stop"))
async def stop_poll(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Спасибо за уделенное время, приходите позже!")


@poll_about_books_router.message(PollAboutBooks.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f"Спасибо, {message.text}")
    await state.set_state(PollAboutBooks.age)
    await message.answer("Сколько вам лет?")


@poll_about_books_router.message(PollAboutBooks.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Возраст должен быть числом!")
    elif int(age) < 12 or int(age) > 80:
        await message.answer("Возраст должен быть от 12 до 80!")
    else:
        await state.update_data(age=message.text)
        await state.set_state(PollAboutBooks.gender)
        await message.answer("Ваш пол?", reply_markup=kb_gender())


@poll_about_books_router.message(PollAboutBooks.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(PollAboutBooks.activities)
    await message.answer("Ваш род деятельности?", reply_markup=kb_activities())


@poll_about_books_router.message(PollAboutBooks.activities)
async def process_activities(message: types.Message, state: FSMContext):
    await state.update_data(activities=message.text)
    await state.set_state(PollAboutBooks.education)
    await message.answer("Ваше образование?", reply_markup=types.ReplyKeyboardRemove())


@poll_about_books_router.message(PollAboutBooks.education)
async def process_education(message: types.Message, state: FSMContext):
    await state.update_data(education=message.text)
    await state.set_state(PollAboutBooks.read)
    await message.answer("Как часто вы читаете художественные книги?", reply_markup=kb_read())


@poll_about_books_router.message(PollAboutBooks.read)
async def process_read(message: types.Message, state: FSMContext):
    await state.update_data(read=message.text)
    await state.set_state(PollAboutBooks.genre)
    await message.answer("Ваш любимый жанр художественной литературы?", reply_markup=kb_genre())


@poll_about_books_router.message(PollAboutBooks.genre)
async def process_genre(message: types.Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(PollAboutBooks.author)
    await message.answer("Ваш любимый автор?", reply_markup=types.ReplyKeyboardRemove())


@poll_about_books_router.message(PollAboutBooks.author)
async def process_author(message: types.Message, state: FSMContext):
    await state.update_data(author=message.text)
    await state.set_state(PollAboutBooks.artwork)
    await message.answer("Ваша любимая художественное произведение?")


@poll_about_books_router.message(PollAboutBooks.artwork)
async def process_artwork(message: types.Message, state: FSMContext):
    await state.update_data(artwork=message.text)
    await state.set_state(PollAboutBooks.advice)
    await message.answer("Какую книгу вы бы посоветовали юному книголюбу?")


@poll_about_books_router.message(PollAboutBooks.advice)
async def process_advice(message: types.Message, state: FSMContext):
    remove_kb = types.ReplyKeyboardRemove()
    await state.update_data(advice=message.text)
    await message.answer("Спасибо")
    data = await state.get_data()
    # save to DataBase
    await message.answer(f"Ваши данные:{data}")
    await state.clear()


