import sqlite3 as sq
from create_bot import bot
from keyboards.client_keyboards import delete_keyboard


def sql_start():
    global base, cur
    base = sq.connect(r'databases/users.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS '
                 'users(datetime TEXT, username TEXT, city TEXT, district TEXT, neighborhood TEXT,'
                 ' rooms TEXT, floor TEXT, heating TEXT, price INTEGER)')
    base.commit()


async def sql_add_users_flat(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_send_users_flats(message):
    """отправляет пользователю список квартир из БД
    !!!! обрати внимание, что при исправлениях здесь
    нужно исправить метод sql_delete_users_flats"""
    for flat in cur.execute('SELECT datetime, city, district, neighborhood, rooms,'
                            ' floor, heating, price FROM users WHERE username == ?',
                            (message.from_user.username,)).fetchall():
        await bot.send_message(message.from_user.id, f"*Ваша конфигурация поиска*\n*Время запроса:* {flat[0]}\n"
                                                     f"*Город:* {flat[1]}\n*Район:* {flat[2]}\n*Количество комнат:* {flat[4]}\n"
                                                     f"*Этаж:* {flat[5]}\n*Цена:* {flat[7]}", parse_mode='Markdown',
                               reply_markup=delete_keyboard)


async def sql_delete_users_flats(callback):
    """удаляет квартиру из БД по времени и юзернейму
    !!!! обрати внимание, что время вырезается из сообщения, поэтому при
    изменении формата сообщения, нужно будет исправить split в этом методе"""
    cur.execute('DELETE FROM users WHERE datetime == ? AND username == ?',
                (callback.message.text.split('\n')[1][-19:], callback.from_user.username))
    base.commit()


def sql_count_users_flats(username) -> int:
    """ считает, сколько запросов на поиск выполнял пользователь """
    lst_of_rows = cur.execute('SELECT username FROM users WHERE username == ?', (username,)).fetchall()
    base.commit()
    length = len(lst_of_rows)
    return length
