from bs4 import BeautifulSoup
import requests, json, re, setting

historyPath, BunpouPath = setting.set(0)

with open(historyPath, 'r') as f:
    data = json.load(f)

i = len(data)
while True:
    html = requests.get('http://www.gutenberg.org/ebooks/{}'.format(i))
    soup = BeautifulSoup(html.text, 'html.parser')
    title = soup.select('#content > div.header > h1')
    title = title[0]
    title = re.split('[<>]', str(title))
    print(i, title[2])

    url = 'http://www.gutenberg.org/ebooks/{}.txt.utf-8'.format(str(i))

    with open(historyPath, 'r') as f:
        _d = json.load(f)
    jsonData = {}
    jsonData = _d
    if title[2] not in jsonData:
        jsonData[title[2]] = {
            "status": False,
            "url": url
        }
        with open(historyPath, 'w') as f:
            json.dump(jsonData, f, indent=4)

    i += 1