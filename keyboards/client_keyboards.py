from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

'''Main menu keyboard'''
b1 = KeyboardButton('Выбрать параметры')
b2 = KeyboardButton('Мои квартиры')
b3 = KeyboardButton('Помощь')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(b1).add(b2).add(b3)

'''City keyboard'''
city_keyboard_buttons = [InlineKeyboardButton(text='Стамбул', callback_data='Стамбул'),
                         InlineKeyboardButton(text='Отменить', callback_data='Отменить')]
city_keyboard = InlineKeyboardMarkup(row_width=1)
city_keyboard.add(*city_keyboard_buttons)

'''District keyboard'''
districts_keyboard_buttons = [InlineKeyboardButton(text='Adalar', callback_data='Adalar'),
                              InlineKeyboardButton(text='Arnavutköy', callback_data='Arnavutköy'),
                              InlineKeyboardButton(text='Ataşehir', callback_data='Ataşehir'),
                              InlineKeyboardButton(text='Avcılar', callback_data='Avcılar'),
                              InlineKeyboardButton(text='Bağcılar', callback_data='Bağcılar'),
                              InlineKeyboardButton(text='Bahçelievler', callback_data='Bahçelievler'),
                              InlineKeyboardButton(text='Bakırköy', callback_data='Bakırköy'),
                              InlineKeyboardButton(text='Başakşehir', callback_data='Başakşehir'),
                              InlineKeyboardButton(text='Bayrampaşa', callback_data='Bayrampaşa'),
                              InlineKeyboardButton(text='Beşiktaş', callback_data='Beşiktaş'),
                              InlineKeyboardButton(text='Beykoz', callback_data='Beykoz'),
                              InlineKeyboardButton(text='Beylikdüzü', callback_data='Beylikdüzü'),
                              InlineKeyboardButton(text='Beyoğlu', callback_data='Beyoğlu'),
                              InlineKeyboardButton(text='Büyükçekmece', callback_data='Büyükçekmece'),
                              InlineKeyboardButton(text='Çatalca', callback_data='Çatalca'),
                              InlineKeyboardButton(text='Çekmeköy', callback_data='Çekmeköy'),
                              InlineKeyboardButton(text='Esenler', callback_data='Esenler'),
                              InlineKeyboardButton(text='Esenyurt', callback_data='Esenyurt'),
                              InlineKeyboardButton(text='Eyüpsultan', callback_data='Eyüpsultan'),
                              InlineKeyboardButton(text='Fatih', callback_data='Fatih'),
                              InlineKeyboardButton(text='Gaziosmanpaşa', callback_data='Gaziosmanpaşa'),
                              InlineKeyboardButton(text='Güngören', callback_data='Güngören'),
                              InlineKeyboardButton(text='Kadıköy', callback_data='Kadıköy'),
                              InlineKeyboardButton(text='Kağıthane', callback_data='Kağıthane'),
                              InlineKeyboardButton(text='Kartal', callback_data='Kartal'),
                              InlineKeyboardButton(text='Küçükçekmece', callback_data='Küçükçekmece'),
                              InlineKeyboardButton(text='Maltepe', callback_data='Maltepe'),
                              InlineKeyboardButton(text='Pendik', callback_data='Pendik'),
                              InlineKeyboardButton(text='Sancaktepe', callback_data='Sancaktepe'),
                              InlineKeyboardButton(text='Sarıyer', callback_data='Sarıyer'),
                              InlineKeyboardButton(text='Şile', callback_data='Şile'),
                              InlineKeyboardButton(text='Silivri', callback_data='Silivri'),
                              InlineKeyboardButton(text='Şişli', callback_data='Şişli'),
                              InlineKeyboardButton(text='Sultanbeyli', callback_data='Sultanbeyli'),
                              InlineKeyboardButton(text='Sultangazi', callback_data='Sultangazi'),
                              InlineKeyboardButton(text='Tuzla', callback_data='Tuzla'),
                              InlineKeyboardButton(text='Ümraniye', callback_data='Ümraniye'),
                              InlineKeyboardButton(text='Üsküdar', callback_data='Üsküdar'),
                              InlineKeyboardButton(text='Zeytinburnu', callback_data='Zeytinburnu'),
                              InlineKeyboardButton(text='Отменить', callback_data='Отменить')]
district_keyboard = InlineKeyboardMarkup(row_width=3)
district_keyboard.add(*districts_keyboard_buttons)

'''Neighbourhood keyboard'''
# inline_games_buttons = [InlineKeyboardButton(text='Игра1', callback_data='show_game1'),
#                         InlineKeyboardButton(text='Игра2', callback_data='show_game2'),
#                         InlineKeyboardButton(text='Игра3', callback_data='show_game3'),
#                         InlineKeyboardButton(text='Игра4', callback_data='show_game4')]
# games_menu = InlineKeyboardMarkup(row_width=1)
# games_menu.add(*inline_games_buttons)

'''Rooms keyboard'''
rooms_keyboard_buttons = [InlineKeyboardButton(text='Студия (1+0)', callback_data='Студия'),
                          InlineKeyboardButton(text='Однокомнатная (1+1, 1.5+1)',
                                               callback_data='Однокомнатная'),
                          InlineKeyboardButton(text='Двухкомнататная (2+0, 2+1, 2.5+1)',
                                               callback_data='Двухкомнататная'),
                          InlineKeyboardButton(text='Трехкомнатная (2+2, 3+0, 3+1)',
                                               callback_data='Трехкомнатная'),
                          InlineKeyboardButton(text='Многокомнатная (остальные варианты)',
                                               callback_data='Многокомнатная'),
                          InlineKeyboardButton(text='Неважно', callback_data='Неважно'),
                          InlineKeyboardButton(text='Отменить', callback_data='Отменить')]
rooms_keyboard = InlineKeyboardMarkup(row_width=1)
rooms_keyboard.add(*rooms_keyboard_buttons)

'''Floor keyboard'''
floor_keyboard_buttons = [InlineKeyboardButton(text='Не нижний', callback_data='Не нижний'),
                          InlineKeyboardButton(text='Неважно', callback_data='Неважно'),
                          InlineKeyboardButton(text='Отменить', callback_data='Отменить')]
floor_keyboard = InlineKeyboardMarkup(row_width=1)
floor_keyboard.add(*floor_keyboard_buttons)

'''Heating keyboard'''
heating_keyboard_buttons = [InlineKeyboardButton(text='Не нижний', callback_data='Не нижний'),
                            InlineKeyboardButton(text='Неважно', callback_data='Неважно'),
                            InlineKeyboardButton(text='Отменить', callback_data='Отменить')]
heating_keyboard = InlineKeyboardMarkup(row_width=1)
heating_keyboard.add(*heating_keyboard_buttons)

'''Delete keyboard'''
delete_keyboard_button = InlineKeyboardButton(text='Удалить', callback_data='Удалить')
delete_keyboard = InlineKeyboardMarkup()
delete_keyboard.add(delete_keyboard_button)

