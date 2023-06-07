import json
import requests
from bs4 import BeautifulSoup
import re

data = []


links = ["https://www.w3schools.com/python/python_strings.asp","https://www.w3schools.com/python/python_strings_slicing.asp"]
file_path = "D:/temp/data.json"


def findtitles(links):
    titles = []
    pattern = "python_[a-z_]*"
    for link in links:
        title = re.findall(pattern,link)
        titles.append(title)
    return titles
titles = findtitles(links)

print (titles)


for url in links:
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, features='html.parser')
    result = soup.find_all('p')
    lines = 0
    explanation = ""
    for res in result:
        lines += 1
        print(res.text)
        explanation += res.text
        if(lines==3):
            break
    
print(data)


# file_path = "D:/temp/data.json"

# with open(file_path, 'w') as json_file:
#     json_data = json.dumps(data)
#     json_file.write(json_data)

# json_file.close()

print("done")

