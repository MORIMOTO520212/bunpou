import json

# levelとは読解の感度を表す値を表すもので、低く設定すると文法の感度が高まりますが、無駄な文法を解釈してしまう可能性が高くなります。
# 平均は50です。

with open('Bunpou.json', 'r') as f:
    data = json.load(f)

#level = input("level >")
#text = input("text here >")
level = 10
text = 'I never had a turtle before, so I asked my parents if I could keep it.'
sentence = text

text = text.replace(".", "").replace("?", "")
text = text.split(" ")

textLength = len(text)

w = 0
word = ""
bunpou = []

def includeCheck(a, b):
    l = a.split()
    for w in l:
        if w in b:
            return w
    return False

def twist(word, count):
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
    while w < textLength:
        word = text[w]
        detector(w+1)

    print(sentence)
    i = 0
    bunpouLength = len(bunpou)
    while i < bunpouLength-1:
        text1 = [key for key in bunpou[i].keys()][0]
        text2 = [key for key in bunpou[i+1].keys()][0]
        res = includeCheck(text1, text2)

        # 文法内の単語が被った場合
        if res != False:
            count1 = bunpou[i][text1]
            count2 = bunpou[i+1][text2]
            if count1 < count2:
                for _ in range(len(text1)-len(res)): print(" ", end="")
                for _ in range(len(text2)): print("-", end="")
                i += 2
            else:
                for _ in range(len(text1)): print("-", end="")
                for _ in range(len(text2)-len(res)): print(" ", end="")
                i += 1
        else:
            for _ in range(len(text1)): print("-", end="")
            for _ in range(len(text2)-len(res)): print(" ", end="")
            i += 1