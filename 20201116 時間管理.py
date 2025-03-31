"""
ubf-8             20201111
ここまでのものをいろいろ切って貼ってして時間管理アプリのようなものを作成する

実装していること
　現在時刻と残り時刻の表示、チェックボックスの作成と削除、スクロールバーでの表示
　（「コード」ファイルの20201015から20201111までの内容を使ってる）

今後
　残りの項目数の表示、なんかキャラクター設置(デスクトップマスコット？)

"""

import tkinter
#ウィンドウの設定
window = tkinter.Tk()
window.geometry("400x460")     #ウィンドウサイズ設定
window.title("時間管理")      #ウィンドウのタイトル設定
window.resizable(width=False, height=False)     #ウィンドウのサイズを変更できないように設定
#----------------------------------現在時刻、残り時間の表示------------------
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
    window.after(1000, now_time)       #一秒毎（1000）にnow_timeを実行？
#現在時刻の表示
jikan = tkinter.Label(font=("游ゴシック", 30))
jikan.place(x=0,y=0)
#残り時間の表示
nokori = tkinter.Label(font=("游ゴシック",30))
nokori.place(x=0,y=60)

#---------------------------------項目表示ようの枠作成--------------------------
#外枠（キャンパス）の作成
canvas = tkinter.Canvas(window ,background="#ffffff")#白色
canvas.place(x=0,y=150,width=400,height=300)
#フレームの設定
#backgroundで背景色設定'#??????'で色を決める「#」がないと読み込めない、右から二つずつ赤緑青
frame = tkinter.Canvas(canvas ,height=300 ,background='#cccccc')#灰
canvas.create_window((0,0),window=frame, anchor="nw")
#縦方向スクロールバーの設定
y_scroll = tkinter.Scrollbar(canvas, orient=tkinter.VERTICAL, command=canvas.yview)  #縦ならVERTICAL、横ならHORIZONTAL
y_scroll.pack(side=tkinter.RIGHT, fill="y")
#横方向スクロールバーの設定
x_scroll = tkinter.Scrollbar(canvas, orient=tkinter.HORIZONTAL, command=canvas.xview)
x_scroll.pack(side=tkinter.BOTTOM, fill="x")
#動きをスクロールバーに反映
canvas["yscrollcommand"] = y_scroll.set
canvas["xscrollcommand"] = x_scroll.set
canvas.config(scrollregion=(0, 0, 400, 300))
#---------------------------チェックボックスの追加、削除-------------------------------------------------
#使うリストをあらかじめ作成
checkbox_list = []
joutai_list = []
sakujo_list =[]
#テキストボックスの設定
text_box = tkinter.Entry(width=45)
text_box.place(x=10, y=125)
#削除ボタンでの操作設定
def sakujo():
    sakujo_list=[] #削除リストは毎回初期化
     #上から何番目を削除するのかを知る
    for i in range(len(checkbox_list)) :
        check = joutai_list[i].get()   #boolean関数は.get()を使わないと取得できない
        if check == True :
            sakujo_list.append(i)
    # ↑でTrueだった回数リストから削除
    for i in range(len(sakujo_list)):
        #削除する列のチェックボックスを非表示にしてリストからも削除
        sakujo_n = sakujo_list[i] -i        #削除するとリストがずれるので、iで修正
        checkbox_list[sakujo_n].destroy()      #チェックボックスはplace_forgetでは消えない？
        checkbox_list.pop(sakujo_n)
        joutai_list.pop(sakujo_n)
    hyouji()
#追加ボタンでの操作設定
def tuika():
    #テキストの取得
    text = text_box.get()             #テキストボックスの値を取得
    if text == "" :
        text = "準エラー：何も入力されていませんでした。"
    text_box.delete(0,"end")          #テキストボックスを空にする
    #チェックボックス設定
    joutai = tkinter.BooleanVar()
    joutai.set(False)
    #チェックボックス作成、テキスト、(フォント、フォントサイズ設定)
    check_box = tkinter.Checkbutton(frame , variable = joutai , text = text , font = ("游ゴシック",10) )
    checkbox_list.append(check_box)         #チェックボックスをリストに追加
    joutai_list.append(joutai)
    hyouji()
#チェックボックスの表示
def hyouji():
    for i in range(len(checkbox_list)) :   #テキストリストの要素数(チェックボックスの数だけ繰り返す)
        checkbox_list[i].place(x=5, y= 5+ i*30)     #チェックリストを表示
    #キャンバスのスクロール範囲を広げる
    #高さ
    zentai_height = len(checkbox_list)*31 +10
    #よこ
    zentai_word=[] #全体の文字数のリスト作成
    for i in range(len(checkbox_list)):
        zentai_word.append(len(checkbox_list[i]["text"]))
    zentai_width = max(zentai_word)*15 + 20
    canvas.config(scrollregion=(0, 0, zentai_width, zentai_height))
    #フレームの範囲を広げる
    frame["height"]=zentai_height
    frame["width"]=zentai_width
# 削除ボタンの作成
sakujobotan = tkinter.Button(window, text="削除" , command = sakujo)
sakujobotan.place(x=350,y=120)
# 追加ボタンの作成
botan = tkinter.Button(window, text="追加" , command = tuika)
botan.place(x=300,y=120) #ボタンを配置する位置の設定
#------------------------最後に回す必要があったもの------------------
now_time()
window.mainloop()
