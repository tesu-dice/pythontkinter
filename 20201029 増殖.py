"""
ubf-8    20201029
ボタン（ウィンドウ全体にしたい）を触ると画面が増えるやつを作りたい
"""
import tkinter

window = tkinter.Tk()
window.geometry("600x400")
window.title("増殖")

def botan_click():
    window = tkinter.Tk()
    window.geometry("600x400")
    window.title("増殖")
    botan1 = tkinter.Button(window, text='クリックすると新たなウィンドウが！', command = botan_click)
    botan1.place(x=20,y=20) #ボタンを配置する位置の設定
#ボタンの作成

botan1 = tkinter.Button(window, text='ボタン', command = botan_click)
botan1.place(x=20,y=20) #ボタンを配置する位置の設定

window.mainloop()
