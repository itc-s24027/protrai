#s24027
#標準入力で受け付けた金額を税込み(10%)価格としてプログラムを作成してください

print("金額を入力してください")
a = int(input())

print("税込み価格は", end="")
print(f"{a * 1.1}円です")
