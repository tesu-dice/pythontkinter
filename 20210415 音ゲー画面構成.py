"""
ubf-8   20210415
ウィンドウ内にフレーム設置、オブジェクトの座標なんかの設定

仕様
音ゲー用の基板？大まかな形の設定

"""
import tkinter as tk   #GUIで使えるように
import re       #後で出てくるre.split()を使えるように
#ウィンドウの設定ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
window = tk.Tk()
window.geometry("600x600+100+50")     #ウィンドウサイズ設定
window.title("音ゲーオブジェクト試作")      #ウィンドウのタイトル設定
window.resizable(width=False, height=False)     #ウィンドウのサイズを変更できないように設定

#音ゲー用lineせってい
line1 = tk.Canvas(window, bg="#999999" , width=100, height=600)
line1.place(x=0,y=0)
line2 = tk.Canvas(window, bg="#555555" , width=100, height=600)
line2.place(x=100,y=0)
line3 = tk.Canvas(window, bg="#999999" , width=100, height=600)
line3.place(x=200,y=0)
line4 = tk.Canvas(window, bg="#555555" , width=100, height=600)
line4.place(x=300,y=0)



#スコアの表示

def score_hyouji():
    score = 0
    tensu = tk.Label(window, text="スコア：" + str(score) , font=("游ゴシック",20) )
    tensu.place(x=410,y=0)


#タイム
time=0

time_L = tk.Label( window, font=("游ゴシック",30) )
time_L.place(x=410, y=50)
def time_hyouji():
    global time
    time =time + 1
    min = time//60     #「//」は切り捨て除算
    sec = time%60

    if sec//10 ==0 :
        sec = "0"+ str(sec)
    time_L["text"] = str(min) + "："+ str(sec)
    window.after(1000,time_hyouji)

#コンボ数


#good,neceとかの判定

score_hyouji()
time_hyouji()
#ウィンドウを画面上に表示ーーーーーーーーーーーーーーーーーーー
window.mainloop()
