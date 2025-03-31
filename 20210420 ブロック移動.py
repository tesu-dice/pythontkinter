"""
ubf-8           20210420
音ゲー用ブロック移動テスト

☆moveの関数にはタグを使って指定ができる！

参考
https://daeudaeu.com/tkinter_canvas_method/

"""

import tkinter as tk

window = tk.Tk() #ウィンドウ作成
window.title("サンプル")#タイトル設定
window.geometry("500x400") #起動時のウィンドウサイズ設定

frame = tk.Canvas(window , bg="#555555")
frame.place(x=0,y=0,width=500,height=400)

XX = frame.create_rectangle(10,10,20,20,fill="#AAAAAA" ,tag="block")
YY = frame.create_rectangle(50,10,60,80,fill="#AAAAAA" ,tag="block")
ZZ = frame.create_rectangle(100,10,150,200,fill="#AAAAAA" ,tag="block")

def move():
    frame.move("block" ,0,1) #(タグまたはオブジェクト名 ,ｘの移動数,ｙの移動)
    window.after(5,move)
move()

window.mainloop()
