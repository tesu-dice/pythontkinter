"""
ubf8 20201026
ウィンドウでボタン作成+入力
"""

import tkinter         #「tkinter」をインポート
#ウィンドウの設定
window = tkinter.Tk()           #ウィンドウ作成
window.geometry("600x300")               #サイズ設定
window.title("ボタン作って入力")                #タイトル設定

#ボタンクリックでの処理
def botan_click():
  print("メッセージ:入力してください")       #個々の処理はコマンドプロンプトで行う
  word = input()
  print("入力された文字　　" + word)
# ボタンの作成
botan = tkinter.Button(window, text='入力してください', command = botan_click)
botan.place(x=10,y=10) #ボタンを配置する位置の設定

#文字の設定
moji1 = tkinter.Label(window, text="ボタンを押して入力しましょう\n"  + "コマンドプロンプトで入力してください", font=("游ゴシック", 20))
moji1.place(x=10, y=50)

window.mainloop()
