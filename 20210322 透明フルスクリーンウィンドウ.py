"""
20210322  ubf-8　　by北須賀
ウィドウの背景色を透明にする設定にしてウィンドウの中身を透明にする
起動時にフルスクリーンで起動するように設定

"""
#「tkinter」をインポート
import tkinter

#・ウィンドウの設定
#rootという名前のウィンドウ作成
root = tkinter.Tk()

#タイトル設定
root.title("ウィンドウの色を透明に!")

#透明の設定-----------------------------------------
#ウィンドウの背景色設定(0000ff)

root.config(background="#0000ff")
#ウィンドウの背景色を透明にする
root.attributes("-transparentcolor", "#0000ff")

#文字を表示---------------------------------------------
#ラベルの言葉、フォント、サイズ、色(foreground)の設定
label = tkinter.Label(root, text="背景が透明に!!!(フルスクリーン)", font=("遊ゴシック", 60) ,
                     foreground='#ff0000' , background="#ffff00",anchor=tkinter.CENTER)
#表示する座標を指定 ↑のCENTERは中央揃えの意味
label.place(x=200 , y=300)

#フルスクリーンの設定ーーーーーーーーーーーーーーーーーー
root.attributes('-fullscreen', True)

#画像の表示ーーーーーーーーーーーーーーーーーーーーー
#画像表示用の座標取得
yoko = root.winfo_screenwidth()
tate = root.winfo_screenheight()
"""確認用
print(str(yoko) + "と" + str(tate) )
"""
#画像作成
image = tkinter.PhotoImage(file="1testimg.png")
size = 500
gazou = tkinter.Label(root, image=image ,background ="#0000ff" ,
                      width=size , height =size)
size = 100
#差表設定
gx = yoko/3
gy = tate/2
gazou.place(x=gx , y=gy)


#ウィンドウを表示ーーーーーーーーーーーーーーーーーーーーーー
root.mainloop()
