# GUIで動くアプリを作ってみるよ

import tkinter as tk #まずこの行を書く必要があるよ

root = tk.Tk() #初めのおまじない

root.geometry("400x400") #ウインドウのサイズを決める
root.title("ハローアプリ") #ウインドウのタイトルを決める
lbl = tk.Label(text="こんにちは世界") #いつもの
a = tk.Label(text="初めてのGUIアプリ")
lbl.pack() #lblを設置させる必要があるよ
a.pack()



root.mainloop() #終わりのおまじない
