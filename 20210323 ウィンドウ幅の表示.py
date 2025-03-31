"""
20210323  ubf-8　　by北須賀
ウィンドウの幅が表示されるようにする

"""
#tkinterを使えるようにするーーーーーーーーーーーーーーーーーーーー
import tkinter    #GUIウィンドウを使えるように
import re         #後で出てくるre.split()を使えるように
#ウィンドウの設定ーーーーーーーーーーーーーーーーーーーーーーーーー
window = tkinter.Tk() #ウィンドウ作成
window.title("ウィンドウ幅を表示")#タイトル設定
window.geometry("500x400") #起動時のウィンドウサイズ設定

#ウィンドウ幅表示用のラベルの設定ーーーーーーーーーーーーーーーーーー
yoko_l = tkinter.Label(font=("遊ゴシック",60)) #文字表示用のラベル準備+文字サイズ設定
tate_l = tkinter.Label(font=("遊ゴシック",60))
X_l = tkinter.Label(font=("遊ゴシック",60))
Y_l = tkinter.Label(font=("遊ゴシック",60))
yoko_l.place(y=0)        #それぞれのラベルの表示座標の設定
tate_l.place(y=100)
X_l.place(y=200)
Y_l.place(y=300)


#毎秒幅の表示をこうしんするための設定ーーーーーーーーーーーーー
def kousin(): #kousinという一連の関数？を設定
    windowsize = window.geometry() #ウィンドウの縦・横幅などを取得
    #この時「windowsize= 横幅x縦幅+ｘ座標+ｙ座標」の文字列

    windowsize = re.split("[x+]",windowsize)#文字列をリストとして分解
    #「er.split("[分割する文字いくつでも今回はｘと+]"　, 分割する文字列　)」
    #「re.split()」はreモジュールをインポートしてないと使えない
    #ここで「windowsize=[横幅,縦幅,X座標,Y座標]」のリストになる
    yoko_l["text"]= "横幅"  + windowsize[0]  #それぞれラベルの文字とリストの内容を連携+文字を少し追加
    tate_l["text"]= "縦幅"  + windowsize[1]
    X_l["text"]   = "X座標" + windowsize[2]
    Y_l["text"]   = "Y座標" + windowsize[3]
    window.after(500,kousin) #一度始めたら1秒ごとに繰り返すように設定
kousin() #最初のkousinを実行

#ウィンドウを画面上に表示ーーーーーーーーーーーーーーーーーーーー
window.mainloop()
