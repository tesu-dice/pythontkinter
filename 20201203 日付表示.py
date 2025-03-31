"""
20201203 ubf-8
daytimeを使って日付を表示
第何週か、何日何曜日かなど
"""
import tkinter
#ウィンドウの設定
root = tkinter.Tk()
root.geometry("370x120")     #ウィンドウサイズ設定
root.title("日付表示")      #ウィンドウのタイトル設定
#現在時刻を取得
import datetime   #「datetime」をインポート
def now_time():   #「now_time」という名前の関数を作る
    day = datetime.datetime.now()          #現在時刻を取得
    #現在時刻設定
    month = day.month
    Day = day.day
    week = day.weekday()
    rh = day.hour     #時間
    rm = day.minute   #分
    rs = day.second   #秒
    time = "{0}月{1}日:{2}曜日 {3}:{4}:{5}".format(month,Day,week,rh,rm,rs)      #「time」を「ｘ時ｘ分ｘ秒」で設定
    jikan["text"] = time          #nowtimeのテキストを設定
    root.title(str(time))

    root.after(1000, now_time)       #一秒毎（1000）にnow_timeを実行？
#現在時刻の表示
jikan = tkinter.Label(font=("游ゴシック", 30))
jikan.place(x=0,y=0)

now_time()
root.mainloop()
