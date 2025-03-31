"""
utf-8 20210427
音ゲーのキーボード入力の判定をする

20210424に追加してキーボード判定をする

参考
20210421　リアルタイムキー入力
20210424
ーーーーーーーーーーーーーーー　　　　～注意～　　　　ーーーーーーーーーーーーーーー
コマンドプロンプト（エクスプローラーでcmdと入れて実行）で
「　　python -m pip install python-vlc　　」
と入れてインストールをしてからじゃないとimprot vlcがエラーになる！
ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

実行するとtxtに関してのエラー？を出すけど今のところは問題なし
"""


import tkinter as tk
import vlc
#ゲームプレイ用の設定
kyoku ="20210427"    #曲名の指定

speed = 5         #ノーツの落下スピード
haba = 20         #ノーツの縦幅1～50？

M_volume = 60     #音楽の音量設定0～100

B_color = "#831583"      #ノーツの色

meyasu_x = 550             #判定ラインの位置
meyasu_color ="#800000"    #判定部分の色  RGB値で検索するとわかりやすい

linecolorA = "#ff69B4"     #ノーツの落下する部分の色AとBの色二種
linecolorB = "#ffb6c1"


#　　　　画面の配置　　　　ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#ウィンドウ設定
window = tk.Tk()
window.geometry("600x600+100+50")     #ウィンドウサイズ設定
window.title("音ゲーブロック関連と楽譜")      #ウィンドウのタイトル設定
window.resizable(width=False, height=False)     #ウィンドウのサイズを変更できないように設定

#音ゲー用line配置
line1 = tk.Canvas(window, bg=linecolorA , width=100, height=600)
line1.place(x=0,y=0)
line2 = tk.Canvas(window, bg=linecolorB , width=100, height=600)
line2.place(x=100,y=0)
line3 = tk.Canvas(window, bg=linecolorA , width=100, height=600)
line3.place(x=200,y=0)
line4 = tk.Canvas(window, bg=linecolorB , width=100, height=600)
line4.place(x=300,y=0)

#判定用の目安ライン設置
line1.create_rectangle(0,meyasu_x,100,550+haba,fill=meyasu_color )
line2.create_rectangle(0,meyasu_x,100,550+haba,fill=meyasu_color )
line3.create_rectangle(0,meyasu_x,100,550+haba,fill=meyasu_color )
line4.create_rectangle(0,meyasu_x,100,550+haba,fill=meyasu_color )


#      音ゲーのノーツ設置         ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#楽譜の読み込み
G_list =[] #一括読み込み用
def readG ():
    gakuhu = open(kyoku+".txt")
    for date in gakuhu :
        line = date.strip("\n")
        G_list.append(line)
#ブロック配置
def setblock():    #これとreadlineで繰り返す
    if setlist[0] == "1":
        makeB1()
    if setlist[1] == "1":
        makeB2()
    if setlist[2] == "1" :
        makeB3()
    if setlist[3] == "1":
        makeB4()
    setB()    #setに戻る

def readline():
    global setlist
    setlist = G_list.pop(0) #G_listの一つ目をとる
    setlist = setlist.split("/")    #「/」で区切る

def setB ():
    readline()
    window.after(setlist[4],setblock) #５番目の数字秒後にsetblockを起動


#       ブロック関係の関数を設定        ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
B_list1 = []
B_list2 = []
B_list3 = []
B_list4 = []
#ブロックの設置関数
def makeB1() :
    block1 = line1.create_rectangle(0,0,100,haba,fill=B_color ,tag="Block")
    B_list1.append(block1)      #　↑　(左上x,左上y,右上x,右下y,fill=色,tag=識別)
def makeB2() :
    block2 = line2.create_rectangle(0,0,100,haba,fill=B_color ,tag="Block")
    B_list2.append(block2)
def makeB3() :
    block3 = line3.create_rectangle(0,0,100,haba,fill=B_color ,tag="Block")
    B_list3.append(block3)
def makeB4() :
    block4 = line4.create_rectangle(0,0,100,haba,fill=B_color ,tag="Block")
    B_list4.append(block4)
#ブロック移動
def move():
    line1.move("Block",0,speed)   #(タグor名前 , x移動 ,y移動)
    line2.move("Block",0,speed)
    line3.move("Block",0,speed)
    line4.move("Block",0,speed)
    window.after(10,move)


#        音楽を流す         ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
def playsound():
    music = vlc.MediaPlayer()    #music を音楽再生機能と関連づける？
    music.set_mrl(kyoku+'.mp3')  #musicのファイル名を指定
    music.audio_set_volume(M_volume)   #musicの音量設定（）の中身は0～100
    music.play()        #musicを再生


#     タイマー表示　　　ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
timer= -1
time_L = tk.Label( window, font=("游ゴシック",30) )
time_L.place(x=410, y=50)
def time():
    global timer
    timer = timer + 1
    min = timer//60     #「//」は切り捨て除算
    sec = timer%60

    if sec//10 ==0 :
        sec = "0"+ str(sec)
    time_L["text"] = str(min) + ":"+ str(sec)
    window.after(1000,time)

#キー入力の処理、入力時の判定ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
def key_down(e):     #入力されたキーを「e」として実行
    key = e.keysym     #入力されたキーの文字をkeyに代入
    if key == "s" :    #Sキー処理
        print("sが押された")
        if len(B_list1) !=0:
            a = line1.coords(B_list1[0])[1]   #line1上の一番下の図形のy0の値を取得
            if abs(a-550) <= haba :    #「abs()」でかっこの中身の絶対値をとる
                sakujo = B_list1.pop(0)
                line1.delete(sakujo)
                print("パーフェクト")

    if key == "f" :    #ｆキー処理
        print("fが押された")
        if len(B_list2) !=0:
            a = line2.coords(B_list2[0])[1]   #line1上の一番下の図形のy0の値を取得
            if abs(a-550) <= haba :    #「abs()」でかっこの中身の絶対値をとる
                sakujo = B_list2.pop(0)
                line2.delete(sakujo)
                print("パーフェクト")

    if key == "j" :    #ｊキー処理
        print("jが押された")
        if len(B_list3) !=0:
            a = line3.coords(B_list3[0])[1]   #line1上の一番下の図形のy0の値を取得
            if abs(a-550) <= haba :    #「abs()」でかっこの中身の絶対値をとる
                sakujo = B_list3.pop(0)
                line3.delete(sakujo)
                print("パーフェクト")

    if key == "l" :    #Lキー処理
        print("lが押された")
        if len(B_list4) !=0:
            a = line4.coords(B_list4[0])[1]   #line1上の一番下の図形のy0の値を取得
            if abs(a-550) <= haba :    #「abs()」でかっこの中身の絶対値をとる
                sakujo = B_list4.pop(0)
                line4.delete(sakujo)
                print("パーフェクト")


#↓の実行には↑の「key_down」関数を先に設定しておく必要がある
window.bind("<KeyPress>", key_down)     #キーボードが押されたとき実行する関数の設定
#(イベントの設定 , 実行する関数)   イベントにはほかにも何個かの種類がある



#        プログラムの最後に順に関数を起動（起動？）         ーーーーーーーーーーーーーーーーーー
playsound()      #音楽を流す
readG()          #楽譜読み込み
setB()       #ブロック設置
move()           #ブロック移動
time()       #タイマーの設定と表示
#画面を表示
window.mainloop()
