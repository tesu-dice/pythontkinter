# 20201015  ubf-8　　by北須賀

#「tkinter」をインポート
import tkinter
#・ウィンドウの設定
#rootという名前のウィンドウ作成
root = tkinter.Tk()
#サイズ設定
root.geometry("300x200")
#タイトル設定
root.title("2020年10月15日のプログラム勉強")
#・文字を表示
#言葉、フォント、サイズ設定
label = tkinter.Label(root, text="文字を表示", font=("遊ゴシック", 20))
label["bg"] = "#ff55ff"    #背景色
label["width"] = 15        #横幅
label["anchor"]  = "w"     #文字を右や左上なんかに寄せる
#表示する座標を指定
label.place(x=80, y=60)
#・画面の表示
#ウィンドウを表示
root.mainloop()
