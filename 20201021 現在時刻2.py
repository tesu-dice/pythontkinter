"""
ubf-8 20201021~
中身（+今後予定）
「現在時刻の表示、一日の残り時間、」
天気や気温、タイマーの機能を追加したい！
"""

import tkinter
#ウィンドウの設定
root = tkinter.Tk()
root.geometry("370x120")     #ウィンドウサイズ設定
root.title("文字表示のテスト")      #ウィンドウのタイトル設定
#現在時刻を取得
import datetime   #「datetime」をインポート
def now_time():   #「now_time」という名前の関数を作る
    day = datetime.datetime.now()          #現在時刻を取得
    #現在時刻設定
    rh = day.hour
    rm = day.minute
    rs = day.second
    if rh < 10 :
        rh = "0"+ str(rh)
    if rm < 10 :
        rm = "0" + str(rm)
    if rs < 10 :
        rs = "0" + str(rs)
    time = "現在時刻　{0}:{1}:{2}".format(rh,rm,rs)      #「time」を「ｘ時ｘ分ｘ秒」で設定
    jikan["text"] = time          #nowtimeのテキストを設定
    #残り時間を設定
    nh = 23 - day.hour
    nm = 60 - day.minute
    ns = 60 - day.second
    if nh < 10 :
        nh = "0"+ str(nh)
    if nm < 10 :
        nm = "0" + str(nm)
    if ns < 10 :
        ns = "0" + str(ns)
    nokori_time =  "残り時間　{0}:{1}:{2}".format(nh,nm,ns)
    nokori["text"] = nokori_time
    root.after(1000, now_time)       #一秒毎（1000）にnow_timeを実行？
#現在時刻の表示
jikan = tkinter.Label(font=("游ゴシック", 30))
jikan.place(x=0,y=0)

#残り時間の表示
nokori = tkinter.Label(font=("游ゴシック",30))
nokori.place(x=0,y=60)
now_time()
root.mainloop()
