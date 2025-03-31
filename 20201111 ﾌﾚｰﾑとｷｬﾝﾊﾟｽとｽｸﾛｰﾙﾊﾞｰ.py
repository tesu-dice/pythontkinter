"""
ubf-8        20201109
追加項目の表示場所をキャンパスの中に設定してスクロールバーで操作
"""

import tkinter

#ウィンドウの設定
window = tkinter.Tk()
window.geometry("600x400")
window.title("キャンパスとスクロールバー")
#フレームの作成
frame1 = tkinter.Frame(width=300, height=200, relief="sunken", background="#ff1111") #「relief」で外枠の設定「sunken, raised, groove, ridge」の種類がある
frame1.pack()

#キャンパスの設定
#backgroundで背景色設定'#??????'で色を決める「#」がないと読み込めない、右から二つずつ赤緑青
canvas = tkinter.Canvas(frame1 ,width=300 ,height=200 ,background='#111188')

#縦方向スクロールバーの設定
y_scroll = tkinter.Scrollbar(frame1, orient=tkinter.VERTICAL, command=canvas.yview)  #縦ならVERTICAL、横ならHORIZONTAL
y_scroll.pack(side=tkinter.RIGHT, fill="y")
#横方向スクロールバーの設定
x_scroll = tkinter.Scrollbar(frame1, orient=tkinter.HORIZONTAL, command=canvas.xview)
x_scroll.pack(side=tkinter.BOTTOM, fill="x")
#動きをスクロールバーに反映
canvas["yscrollcommand"] = y_scroll.set
canvas["xscrollcommand"] = x_scroll.set

canvas.pack()

window.mainloop()
