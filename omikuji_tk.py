# s24027
# GUIで動くおみくじ

import tkinter as tk

import random
root = tk.Tk()
root.geometry("400x400")
root.title("おみくじ")
kuji = ["大吉","中吉","小吉","凶","大凶"]
lbl = tk.Label(text=random.choice(kuji))
lbl.pack()

root.mainloop()
               

