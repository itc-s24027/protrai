import tkinter as tk #tkinterをインポートしてtkと略して使う

root = tk.Tk()
# 画面の大きさを決める
root.geometry("200x100")

# ラベルを作る
lbl = tk.Label(text="LABEL")
# ボタンを作る
btn = tk.Button(text="PUSH")

#画面にラベルを配置する
lbl.pack()
# 画面にボタンを配置する
btn.pack()
# 作ったウインドウを表示する
tk.mainloop()
