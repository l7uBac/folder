from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = 'Рассчитать'),
                                    KeyboardButton(text = 'Информация')]], resize_keyboard = True)

kb2 = InlineKeyboardMarkup()
bt = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
bt2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data = 'formulas')
kb2.row(bt, bt2)

@dp.message_handler(commands = ['start'])
async def start(message):
    await message.answer(f'Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)

@dp.message_handler(text = ['Информация'])
async def main_menu(message):
    await message.answer(f'Я бот, помогающий расчитать твою суточную норму каллорий, '
                         f'исходя из твоей активности в течении дня.')

@dp.message_handler(text = ['Рассчитать'])
async def main_menu_2(message):
    await message.answer(f'Выберите опцию:', reply_markup = kb2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text = ['formulas'])
async def get_formulas(call):
    await call.message.answer(f'(10 x вес(кг) + 6,25 х рост(см) - 5 х возраст(лет) + 5) x 1.375')
    await call.answer()

@dp.callback_query_handler(text = ['calories'])
async def set_age(call):
    await call.message.answer(f'Введите свой возраст (полных лет):')
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer(f'Введите свой рост (в см):')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer(f'Введите свой вес (в кг):')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    # Минимальная активность: A = 1, 2.
    A = 1.375 # Слабая активность:
    # Средняя активность: A = 1, 55.
    # Высокая активность: A = 1, 725.
    # Экстра активность: A = 1, 9
    Calories = round(((10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5) * A), 1)
    await message.answer(f'Ваша суточная норма калорий: {Calories}')
    await state.finish()

@dp.message_handler()
async  def all_massages(message):
    await message.answer(f'Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)