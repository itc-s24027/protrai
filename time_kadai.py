#s24027
#コメントで重要な行の説明を追記

import datetime #日付や時刻を表示できるモジュール
import tkinter as tk # GUIでアプリを作ることができるモジュール

#時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    
    lbl.config(text=current_time)
    root.after(1000,update_time) #指定した関数を一定時間経過後に実行する
    
#Tkinterのウインドウを作成
root = tk.Tk() #初めのおまじない
root.title("現在の時刻")

#ラベルを設定
lbl = tk.Label() 
lbl.config(text="", font=("Helvetica",20)) #フォント、文字サイズの設定
lbl.pack()

#関数の呼び出し
update_time()

root.mainloop() #終わりのおまじない

