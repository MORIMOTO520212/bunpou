import json

try:
    with open('Bunpou.json', 'r') as f:
        _ = json.load(f)

    jsonData = {}
    jsonData = _
    list = []

    level = input('レベル >')
    for key in _:
        if jsonData[key] <= int(level):
            list.append(key)
        elif " " == key:
            list.append(key)
        elif "\r" in key:
            list.append(key)
        elif "\"" in key:
            list.append(key)
        elif "\\x80\x9d" in key:
            list.append(key)

    for key in list:
        del jsonData[key]

    with open('Bunpou.json', 'w') as f:
        json.dump(jsonData, f, indent=4)

    print("削除した文法の数:",len(list))
    input("\nなにかキーを押して終了する")
except Exception as error:
    print(error)
    input("\nなにかキーを押して終了する")
