"""
ubf8     20201026
クラスで表みたいに表示
"""

import tkinter    #tkinterをインポート
#ウィンドウ設定
window = tkinter.Tk()      #windowという名前のウィンドウを作成
window.geometry("600x400")      #サイズ設定
window.title("表みたいに表示")     #タイトル設定
#表示することの設定
koumoku = ["項目１","項目２","項目３","項目４","項目５"]
bikou   = ["備考１","備考２","備考３","備考４","備考５"]
#表みたいに表示
moji=""
for i in range(len(koumoku)):
    #mojiの設定
    moji = moji + koumoku[i] + "  " + bikou[i] + "\n"
moji = tkinter.Label(window, text=moji, font=("游ゴシック", 20))
moji.place(x= 20, y=10)


window.mainloop()           #ウィンドウを表示
