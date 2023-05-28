import telebot
from constants import API_KEY

bot = telebot.TeleBot(API_KEY,parse_mode=None)

def hello(message):
    bot.send_message(message.chat.id,"✋")


@bot.message_handler(commands=["start","hello"])
def start(message):
    hello(message)
    result = " Hey there... ✋\n Need to learn new programming language...💻\n\n dont worry I'm here to help you...\n I am a virtual bot Created to help others...🤖\n please Enter the following commands...\n\n /python - to start python  \n /c - to start c \n /c++ - to start c++ \n /java - to start java \n /HTML - to start HTMl"
    bot.send_message(message.chat.id,result)

@bot.message_handler(commands=["muruga"])
def muruga(message):
    bot.send_photo(message.chat.id,"https://miro.medium.com/v2/resize:fit:439/1*ZYyXvhYDGvELzYoXYpPLMg.png")

@bot.message_handler(commands=["python"])
bot.polling()