#s24027
#エントリーウイジェットで受け付けた金額を税込み(10%)価格としてプログラムを作成してください
#コードをアレンジして各自作成してください

import tkinter as tk #tkinterをtkと略して使用する

def dispLabel():  #エントリーメソッドを使用して入力を受け付け変数aに格納
    print("金額を入力してください")
    a = int(entry.get())
    print(f"aは{type(a)}") #ログの出力
    lbl.config(text=f"税込み価格は{int(a * 1.1)}円です")
    

root = tk.Tk()
root.title("エントリーウイジェット")
root.geometry("400x200")

lbl = tk.Label(text="ラベル", font=("Helvetica", 20))
entry = tk.Entry(font=("Helvetica", 20))
btn = tk.Button(text="ボタン", font=("Helvetica", 20), command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()
