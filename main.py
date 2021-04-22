from telebot import types
import telebot
import cfg
bot = telebot.TeleBot(cfg.token)

def Main():
    main_markup = types.ReplyKeyboardMarkup(True)
    main_markup.add(cfg.btn_new)
    main_markup.add(cfg.btn_new1)
    return main_markup


@bot.message_handler(commands=['start'])
def echo(message):
    bot.send_message(message.from_user.id, cfg.start_msg, reply_markup=Main())
bot.polling(none_stop=True, interval=12)
