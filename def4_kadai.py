# s24027
# メインの処理をmain()関数に行わせるおみくじプログラム

import random

# ランダムでkujiの中を返す関数
def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

# エントリーポイントの定義
def main():
    kekka = omikuji()
    print("結果は",kekka,"です")

if __name__ == "__main__":
    main()
