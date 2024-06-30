# s24027
#おみくじプログラム

import tkinter as tk
import random

def dispLabel():
    kuji = ["大吉","中吉","小吉","凶","大凶","半吉","末吉","大大吉"]
    lbl.configure(text=random.choice(kuji))

root = tk.Tk()
root.geometry("400x200")

lbla = tk.Label(text="おみくじルーレット")
lbl = tk.Label(text="おみくじを表示")
btn = tk.Button(text="PUSH", command=dispLabel)

lbla.pack()
lbl.pack()
btn.pack()

root.mainloop()
