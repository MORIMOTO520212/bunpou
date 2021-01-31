import json

# levelとは読解の感度を表す値を表すもので、低く設定すると文法の感度が高まりますが、意味のない文法を解釈してしまう可能性が高くなります。
# 平均は50です。

with open('Bunpou.json', 'r') as f:
    data = json.load(f)

level    = ""
text     = ""
sentence = ""
sentenceSpace = [] # 文の一文字一文字を格納する配列
textLength = 0
w = 0
word = ""
bunpou = [] # センテンスに含まれる文法を抽出し格納する変数
choiceBunpou = []

def includeCheck(a, b):
    '''
    二つの文字列を比較して被っていない場合はFalseを返します。
    '''
    l = a.split()
    for w in l:
        if w in b:
            return w
    return False

def twist(word, count):
    '''
    文法とその頻出度をbunpouに格納します。
    '''
    global bunpou
    dt = {
        word: count
    }
    bunpou.append(dt)

def detector(l):
    global w, word

    cntW = word

    if l < textLength:
        word += ' {}'.format(text[l])

        if word in data and int(level) < data[word]:
            twist(word, data[word])
            detector(l+1)
        else:
            w += 1
    else:
        w += 1


if __name__=='__main__':
    print("+Bunpou Detector+\n")
    print("levelとは読解の感度を表す値を表すもので、低く設定すると文法の感度が高まりますが、意味のない文法を解釈してしまう可能性が高くなります。\n平均は10~60です。")
    level = input("level >")
    text = input("text here >")

    if level == "":
        print("levelを10に設定します。")
        level = 10

    sentence = text
    text = text.replace(".", "").replace("?", "")
    sentenceSpace = [" " for _ in text] # 文の一文字一文字を格納する配列
    text = text.split(" ")
    textLength = len(text)

    print("解析中\n")
    while w < textLength:
        word = text[w]
        detector(w+1)

    print(sentence)
    i = 0
    bunpouLength = len(bunpou)

    # 文法内の単語が被った場合、頻出度が多い方を選び、アンダーラインを設定する
    while i < bunpouLength-1:
        text1 = [key for key in bunpou[i].keys()][0]
        text2 = [key for key in bunpou[i+1].keys()][0]
        res = includeCheck(text1, text2)
        
        if res != False:
            count1 = bunpou[i][text1]
            count2 = bunpou[i+1][text2]
            # 頻出度の多い方を選ぶ
            if count1 < count2:
                #for _ in range(len(text1)-len(res)): print(" ", end="")
                #for _ in range(len(text2)): print("-", end="")
                h = 0
                while h < len(text2):
                    sentenceSpace[sentence.find(text2)+h] = "-"
                    h += 1
                choiceBunpou.append("2:"+text2)

                i += 1
            else:
                #for _ in range(len(text1)): print("-", end="")
                #for _ in range(len(text2)-len(res)): print(" ", end="")
                h = 0
                while h < len(text1):
                    sentenceSpace[sentence.find(text1)+h] = "-"
                    h += 1
                choiceBunpou.append("1:"+text1)

                i += 2
        else:
            #for _ in range(len(text1)): print("-", end="")
            #for _ in range(len(text2)-len(res)): print(" ", end="")
            while h < len(text1):
                sentenceSpace[sentence.find(text1)+h] = "-"
                h += 1
            choiceBunpou.append("0:"+text1)

            i += 1
    
    # アンダーラインを引く
    underline = ""
    for string in sentenceSpace:
        underline += string
    print(underline)

    for _ in bunpou:
        print(_)
    for bunpouS in choiceBunpou:
        print(bunpouS)
    input()