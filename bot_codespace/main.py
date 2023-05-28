import telebot
from constants import API_KEY

bot = telebot.TeleBot(API_KEY,parse_mode=None)

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg,"Hi da cibi")

@bot.message_handler(commands=["cibi"])
def start(msg):
    bot.reply_to(msg,"cibi = motta")


bot.polling()