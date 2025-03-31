"""
UBF-8     20201030
ウィンドウにテキストボックスを設定、その値を取得
"""
import tkinter

window = tkinter.Tk()
window.geometry("600x400")
window.title("テキストボックス")

text_box = tkinter.Entry(width=20)
text_box.place(x=10, y=10)

list = []
def kousin ():

    text = text_box.get()
    list.append(text)
    text_box.delete(0,"end")
    for i in range(len(list)) :
            #チェックボックス設定
            check_box = tkinter.Checkbutton( window ,  text = list[i] , font = ("游ゴシック",10)  )    #チェックボックス作成、テキスト、フォント、フォントサイズ設定
            check_box.place(x=10,y=30 + 25*i)

# ボタンの作成
botan = tkinter.Button(window, text="追加" , command = kousin)
botan.place(x=150,y=10) #ボタンを配置する位置の設定

window.mainloop()
