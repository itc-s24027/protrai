# s24027
#

import random
def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    return random.choice(kuji)

def main():
    kekka = omikuji()
    print("結果は",kekka,"です")

if __name__ == "__main__":
    main()
