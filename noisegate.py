import json

try:
    with open('Bunpou.json', 'r') as f:
        _ = json.load(f)

    jsonData = {}
    jsonData = _
    list = []

    level = input('ノイズレベル >')
    for key in _:
        if jsonData[key] <= int(level):
            list.append(key)

    for key in list:
        del jsonData[key]

    with open('Bunpou.json', 'w') as f:
        json.dump(jsonData, f, indent=4)
except Exception as error:
    input(error)
