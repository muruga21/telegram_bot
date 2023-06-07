import telebot
#to avoid sharing api key.. i created a separate python file which consists api key for my bot
from constants import API_KEY
import json

with open('python.json') as file:
    python_data = json.load(file)

#initializing bot with api key
bot = telebot.TeleBot(API_KEY,parse_mode=None)

#mapping send variable with bot.send_message method
send = bot.send_message

#defining some functions for emojis "just for fun"
def hello(message):
    bot.send_message(message.chat.id,"💻")
def cool(message):
    bot.send_message(message.chat.id,"💻")
def laugh(message):
    send(message.chat.id,"📱")
#kishore

#creating a function to fetch data from json
def fetch(command):
    return python_data[command]["explanation"] +"🧑‍💻 \n\n" + python_data[command]["syntax"]+"\n\n"+ python_data[command]["next"]



#for start command
@bot.message_handler(commands=["start","hello"])
def start(message):
    hello(message)
    result = " Hey there... ✋\n Need to learn new programming language...💻\n\n dont worry I'm here to help you...\n I am a virtual bot Created to help others...🤖\n please Enter the following commands...\n\n /python - to start python  \n /c - to start c \n /cpp - to start c++ \n /java - to start java \n /HTML - to start HTMl"
    send(message.chat.id,result)

@bot.message_handler(commands=["python"])
def python(message):
    bot.send_photo(message.chat.id,"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRh4zu2rGA8O90sKDRweHk7XogaXttx9-uEfQ&usqp=CAU")
    result = '''PYTHON!! \t yay...🍾\n
    /python_introduction - to know about python\n
    /python_hello_world - how print statement works...\n
    /python_comment_line - how to comment a line in python\n
    /python_variables - how to create and use variables\n
    /python_Numeric_types - Numeric types in python\n
    /python_Type_Casting -  To convert one data type to another data type\n
    /python_Strings - what is a string?\n
    /python_Booleans - what is a boolean\n
    /python_Operators - what is an operator\n
    '''
    send(message.chat.id,result)


# Handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    messageInput = message.text
    messageInput = messageInput[1::]
    bot.send_message(message.chat.id, fetch(messageInput))
    


#calling bot polling function
bot.polling()