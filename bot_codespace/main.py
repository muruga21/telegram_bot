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
    result = "Hey there... ✋\nNeed to learn new programming language...💻\n\ndont worry I'm here to help you...\nI am a virtual bot Created to help others...🤖\nplease Enter the following commands...\n\n/python - to start python  \n/c - to start c\n\n /about"
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
    /c_part1 - To start part 1\n
    /c_part2 - To start part 2\n
    /c_part3 - To start part 3\n
    '''
    bot.send_photo(message.chat.id,'https://contentstatic.techgig.com/photo/90325682.cms',caption=result)


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
    bot.send_photo(message.chat.id,'https://images.app.goo.gl/VX5uxtezZXmT8WBr6',caption=result)
@bot.message_handler(commands=["c_part2"])
def start(message):
    result = '''
    Part 2 contains\n\n
    /c_conditions - to know about conditional statements\n
    /c_conditions_short_hand - what is conditions short hand\n
    /c_switch - to know about switch statement\n
    /c_while_loop - what is while loop\n
    /c_for_loop - how to use for loop\n
    /c_arrays - how to store datas in array\n
    /c_arrays_multi - to know about multi dimension array\n
    /c_strings - what is a string\n
    /c_strings_functions - inbuilt string function\n
    '''
    bot.send_photo(message.chat.id,'https://media.licdn.com/dms/image/C4E12AQE4VA_ZhZLp8g/article-cover_image-shrink_720_1280/0/1582135557552?e=2147483647&v=beta&t=YCMm683mzuJIiHVksVRTjmZSi7xT4ziNJEVrOfGQG3U',caption=result)

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
                bot.send_photo(message.chat.id, c_data[messageInput]['image'],caption=fetch(messageInput))
        except:
            bot.send_message(message.chat.id, fetch(messageInput))
    except:
        bot.send_message(message.chat.id, "invalid command")



#calling bot polling function
bot.polling()