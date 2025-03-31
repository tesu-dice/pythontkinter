"""
ubf-8   20201029
チェックボックスの作成
"""

import tkinter       #tkinterをインポート
#ウィンドウ設定
window = tkinter.Tk()
window.geometry("600x400")
window.title("チェックボックス")
#チェックボックス設定
check_box = tkinter.Checkbutton(text="チェックボックス",font=("游ゴシック",50))    #チェックボックス作成、テキスト、フォント、フォントサイズ設定
check_box.place(x=10,y=50)



window.mainloop()
