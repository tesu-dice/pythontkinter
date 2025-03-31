import tkinter

def key_down(e):     #入力されたキーを「e」として実行？
    key_c = e.keycode    #キーボードそれぞれについた番号
    label1["text"] = "keycode "+str(key_c)    #テキストを更新
    key_s = e.keysym     #入力されたキーの文字
    label2["text"] = "keysym "+key_s

root = tkinter.Tk()
root.geometry("400x200")
root.title("キー入力")
root.bind("<KeyPress>", key_down)     #キーボードが押されたとき実行する関数の設定
#(イベントの設定 , 実行する関数)   イベントにはほかにも何個かの種類がある
fnt = ("Times New Roman", 30)    #フォントをあらかじめ設定しておく
label1 = tkinter.Label(text="keycode", font=fnt)
label1.place(x=0, y=0)     #座標
label2 = tkinter.Label(text="keysym", font=fnt)
label2.place(x=0, y=80)
root.mainloop()
