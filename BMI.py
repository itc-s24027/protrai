# s24027
#BMI値計算プログラム

h = float(input("身長何cmですか？")) / 100.0
w = float(input("体重は何kgですか？"))

bmi = w/(h * h)
print("あなたのBMI値は、",bmi,"です。")
