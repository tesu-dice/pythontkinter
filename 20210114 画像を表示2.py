"""
 2021014  ubf-8　　by北須賀

画像表示をボタン型にしたい

"""
#「tkinter」をインポート
import tkinter
import os
#・ウィンドウの設定
#rootという名前のウィンドウ作成
root = tkinter.Tk()
#サイズ設定
root.geometry("600x600")
#タイトル設定
root.title("画像表示")
#------------------------------------------------------

#ボタンクリックでの処理
def botan_click():
  print("画像1がクリックされました")       #ここからの処理はコマンドプロンプトで行う


def botan2_click():
  print("画像2がクリックされました")       #ここからの処理はコマンドプロンプトで行う

#ーーーーーーーーーーー ボタンの作成ーーーーーーーーーーーーーーーー
#画像の読み込み
print( os.getcwd())
gazou = tkinter.PhotoImage(file="00a.png")
#ボタンを作成　(表示する枠組み , 画像の指定 , コマンド名の指定)
botan = tkinter.Button(root, image=gazou, command = botan_click)
botan.place(x=10,y=10) #ボタンを配置する位置の設定

botan2 =tkinter.Button(root, image=gazou ,text="aaaaa", command = botan2_click)
#ボタン（小）のサイズ設定
botan2["heigh"]= 50
botan2["width"] =50

botan2.place(x=100, y=100)







#・画面の表示
#ウィンドウを表示
root.mainloop()
