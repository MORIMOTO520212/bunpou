bunpou = {
    'I never': 50, 
    'I never had': 20, 
    'never had': 3,
    'had a': 8, 
    'so I': 90
    }

def includeCheck(a, b):
    l = a.split()
    for w in l:
        if w in b:
            return w
    return False

i = 0
while i < len(bunpou):
    text1 = [key for key in bunpou[i].keys()][0]
    text2 = [key for key in bunpou[i+1].keys()][0]
    res = includeCheck(text1, text2)