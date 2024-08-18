from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Рассчитать')
            ],
        [KeyboardButton(text='Купить')]
        ], resize_keyboard=True
)

kb2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
        ]
    ]
)

kb3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Витамин А', callback_data='product_buying'),
            InlineKeyboardButton(text='Витамин B', callback_data='product_buying'),
            InlineKeyboardButton(text='Витамин D3', callback_data='product_buying'),
            InlineKeyboardButton(text='Витамин A&D', callback_data='product_buying')
        ]
    ]
)


get_all_products()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Информация'])
async def inform(message):
    await message.answer('Информация о боте')


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    with open('files/A.png', "rb") as img:
        await message.answer_photo(img, f'Название: {products[0][1]} | Описание: {products[0][2]} | '
                                        f'Цена: {products[0][3]} руб.')
    with open('files/B.png', "rb") as img:
        await message.answer_photo(img, f'Название: {products[1][1]} | Описание: {products[1][2]} | '
                                        f'Цена: {products[1][3]} руб.')
    with open('files/D.png', "rb") as img:
        await message.answer_photo(img, f'Название: {products[2][1]} | Описание: {products[2][2]} | '
                                        f'Цена: {products[2][3]} руб.')
    with open('files/A&D.png', "rb") as img:
        await message.answer_photo(img, f'Название: {products[3][1]} | Описание: {products[3][2]} | '
                                        f'Цена: {products[3][3]} руб.')
        await message.answer('Выберите продукт для покупки:', reply_markup=kb3)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    value = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша норма потребления: {value} калорий.')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
