import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]
html = requests.get(url, verify = False)

with open('downloaded_html.html', "wb") as file:
    file.write(html.content)

def get_all_text():
    soup = BeautifulSoup(html.content, 'html.parser')
    text_tags = soup.find_all(['p', 'h'])
    texts = []
    for tag in text_tags:
        print(tag.text.lower())
        texts.append(tag.text.lower())
    letters = 'qwertyuiopasdfghjklzxcvbnm .,-'
    finished_text = ''
    for text in texts:
        for char in text:
            if char in letters:
                finished_text += char
    with open('downloaded_text.txt', "w") as file:
        file.writelines(finished_text)

get_all_text()