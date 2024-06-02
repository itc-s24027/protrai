#「turtle3.py」という名前で保存しましょう
# カラフルな星をかく　


from turtle import *
shape("turtle")
#col = ["orange","limegreen","gold","plum","tomato"]
col= ["red","blue","green","brown","black"]
for i in range(5):
    color(col[i])
    forward(100)
    left(144)

done()
