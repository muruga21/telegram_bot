import telebot
#to avoid sharing api key.. i created a separate python file which consists api key for my bot
from constants import API_KEY
import json

with open('python.json') as file:
    data = json.load(file)

#initializing bot with api key
bot = telebot.TeleBot(API_KEY,parse_mode=None)

#mapping send variable with bot.send_message method
send = bot.send_message

#defining some functions for emojis "just for fun"
def hello(message):
    bot.send_message(message.chat.id,"✋")
def cool(message):
    bot.send_message(message.chat.id,"💻")
def laugh(message):
    send(message.chat.id,"📱")


#creating a list of topics in 


#for start command
@bot.message_handler(commands=["start","hello"])
def start(message):
    hello(message)
    result = " Hey there... ✋\n Need to learn new programming language...💻\n\n dont worry I'm here to help you...\n I am a virtual bot Created to help others...🤖\n please Enter the following commands...\n\n /python - to start python  \n /c - to start c \n /cpp - to start c++ \n /java - to start java \n /HTML - to start HTMl"
    send(message.chat.id,result)

#for muruga command "just for testing purpose"
@bot.message_handler(commands=["muruga"])
def muruga(message):
    bot.send_photo(message.chat.id,"https://miro.medium.com/v2/resize:fit:439/1*ZYyXvhYDGvELzYoXYpPLMg.png")

#for python command
@bot.message_handler(commands=["python"])
def python(message):
    cool(message)
    result = '''PYTHON!! \t yay...🍾\n
    /python_hello_world - how print statement works...\n
    /python_comment_line - how to comment a line in python\n
    /python_variables - how to create and use variables\n
    '''
    send(message.chat.id,result)

#for python_hello_world command
@bot.message_handler(commands=["python_hello_world"])
def python_hello_world(message):
    result=data["python_hello_world"]["explanation"] +"🧑‍💻 \n\n" + data["python_hello_world"]["syntax"]
    send(message.chat.id,result)

#for pythoncomment_line command    
@bot.message_handler(commands=["python_comment_line"])
def python_comment_line(message):
    laugh(message)
    result=data["python_comment_line"]["explanation"] +"🧑‍💻 \n\n" + data["python_comment_line"]["syntax"]
    send(message.chat.id,result)
#for pythoncomment_line command    
@bot.message_handler(commands=["python_variables"])
def python_comment_line(message):
    result=data["python_variables"]["explanation"] +"🧑‍💻 \n\n" + data["python_variables"]["syntax"]
    send(message.chat.id,result)        

#calling bot polling function
bot.polling()