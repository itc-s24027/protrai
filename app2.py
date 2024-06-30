import tkinter as tk #tkinterをインポートしてtkと略して使う


def dispLabel():
    lbl.config(text="こんにちは")
    
root = tk.Tk()
# 画面の大きさを決める
root.geometry("400x200")

# ラベルを作る
lbl = tk.Label(text="LABEL", font=("Helvetica", 20))
# ボタンを作る
btn = tk.Button(text="PUSH", command=dispLabel, font=("Helvetica", 20))

#画面にラベルを配置する
lbl.pack()
# 画面にボタンを配置する
btn.pack()

lbl2 = tk.Label(text="ラベル２", font=("Helvetica", 20)).pack()

btn2 = tk.Button(text="何もしないボタン", command=dispLabel, font=("Helvetica", 20)).pack()

# 作ったウインドウを表示する
tk.mainloop()


