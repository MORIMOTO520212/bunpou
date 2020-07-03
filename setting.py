def set(x):
    '''
    引数説明  
    0 - 初期  
    1 - 実験用
    例）historyPath, BunpouPath = setting.setting(0)
    '''
    if x == 0:
        # 学習データのリンク
        historyPath = "history.json"
        # 学習データ
        BunpouPath = "Bunpou.json"

        return historyPath, BunpouPath
    
    elif x == 1:
        # 学習データのリンク
        historyPath = "test/history.json"
        # 学習データ
        BunpouPath = "test/Bunpou.json"

        return historyPath, BunpouPath