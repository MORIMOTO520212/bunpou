import json

# 頻出度の文法を降順で調べる

json_data = {}

with open("Bunpou.json", "r", encoding="utf-8") as f:
    _d = json.load(f)

json_data = _d

for _ in range(100):
    max = 0
    max_key = ''
    for key in json_data:
        if max < json_data[key]:
            max = json_data[key]
            max_key = key

    print(max_key+": "+str(json_data[max_key]))

    del json_data[max_key]

input()