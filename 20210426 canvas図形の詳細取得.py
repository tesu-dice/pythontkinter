"""
 utf-8
 canvas上の図形の座標なんかを取得


"""
import tkinter as tk

window =tk.Tk()
window.geometry("1000x600")
window.title("canvas上の図形のあれこれ")
#図形設置用キャンパス
kyanpasu = tk.Canvas(window ,width=800 ,height=500 ,bg="#555555")
kyanpasu.place(x=0 ,y=0)

#図形の配置
zukei = kyanpasu.create_rectangle(10,20,80,400,fill="#1111ff" )

#図形の詳細の表示（コマンドプロンプト上に）
shousai = kyanpasu.coords(zukei)  #詳細取得
"""  帰ってくる値（リスト）==[左上のx ,左上のy ,右下のx ,右下のy]
    ※すべて小数点一桁までの値で帰ってくる、それぞれ(x0 ,y0 ,x1 ,y1 )とも表せる？"""


print("そのまま表示"+ str(shousai) + "\n")
print("x0(右上x): "+ str(shousai[0]))
print("y0(右上y): "+ str(shousai[1]))
print("x1(左下x): "+ str(shousai[2]))
print("y1(左下x): "+ str(shousai[3]))


window.mainloop()
