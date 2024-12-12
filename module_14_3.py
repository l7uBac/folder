from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Рассчитать'),
                                    KeyboardButton(text='Информация')],
                                   [KeyboardButton(text='Купить')]], resize_keyboard=True)

kb2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
                      InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]],
    resize_keyboard=True)

kb3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
                                             InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
                                             InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
                                             InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')]],
                           resize_keyboard=True)

kb4 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Мужской'),
                                     KeyboardButton(text='Женский')]], resize_keyboard=True)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет! '
                         f'Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Информация'])
async def main_menu(message):
    await message.answer(f'Я бот, помогающий расчитать твою суточную норму каллорий, '
                         f'исходя из твоей активности в течении дня.')


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    with open('Продукт_1.jpg', 'rb') as img1:
        await message.answer(f'Название: Product {1} | Описание: описание {1} | Цена: {1 * 100}')
        await message.answer_photo(img1)
    with open('Продукт_2.jpg', 'rb') as img2:
        await message.answer(f'Название: Product {2} | Описание: описание {2} | Цена: {2 * 100}')
        await message.answer_photo(img2)
    with open('Продукт_3.jpg', 'rb') as img3:
        await message.answer(f'Название: Product {3} | Описание: описание {3} | Цена: {3 * 100}')
        await message.answer_photo(img3)
    with open('Продукт_4.jpg', 'rb') as img4:
        await message.answer(f'Название: Product {4} | Описание: описание {4} | Цена: {4 * 100}')
        await message.answer_photo(img4, reply_markup=kb3)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer(f'Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(text=['Рассчитать'])
async def main_menu_2(message):
    await message.answer(f'Выберите опцию:', reply_markup=kb2)


def info():
    print(f'где А - это уровень активности человека, его различают обычно по '
          f'пяти степеням физических нагрузок в сутки:''\n'
          f'1. Минимальная активность: A = 1,2.' '\n'
          f'2. Слабая активность: A = 1,375.' '\n'
          f'3. Средняя активность: A = 1,55.' '\n'
          f'4. Высокая активность: A = 1,725.' '\n'
          f'5. Экстра-активность: A = 1,9 (под эту категорию обычно подпадают люди, занимающиеся, '
          f'например, тяжелой атлетикой, или другими силовыми видами спорта с ежедневными '
          f'тренировками, а также те, кто выполняет тяжелую физическую работу).')


@dp.callback_query_handler(text=['formulas'])
async def gender(call):
    await call.message.answer(f'Укажите ваш пол', reply_markup=kb4)
    await call.answer()


@dp.message_handler(text=['Мужской', 'Женский'])
async def get_formulas(message):
    if message.text == 'Мужской':
        await message.answer(f'(10 x вес (кг) + 6,25 х рост (см) - 5 х возраст (лет) + 5) x A', info())
    if message.text == 'Женский':
        await message.answer(f'(10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (лет) – 161) x A', info())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer(f'Введите свой возраст (полных лет):')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer(f'Введите свой рост (в см):')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer(f'Введите свой вес (в кг):')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # Минимальная активность: A = 1.2
    a = 1.375  # Слабая активность:
    # Средняя активность: A = 1.55
    # Высокая активность: A = 1.725
    # Экстра активность: A = 1.9
    calories = round(((10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5) * a), 1)
    await message.answer(f'Ваша суточная норма калорий: {calories}')
    await state.finish()


@dp.message_handler()
async def all_massages(message):
    await message.answer(f'Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
