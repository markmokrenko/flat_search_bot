from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.client_keyboards import main_menu
from handlers import survey
from databases.users_db import sql_send_users_flats, sql_delete_users_flats, sql_count_users_flats


async def command_start_reply(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}!\n'
                         f'Этот бот позволяет искать квартиры блаблабла', reply_markup=main_menu)
    await message.delete()

async def start_survey(message : types.Message):
    if sql_count_users_flats(message.from_user.username) < 3:
    # print(type(sql_count_users_flats(message.from_user.username)))
        await survey.cm_start(message)
    else:
        await message.answer('У вас больше 3 запросов, удалите один или несколько')


async def show_me_requests(message : types.Message):
    await sql_send_users_flats(message)

async def delete_my_request(callback : types.CallbackQuery):
    '''Удаляет сообщение с параметрами квартиры и квартиру из базы данных'''
    await callback.message.delete()
    await sql_delete_users_flats(callback)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start_reply, commands=['start', 'help'])
    dp.register_message_handler(start_survey, text='Выбрать параметры')
    dp.register_message_handler(show_me_requests, text='Мои квартиры')
    dp.register_callback_query_handler(delete_my_request, text='Удалить', )

