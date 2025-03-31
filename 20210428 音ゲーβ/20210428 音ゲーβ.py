"""
utf-8 20210428～
楽譜のシステム変更への対応（readline関数）      済
ミスした時の図形の削除（move） new! 　　　　　　済
コンボ数の表示  new!                          済
タイマーの計算を少し変える（import time関係）   済
ラベルに外枠をつけて配置　new!                 済
判定の追加　new!                              済
スコアの追加　new!                            済
キー入力時の判定関数の整理（key_down）         済
プロセカ風にカラーの調整                       済

概要
20210427に追加してキーボード判定をする

参考
20210427
ーーーーーーーーーーーーーーー　　　　～注意～　　　　ーーーーーーーーーーーーーーー
python39を指定のフォルダに入れないと動きません
詳しくはread me を読みましょう。
ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

実行するとtxtに関してのエラー？を出すけど今のところは問題なし
"""


import tkinter as tk    #GUI用のtkinterをtkとして設定
import vlc              #音楽流す用にインポート
import time   #タイマー計算用
#ゲームプレイ用の設定ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
kyoku ="20210428"    #曲名の指定
fail = ".mp3"        #音源のファイル種類の指定
M_volume = 100     #音楽の音量設定0～100
window_bg ="#222222"
key1 = "e"
key2 = "f"
key3 = "j"
key4 = "i"
#ノーツ関係の設定
speed = 6         #ノーツの落下スピード
haba = 20         #ノーツの縦幅1～50？
move_per_sec = 20    #ノーツの描写枚数（毎秒）
B_color = "#ffffff"      #ノーツの色
hanteiL_x = 550             #判定ラインの位置
hanteiL_color = "#9999ff"    #判定部分の色  RGB値で検索するとわかりやすい
linecolorA    = "#858585"     #ノーツの落下する部分の色AとBの色二種
linecolorB    = "#858585"     #Bの色
#判定距離の設定
perfect = speed * (100//move_per_sec) /2
great = perfect*2
good = perfect*3

#ラベル用の設定
FONT = ("游ゴシック",30)
LabelsWidth =7
LabelsBG  = "#ffffff"    #ラベルの背景色
perfect_bg= "#ff00ff"    #パーフェクトでの背景色
great_bg  = "#33ffff"    #グレートでの
good_bg   = "#33ff00"    #グッドでの
timer_X = 410
timer_Y = 50
combo_X = 410
combo_Y = 350
score_X = 410
score_Y = 200
hyoukaL_X = 410
hyoukaL_Y = 500
#　　　　画面の配置　　　　ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#ウィンドウ設定
window = tk.Tk()
window.geometry("600x600+100+50")     #ウィンドウサイズ設定
window.config(background=window_bg)   #ウィンドウの背景色を指定
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
line1.create_rectangle(0,hanteiL_x,100,550+haba,fill=hanteiL_color )  #判定部分の目安ラインをそれぞれ設置
line2.create_rectangle(0,hanteiL_x,100,550+haba,fill=hanteiL_color )
line3.create_rectangle(0,hanteiL_x,100,550+haba,fill=hanteiL_color )
line4.create_rectangle(0,hanteiL_x,100,550+haba,fill=hanteiL_color )
line1.create_text(50,585 ,text=key1.upper() , font=("游ゴシック",20) )       #目安ラインの下に対応キーの案内テキスト
line2.create_text(50,585 ,text=key2.upper() , font=("游ゴシック",20) )       #「文字.upper()」で文字を大文字に変換
line3.create_text(50,585 ,text=key3.upper() , font=("游ゴシック",20) )
line4.create_text(50,585 ,text=key4.upper() , font=("游ゴシック",20) )
#      音ゲーのノーツ設置         ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
#楽譜の読み込み
G_list =[] #一括読み込み用
def readG ():
    gakuhu = open(kyoku+".txt")
    for date in gakuhu :
        line = date.strip("\n")
        G_list.append(line)
    global G_gosa
    G_gosa = G_list.pop(0)     #落下時間などのスタート時間の誤差を修正する用

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

def readline():
    global setlist
    if len(G_list) != 0:
        setlist = G_list.pop(0) #G_listの一つ目をとる
        setlist = setlist.split("/")    #「/」で区切る

def setB ():

    B_timer = int(setlist[4])/10 + int(G_gosa)/10  #最初のノーツの位置、落下時間分の誤差修正
    if B_timer   <= timer :
        setblock()
        readline()
    window.after(10,setB)


#       ブロック関係の関数を設定        ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
B_list1 = []   #各列のブロックの保存、存在確認
B_list2 = []
B_list3 = []
B_list4 = []
#ブロックの設置関数
def makeB1() :
    block1 = line1.create_rectangle(0,0,100,haba,fill=B_color ,tag="Block")
    B_list1.append(block1)      #　↑　(左上x,左上y,右上x,右下y,fill=色,tag=識別) #ブロックの配置1～4
def makeB2() :
    block2 = line2.create_rectangle(0,0,100,haba,fill=B_color ,tag="Block")
    B_list2.append(block2)
def makeB3() :
    block3 = line3.create_rectangle(0,0,100,haba,fill=B_color ,tag="Block")
    B_list3.append(block3)
def makeB4() :
    block4 = line4.create_rectangle(0,0,100,haba,fill=B_color ,tag="Block")
    B_list4.append(block4)
#ブロック移動とミスの判定
def move():
    line1.move("Block",0,speed)   #(タグor名前 , x移動 ,y移動)
    line2.move("Block",0,speed)
    line3.move("Block",0,speed)
    line4.move("Block",0,speed)

    #ミスの判定
    if len(B_list1) != 0 :
        if line1.coords(B_list1[0])[1] >= 600 :     #line.coords(XXX)[1] はXXXのy０座標の値
            sakujo = B_list1.pop(0)
            line1.delete(sakujo)
            combo_Re()
            print("ライン1でミス！")

    if len(B_list2) != 0 :
        if line2.coords(B_list2[0])[1] >= 600 :
            sakujo = B_list2.pop(0)
            line2.delete(sakujo)
            combo_Re()
            print("ライン2でミス！")

    if len(B_list3) != 0 :
        if line3.coords(B_list3[0])[1] >= 600 :
            sakujo = B_list3.pop(0)
            line3.delete(sakujo)
            combo_Re()
            print("ライン3でミス！")

    if len(B_list4) != 0 :
        if line4.coords(B_list4[0])[1] >= 600 :
            sakujo = B_list4.pop(0)
            line4.delete(sakujo)
            combo_Re()
            print("ライン4でミス！")

    window.after(move_per_sec,move)


#        音楽を流す         ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
def playsound():
    music = vlc.MediaPlayer()    #music を音楽再生機能と関連づける？
    music.set_mrl( kyoku + fail )  #musicのファイル名を指定
    music.audio_set_volume(M_volume)   #musicの音量設定（）の中身は0～100
    music.play()        #musicを再生


#     タイマー表示　　　ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
start = time.time()
time_L = tk.Label( window, font=FONT ,width=LabelsWidth ,bg=LabelsBG)
time_L.place(x=timer_X, y=timer_Y)
def time_update() :
    global timer
    timer = (time.time() - start ) //0.1 /10      #timerは開始してからの時間小数点1位まで
    min = int(timer//60)     #「//」は切り捨て除算
    sec = int(timer%60)      # int()は小数点以下切り捨て
    if sec//10 ==0 :
        sec = "0"+ str(sec)
         #  下二行について：　「 \ 」を入れると途中で開業を挟んでも続けてくれるが、「#」でコメント入れたりはできなくなる
    time_L["text"] = str(min) + ":" + str(sec) \
                    + "\n" + str(timer)
    window.after(50,time_update)

#コンボの表示ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
combo = 0
combo_L =tk.Label(window , font=FONT ,width=LabelsWidth ,bg=LabelsBG)

def combo_update():
    combo_L["text"] = "コンボ\n"+ str(combo)
    window.after(100,combo_update) #コンボラベルの文字を更新
combo_update()

combo_L.place(x=combo_X ,y=combo_Y)
def combo_Re():
    global combo
    combo = 0
def combopuls () :
    global combo
    combo += 1

#スコアの表示ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
score = 0
score_L =tk.Label(window , font=FONT ,width=LabelsWidth ,bg=LabelsBG)
score_L.place(x=score_X ,y=score_Y)
def scoreupdate ():
    score_L["text"] = "スコア\n" +str(score)
    window.after(100,scoreupdate)
scoreupdate()

def scorepuls (hyouka):
    global score
    if hyouka == "perfect" :
        score += 100
    if hyouka == "great" :
        score += 50
    if hyouka == "good" :
        score += 25

#判定ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
def hantei (kyori):
    if kyori <=perfect :
        hyouka = "perfect"
        set_hyouka(hyouka)
        scorepuls(hyouka)

    elif kyori <= great :
        hyouka = "great"
        set_hyouka(hyouka)
        scorepuls(hyouka)

    elif kyori <= good :
        hyouka = "good"
        set_hyouka(hyouka)
        scorepuls(hyouka)

#判定のラベル表示
hanteilist =[]
def hanteiL_D ():
    sakujo = hanteilist.pop(0)
    print(len(hanteilist))
    sakujo.destroy()

def set_hyouka (hyouka) :
    if hyouka == "perfect" :     #判定評価によって文字の色を変更
        hyouka_bg = perfect_bg
    if hyouka == "great" :
        hyouka_bg = great_bg
    if hyouka == "good" :
        hyouka_bg = good_bg
    hyouka_L =tk.Label(window , font=FONT ,width=LabelsWidth ,bg=LabelsBG ,fg=hyouka_bg, text=hyouka)
    hyouka_L.place(x=hyoukaL_X , y=hyoukaL_Y)                              #「fg (oreground)」は文字の色
    hanteilist.append(hyouka_L)
    print(len(hanteilist))
    window.after(750 , hanteiL_D    )   #0.5秒後にラベルを削除






#キー入力の処理、入力時の判定ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
def set_kyori(a):
    global kyori
    kyori = abs(a - hanteiL_x)    #「abs()」でかっこの中身の絶対値をとる
    hantei(kyori)

def key_down(e):     #入力されたキーを「e」として実行
    key = e.keysym     #入力されたキーの文字をkeyに代入
    if key == key1 :    #Sキー処理
        print(key1 +"が押された")
        if len(B_list1) !=0:
            a = line1.coords(B_list1[0])[1]   #line1上の一番下の図形のy0の値を取得
            set_kyori(a)   #「a」の値を利用して「set_kyori」を起動
            if kyori <=good:
                sakujo = B_list1.pop(0)
                line1.delete(sakujo)
                combopuls()

    if key == key2 :    #ｆキー処理
        print(key2 + "が押された")
        if len(B_list2) !=0:
            a = line2.coords(B_list2[0])[1]
            set_kyori(a)
            if kyori <= good :
                sakujo = B_list2.pop(0)
                line2.delete(sakujo)
                combopuls()

    if key == key3 :    #ｊキー処理
        print(key3 + "が押された")
        if len(B_list3) !=0:
            a = line3.coords(B_list3[0])[1]
            set_kyori(a)
            if kyori <= good :
                sakujo = B_list3.pop(0)
                line3.delete(sakujo)
                combopuls()

    if key == key4 :    #Lキー処理
        print(key4 + "が押された")
        if len(B_list4) !=0:
            a = line4.coords(B_list4[0])[1]
            set_kyori(a)
            if kyori <= good :
                sakujo = B_list4.pop(0)
                line4.delete(sakujo)
                combopuls()

#↓の実行には↑の「key_down」関数を先に設定しておく必要がある
window.bind("<KeyPress>", key_down)     #キーボードが押されたとき実行する関数の設定
#(イベントの設定 , 実行する関数)   イベントにはほかにも何個かの種類がある





#プログラム内容確認用のプリント関数
""" 判定距離目安 """
print(str(perfect))
print(str(great) )
print(str(good) )

#        プログラムの最後に順に関数を起動（起動？）         ーーーーーーーーーーーーーーーーーー

time_update()#タイマーの設定と表示はその場で実行
playsound()      #音楽を流す
readG()          #楽譜読み込み
readline()
setB()       #ブロック設置
move()           #ブロック移動

#画面を表示
window.mainloop()
