# 20201020 ubf-8

import tkinter
W = tkinter.Tk()
W.geometry("600x600")
W.title("文字表示のテスト")
#moji1の設定
moji1 = tkinter.Label(W, text="文字1", font=("游ゴシック", 20))
moji1.place(x=10, y=10)
#文字2の設定
moji2 = tkinter.Label(W,text="文字２",font=("游ゴシック",50))
moji2.place(x=100,y=100)
W.mainloop()
