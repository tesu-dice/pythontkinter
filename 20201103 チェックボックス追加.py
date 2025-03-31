"""
UBF-8     20201030
バージョン2　更新するとチェックマークが外れるのを直したい
"""
import tkinter

window = tkinter.Tk()
window.geometry("600x400")
window.title("テキストボックス")

text_box = tkinter.Entry(width=20)
text_box.place(x=10, y=10)

def sakujo ():
    check_box.place_forget()
    sakujo_botan.place_forget()


list = []
def kousin ():                           #追加のボタンを押したときの処理
    text = text_box.get()             #テキストボックスの値を取得
    list.append(text)                 #値をリストに追加
    text_box.delete(0,"end")          #テキストボックスを空にする

    i = list.index(text)
    #チェックボックス設定
    global check_box
    check_box = tkinter.Checkbutton( window ,  text = list[i] , font = ("游ゴシック",10)  )    #チェックボックス作成、テキスト、フォント、フォントサイズ設定
    check_box.place(x=10,y=30 + 25*(i+1) )
    # 削除ボタンの作成
    global sakujo_botan
    sakujo_botan = tkinter.Button(window, text="削除" , command = sakujo)
    sakujo_botan.place( x=150 , y=30+ 25*(i+1) ) #ボタンを配置する位置の設定

# ボタンの作成
botan = tkinter.Button(window, text="追加" , command = kousin)
botan.place(x=150,y=10) #ボタンを配置する位置の設定

window.mainloop()
