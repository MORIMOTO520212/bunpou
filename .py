text = 'I never had a turtle before, so I asked my parents if I could keep it.'
sentence = text

text = text.replace(".", "").replace("?", "")
sentenceSpace = [" " for _ in text]
text = text.split(" ")


print(sentenceSpace)