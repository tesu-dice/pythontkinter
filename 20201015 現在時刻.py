# 20201015 ubf-8
#時間を表示、リアルタイム処理
import tkinter
import datetime   #「datetime」をインポート

def now_time():   #「now_time」という名前の関数を作る
    day = datetime.datetime.now()          #現在時刻を取得
    time = "{0}時{1}分{2}秒".format(day.hour, day.minute, day.second)      #「time」を「ｘ時ｘ分ｘ秒」で設定
    label["text"] = "現在時刻"+time          #
    root.after(1000,now_time)

#文字を表示
root = tkinter.Tk()
root.geometry("1000x500")
root.title("時計？")
label = tkinter.Label(font=("游ゴシック", 60))
label.pack()
now_time()
root.mainloop()
