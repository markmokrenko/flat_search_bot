from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_keyboards import city_keyboard, district_keyboard, rooms_keyboard, floor_keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import datetime
from databases.users_db import sql_add_users_flat


class FSMAdmin(StatesGroup):
    city = State()
    district = State()
    # neighborhood = State()
    rooms = State()
    floor = State()
    # heating = State()
    price = State()


async def cm_start(message: types.Message):
    await FSMAdmin.city.set()
    await message.answer('Выбери город:', reply_markup=city_keyboard)
    # await message.delete()


async def canceling(callback: types.CallbackQuery,
                    state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await callback.message.answer('ОК')
    await callback.answer()


async def city_choose(callback: types.CallbackQuery,
                      state: FSMContext):
    async with state.proxy() as data:
        data['datetime'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        data['name'] = callback.from_user.username
        data['city'] = callback.data
    await callback.message.delete()
    await FSMAdmin.next()
    await callback.message.answer('Выбери район:', reply_markup=district_keyboard)


async def district_choose(callback: types.CallbackQuery,
                          state: FSMContext):
    async with state.proxy() as data:
        data['district'] = callback.data
        data['neigborhood'] = None  # заполнитель для таблицы, пока не написана функция
    await callback.message.delete()
    await FSMAdmin.next()
    await callback.message.answer('Выбери количество комнат:', reply_markup=rooms_keyboard)


async def rooms_choose(callback: types.CallbackQuery,
                       state: FSMContext):
    async with state.proxy() as data:
        data['rooms'] = callback.data
    await callback.message.delete()
    await FSMAdmin.next()
    await callback.message.answer('Выбери этаж:', reply_markup=floor_keyboard)


async def floor_choose(callback: types.CallbackQuery,
                       state: FSMContext):
    async with state.proxy() as data:
        data['floor'] = callback.data
        data['heating'] = None  # заполнитель для таблицы, пока не написана функция
    await callback.message.delete()
    await FSMAdmin.next()
    await callback.message.answer('Введите максимальную цену:')


# async def heating_choose(callback: types.CallbackQuery,
#                           state: FSMContext):
#     async with state.proxy() as data:
#         data['heating'] = callback.data
#     await callback.message.delete()
#     await FSMAdmin.next()
#     await callback.message.answer('Введи макcимальную цену:')

async def max_price_choose(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        try:
            data['price'] = int(message.text)
        except Exception:
            await message.reply('Введите число')
    await message.answer(
        f"*Выбранные параметры*\n*Город:* {data['city']}\n*Район:* {data['district']}"
        f"\n*Количество комнат:* {data['rooms']}\n*Этаж:* {data['floor']}\n*Максимальная цена:* {data['price']}",
        parse_mode='Markdown'
    )
    await message.delete()
    try:
        await sql_add_users_flat(state)
        await message.answer('Выбор сохранен')
    except Exception:
        await message.answer('Произошла ошибка, изменения не сохранены')
    await state.finish()


def register_handlers_survey(dp: Dispatcher):
    dp.register_message_handler(cm_start, text='Выбрать параметры', state=None)
    dp.register_callback_query_handler(canceling, text='Отменить', state='*')
    dp.register_callback_query_handler(city_choose, state=FSMAdmin.city)
    dp.register_callback_query_handler(district_choose, state=FSMAdmin.district)
    # dp.register_callback_query_handler(neighbohood_choose, state=FSMAdmin.neighbourhood)
    dp.register_callback_query_handler(rooms_choose, state=FSMAdmin.rooms)
    dp.register_callback_query_handler(floor_choose, state=FSMAdmin.floor)
    # dp.register_callback_query_handler(heating_choose, state=FSMAdmin.rooms)
    dp.register_message_handler(max_price_choose, state=FSMAdmin.price)
