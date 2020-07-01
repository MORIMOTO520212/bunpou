import json

def main(title, url):
    with open("history.json", "r") as f:
        _history = json.load(f)
    history_data = {}
    history_data = _history

    if title not in history_data:
        history_data[title] = {
            "status": False,
            "url": url
        }
    else:
        print("既に存在します。")
    
    with open("history.json", "w") as f:
        json.dump(history_data, f, indent=4)

if __name__=="__main__":
    print("q - 終了")
    while True:
        title = input("Title >")
        if title == "q":
            exit()
        url   = input("url >")
        if url == "q":
            exit()
        main(title, url)