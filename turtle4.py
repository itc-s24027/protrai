#「turtle4.py」という名前で保存しましょう
# カラフルな花をかく

from turtle import *
shape("turtle")
col = ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    circle(100)
    left(72)

done()
