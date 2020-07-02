import os, re, json, requests
# ------- Bunpou ------- #
# + このプログラムについて +
# Bunpouは洋書物から文法を学習し、データから英文を解釈、出力として意味の区切れごとにスラッシュを打つ文法解析プログラムです。
# 機械学習っぽい何かです。
# 独自の差分プログラムを使っています。
# 実行環境 Windows10
# update 2020/06/29

# 学習する書物がある対応しているサイト： 沢山食わせてあげて下さい。
# http://www.gutenberg.org/wiki/Main_Page
# 書物の文の場所はサイトから書物をクリックしてPlain Text UTF-8をクリック

# --- プログラム実行に必要なファイル一覧 --- #
# ファイル名   | 説明
# Bunpou.json | 文法を保存するファイルです。
# book.txt    | 書物の全文が書かれています。 bookには書物のタイトルが入ります。
# ファイルのフォーマットはUTF-8です。


# ~Note
# プログレスバー追加する
# 推定時間を測る
# ベクトルの高い文法を抽出して確かめる
# リンクから学習を実行できるようにする

# 学習データを取得する
with open("history.json", "r") as f:
    _history = json.load(f)
history_data = {}
history_data = _history

for key in history_data:
    if history_data[key]["status"] == False:
        break

history_data[key]["status"] = True

with open("history.json", "w") as f:
    json.dump(history_data, f, indent=4)

# テキストファイル読み込み
r = requests.get(history_data[key]["url"])
text = r.text

# テキストの記号や空白を削除する
text = text.replace("“", "")
text = text.replace("”", "")
text = text.replace("  ", " ")
text = text.replace("\n", "")
text = text.replace("? ","?")
text = text.replace(". ",".")
text = re.split("[.?]", text)

# テキスト全体のサイズ
text_length = len(text)
# L1
i = 0
# L2
j = 0
# 一文の列の変数初期化
w = 0
# データ一時保存
list = {}
# 重複防止
slash = []
_slash = []
# 連結関数に使用
word = ''

def json_save(word):
    '''
        jsonに文法を保存し、カウントします。

        wordの型は`配列`にして下さい。
    '''    
    global list, _slash

    # 配列を文字列に変換する
    w_s = str(word)
    grammar = w_s.replace("['", "").replace("', '", " ").replace("']", "")

    # 既にある場合
    try:
        list[grammar] = list[grammar]+1
    # 新たに追加する場合
    except:
        list[grammar] = 0
    
    if grammar not in _slash:
        _slash.append(grammar)


def renketu(j, text_line, text_line_length):
    '''
        連結関数

        引数名 | 型 | 説明

        `word` | str | 単語

        `j` | int | 行

        `text_line` | list | 単語で分割した配列

        `text_line_length` | int | 単語で分割した配列のサイズ
    '''    
    global w, word, slash

    # 次の行と比較する　最後の単語ではない場合 slash配列にwordが含まれていない場合　は処理する
    if word in text[j] and text_line[text_line_length-1] not in word and word not in slash:

        # combine
        w += 1
        word += " {}".format(text_line[w])
        
        renketu(j, text_line, text_line_length)
    else:
        # リスト化
        w_s = word.split(" ")
        
        w += 1

        # 最後の単語を削除
        w_s.pop()

        if 1 < len(w_s):
            # save
            json_save(w_s)


# L1 メインの行のループ
while i < text_length:
    os.system("cls")
    print("+ Bunpou +")
    print("text line : 現在プロセス/総プロセス数")
    print("text line : {}/{}".format(str(i), text_length-1))

    # 配列結合
    slash.extend(_slash)
    _slash.clear()

    # 5列以上空白のある行は飛ばす
    if "     " not in text[i]:

        # sentence row list
        text_line = text[i].split(" ")

        # 一文の単語のサイズ
        text_line_length = len(text_line)

        j = i+1
        
        # L2 比較する行をループ
        while j < text_length:

            # 一文の列をループ
            w = 0

            while w < text_line_length:

                # 単語抽出
                word = text_line[w]

                # 次の文に単語が含まれていたら次の単語と連結する
                renketu(j, text_line, text_line_length)

            j += 1

    i += 1

print("now writing...")
with open("Bunpou.json", "r") as f:
    bunpou_data = json.load(f)
listData = {}
listData = bunpou_data

for key in list:
    try:
        listData[key] = listData[key] + list[key]
    except:
        listData[key] = list[key]

with open("Bunpou.json", "w") as f:
    json.dump(listData, f, indent=4)

print("complete!")