from telebot import types
btn_new = types.KeyboardButton('Кнопка1')
btn_new1 = types.KeyboardButton('Кнопка')
main_markup = types.ReplyKeyboardMarkup(True)
main_markup.add(btn_new)
main_markup.add(btn_new1)

