#s24027
#グレースケール、90度回転、水平方向に反転、画像サイズ調整

import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    #画像を読みこんでモザイクに変換
    newImage = PIL.Image.open(path).convert("L").rotate(90).transpose(PIL.Image.FLIP_LEFT_RIGHT).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        lbl = tk.Label(text=fpath)
        lbl.pack()
        
root = tk.Tk()
root.geometry("400x500")


lbl = tk.Label(text= "画像表示アプリ バージョン2.0")
btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()

lbl.pack()
btn.pack()
imageLabel.pack()


tk.mainloop()
