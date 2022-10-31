
from curses import resize_term
from gc import callbacks
import telebot
from config import TOKEN
from telebot import types
import random


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('first button', callback_data = 'first')
    item2 = types.InlineKeyboardButton('second button', callback_data = 'second')
    item3 = types.InlineKeyboardButton('thшrd button', callback_data = 'third')
    
    markup.add(item1, item2, item3)
    bot.reply_to(message, "How i can help you?",reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Как дела?')
    item3 = types.KeyboardButton('/start')
    item4 = types.KeyboardButton('/help')
    markup.add(item1,item2, item3, item4)

    img = open('static/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, img)
    bot.send_message(message.chat.id, "Добро пожаловать,\
        {0.first_name}!\nЯ {1.first_name},\nЯ тут просто исслудую территорию.\nbot_id - {1.id}\
        \nuser_id - {0.id}\nuser_name - {0.username}".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    name = message.from_user.first_name
    print(f'name - {name}')
    print(bot.get_me())
    getMeBot = bot.get_me()
    print(type(getMeBot))
    bot.send_message(message.chat.id, getMeBot)
    bot.send_message(message.chat.id, name)
  

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    x = random.getrandbits(10)
    if message.chat.type == 'private':
        if message.text == "Рандомное число":
            bot.send_message(message.chat.id, x)
        elif message.text == "Как дела?":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Good', callback_data = 'good')
            item2 = types.InlineKeyboardButton('Bad', callback_data = 'bad')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Норм, как сам?", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Моя твоя не понимай")
            #повторялка
            # bot.send_message(message.chat.id, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, "This is good.")
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'This is bad.')
            else:
                bot.send_message(call.message.chat.id, 'ЧЕЕЕЕЕ?')

            bot.answer_callback_query(call.id, show_alert=False, text="Тестовое Уведомление")
            bot.edit_message_text(chat_id=call.message.chat.id, \
                message_id = call.message.message_id, text='Как дела?', reply_markup=None)
            
    except Exception as ex:
        print(repr(ex))
        

bot.polling(none_stop=True)


