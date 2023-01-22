import sys
import requests
url = sys.argv[1]
html = requests.get(url)
with open('downloaded_html.html', "wb") as file:
    file.write(html.content)