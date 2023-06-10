import telebot
#to avoid sharing api key.. i created a separate python file which consists api key for my bot
from constants import API_KEY
import json

with open('python.json') as py_file:
    python_data = json.load(py_file)

with open('c.json') as c_file:
    c_data = json.load(c_file)

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

#creating a function to fetch python_data from json
def fetch(command):
    if command[0]=='p':
        return python_data[command]["explanation"] +"🧑‍💻 \n\n" + python_data[command]["syntax"]+"\n\n"+ python_data[command]["next"]
    elif command[0]=='c':
        return c_data[command]["explanation"] +"🧑‍💻 \n\n" + c_data[command]["syntax"]+"\n\n"+ "Next topic \n" + c_data[command]["next"]


#for start command
@bot.message_handler(commands=["start","hello"])
def start(message):
    hello(message)
    result = "Hey there... ✋\nNeed to learn new programming language...💻\n\ndont worry I'm here to help you...\nI am a virtual bot Created to help others...🤖\nplease Enter the following commands...\n\n/python - to start python  \n/c - to start c \n/cpp - to start c++ \n/java - to start java \n/HTML - to start HTMl\n\n/about"
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


@bot.message_handler(commands=["c"])
def c(message):
    result = '''Welcome to c language\n
    C is a general-purpose programming language that was developed in the early 1970s by Dennis Ritchie at Bell Labs. C is known for its efficiency, flexibility, and low-level programming capabilities, making it suitable for system-level programming and developing applications with high performance requirements.\n\n\n
    
we have devided c language into three parts :\n
    /c_part1\n
    /c_part2\n
    /c_part3\n
    '''
    send(message.chat.id,result)


@bot.message_handler(commands=["c_part1"])
def start(message):
    result = '''
    Part 1 contains\n\n
    /c_comments - to create comment lines\n
    /c_data_types - to know about datatypes\n
    /c_variables - How to create a variable\n
    /c_type_conversion - type conversion in c\n
    /c_operators - operators in c\n
    /c_booleans - what is a booleans\n
    '''
    send(message.chat.id,result)
@bot.message_handler(commands=["c_part2"])
def start(message):
    result = '''
    Part 2 contains\n\n
    /c_comments - to create comment lines\n
    /c_data_types - to know about datatypes\n
    /c_variables - How to create a variable\n
    /c_type_conversion - type conversion in c\n
    /c_operators - operators in c\n
    /c_booleans - what is a booleans\n
    '''
    send(message.chat.id,result)

# Handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    messageInput = message.text
    messageInput = messageInput[1::]
    try:
        try:
            if(messageInput[0]=='p'):
                bot.send_photo(message.chat.id, python_data[messageInput]['image'],caption=fetch(messageInput))
            if(messageInput[0]=='c'):
                bot.send_photo(message.chat.id, python_data[messageInput]['image'],caption=fetch(messageInput))
        except:
            bot.send_message(message.chat.id, fetch(messageInput))
    except:
        bot.send_message(message.chat.id, "invalid command")
    


#calling bot polling function
bot.polling()