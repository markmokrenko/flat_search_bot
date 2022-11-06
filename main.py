from aiogram.utils import executor
from create_bot import dp
from handlers import client_handlers, survey
from databases import users_db


async def on_startup(_):
    print("Бот онлайн")
    # создание базы данных при запуске бота
    users_db.sql_start()


if __name__ == '__main__':
    # регистрация хендлеров из файлов
    client_handlers.register_handlers_client(dp)
    survey.register_handlers_survey(dp)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
