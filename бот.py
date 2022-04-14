import telebot
from telebot import types
token = "5132971449:AAGiLXfJiUuyzSqJ6_18BC715tk-gHpk32Q"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    bot.send_message(message.chat.id, 'Приветствую! Я - твой личный помощник. Чтобы узнать о моих возможностях пропиши команду /help', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, "Чтобы перейти в нашу группу вк напишите команду  /вк "
                                      "\nЧтобы узнать текущий состав сборной, напишите команду /cостав "
                                      "\nЧтобы узнать актуадбные результаты сезона, напишите /сезон")
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "/вк":
        bot.send_message(message.chat.id, 'Наш вк: https://vk.com/volleymtuci')
    if message.text.lower() == "/состав":
        bot.send_message(message.chat.id, 'Текущий состав: https://mrsss.nagradion.ru/tournament27407/team/231870/players')
    if message.text.lower() == "/сезон":
        bot.send_message(message.chat.id, 'Актуальные результаты сезона: https://mrsss.nagradion.ru/tournament27407')
bot.polling()