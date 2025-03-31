# 2021013  ubf-8　　by北須賀

#「tkinter」をインポート
import tkinter
#・ウィンドウの設定
#rootという名前のウィンドウ作成
root = tkinter.Tk()
#サイズ設定
root.geometry("600x600")
#タイトル設定
root.title("画像表示")
#------------------------------------
#画像表示1 こっちはよくわからん
gazou = tkinter.PhotoImage(file="00a.png")

canvas = tkinter.Canvas(background="#cccccc" ,width=50 ,height=50)
canvas.place(x=50 ,y=50)
#canvas内に画像を表示
canvas.create_image(0,0 ,image=gazou)

#-------------------------------------------
#画像を「Label」を使って表示    こっちのがおすすめ
gazou2 = tkinter.PhotoImage(file="00a.png")
#画像の縦・横幅もここで設定　（伸ばせる）
label_ver = tkinter.Label(root, image=gazou ,width=100 ,height=50)
label_ver.place(x=50, y=150)
#・画面の表示
#ウィンドウを表示
root.mainloop()
