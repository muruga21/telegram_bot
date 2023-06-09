import json
import requests
from bs4 import BeautifulSoup
import re

datas = []


links = [
    "https://www.w3schools.com/c/c_comments.php",
    "https://www.w3schools.com/c/c_variables.php",
    "https://www.w3schools.com/c/c_data_types.php",
    "https://www.w3schools.com/c/c_type_conversion.php",
    "https://www.w3schools.com/c/c_constants.php",
    "https://www.w3schools.com/c/c_operators.php",
    "https://www.w3schools.com/c/c_booleans.php",
    "https://www.w3schools.com/c/c_conditions.php",
    "https://www.w3schools.com/c/c_conditions_short_hand.php",
    "https://www.w3schools.com/c/c_switch.php",
    "https://www.w3schools.com/c/c_while_loop.php",
    "https://www.w3schools.com/c/c_for_loop.php",
    "https://www.w3schools.com/c/c_break_continue.php",
    "https://www.w3schools.com/c/c_arrays.php",
    "https://www.w3schools.com/c/c_arrays_multi.php",
    "https://www.w3schools.com/c/c_strings.php",
    "https://www.w3schools.com/c/c_strings_esc.php",
    "https://www.w3schools.com/c/c_strings_functions.php",
    "https://www.w3schools.com/c/c_user_input.php",
    "https://www.w3schools.com/c/c_memory_address.php",
    "https://www.w3schools.com/c/c_pointers.php",
    "https://www.w3schools.com/c/c_pointers_arrays.php",
    "https://www.w3schools.com/c/c_functions.php",
    "https://www.w3schools.com/c/c_functions_parameters.php",
    "https://www.w3schools.com/c/c_functions_decl.php",
    "https://www.w3schools.com/c/c_functions_recursion.php",
    "https://www.w3schools.com/c/c_math.php",
    "https://www.w3schools.com/c/c_structs.php",
    "https://www.w3schools.com/c/c_files.php",
    "https://www.w3schools.com/c/c_files_write.php",
    "https://www.w3schools.com/c/c_files_read.php",
]



def findtitles(links):
    titles = []
    pattern = "c_[a-z_]*"
    for link in links:
        title = re.findall(pattern,link)
        titles.append(title)
    return titles
titles = findtitles(links)

print (titles)


def findexplanation(links):
    explanation = []
    for url in links:
        response = requests.get(url)
        html_content = response.content

        soup = BeautifulSoup(html_content, features='html.parser')
        result = soup.find_all('p')
        lines = 0
        contentExplanation = ""
        for res in result:
            lines += 1
            contentExplanation += res.text
            if(lines==3):
                break
        explanation.append([contentExplanation])
    return explanation

explanations = findexplanation(links)


def findsyntax(links):
    syntax_all = []
    for url in links:
        response = requests.get(url)
        html_content = response.content
        soup = BeautifulSoup(html_content,features='html.parser')
        result = soup.find_all(class_='w3-code notranslate javaHigh')
        lines=0
        syntax = ''
        for res in result:
            lines+=1
            syntax += res.text
            if(lines==3):
                break
        syntax_all.append([syntax])
    return syntax_all

syntaxs = findsyntax(links)

print(syntaxs)

print(explanations)

numberofdatas = len(explanations)

def createcontent(numberofdatas,explanations):
    for i in range(0,numberofdatas):
        data = {
            "title":titles[i][0],
            "image":" ",
            "explanation":explanations[i][0],
            "syntax": syntaxs[i][0],
            "next":" "
        }
        
        datas.append(data)

createcontent(numberofdatas,explanations)

print(datas)

file_path = "D:/telebot/telegram_bot/bot_codespace/c.json"

with open(file_path, 'w') as json_file:
    json_data = json.dumps(datas)
    json_file.write(json_data)

json_file.close()

print("done")
