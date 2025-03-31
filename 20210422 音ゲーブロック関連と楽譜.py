"""
utf-8 20210422
音ゲー用ブロック落下の設定+判定

仕様
ブロック用のテキスト読み込み　+　ブロックの作成　

参考
20210413 音ゲー用テキスト読み込み

"""
import tkinter as tk

#ウィンドウの設定ーーーーーーーーーーーーーーーーーーーーーーーーーーーー
window = tk.Tk()
window.geometry("600x600+100+50")     #ウィンドウサイズ設定
window.title("音ゲーブロック関連と楽譜")      #ウィンドウのタイトル設定
window.resizable(width=False, height=False)     #ウィンドウのサイズを変更できないように設定

#音ゲー用line配置
line1 = tk.Canvas(window, bg="#999999" , width=100, height=600)
line1.place(x=0,y=0)
line2 = tk.Canvas(window, bg="#555555" , width=100, height=600)
line2.place(x=100,y=0)
line3 = tk.Canvas(window, bg="#999999" , width=100, height=600)
line3.place(x=200,y=0)
line4 = tk.Canvas(window, bg="#555555" , width=100, height=600)
line4.place(x=300,y=0)

#楽譜の読み込みーーーーーーーーーーーーーーーーーーーーーーーー
G_list =[] #一括読み込み用
def readG ():
    gakuhu = open("20210422 楽譜.txt")
    for date in gakuhu :
        line = date.strip("\n")
        G_list.append(line)

#ブロック配置
def setblock():    #これとreadlineで繰り返す
    if setlist[0] == "1":
        makeB1()
    if setlist[1] == "1":
        makeB2()
    if setlist[2] =="1" :
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




#ブロック関係ーーーーーーーーーーーーーーーーーーーーーーーー
B_list1 = []
B_list2 = []
B_list3 = []
B_list4 = []
#ブロックの設置関数
haba = 15
def makeB1() :
    block1 = line1.create_rectangle(0,0,100,haba,fill="#ff55ff" ,tag="Block")
    B_list1.append(block1)      #　↑　(左上x,左上y,右上x,右下y,fill=色,tag=識別)
def makeB2() :
    block2 = line2.create_rectangle(0,0,100,haba,fill="#ff55ff" ,tag="Block")
    B_list2.append(block2)
def makeB3() :
    block3 = line3.create_rectangle(0,0,100,haba,fill="#ff55ff" ,tag="Block")
    B_list3.append(block3)
def makeB4() :
    block4 = line4.create_rectangle(0,0,100,haba,fill="#ff55ff" ,tag="Block")
    B_list4.append(block4)
#ブロック移動
speed = 3
def move():
    line1.move("Block",0,speed)   #(タグor名前 , x移動 ,y移動)
    line2.move("Block",0,speed)
    line3.move("Block",0,speed)
    line4.move("Block",0,speed)
    window.after(2,move)


#プログラムの最後に順に関数を起動（起動？）

readG()          #楽譜読み込み
setB()       #ブロック設置
move()           #ブロック移動

window.mainloop()
