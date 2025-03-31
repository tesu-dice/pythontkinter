"""
20201208     ubf-8
20201116時間管理に、ファイル読み込みを使って格言？みたいなのを追加

実装していること
　現在時刻と残り時刻の表示、チェックボックスの作成と削除、スクロールバーでの表示
　（「コード」ファイルの内容を使ってる）
　new!     「今日の一言」の枠を追加、各自の座標などの設定用の関数設定( XXXXX_x , XXXXX_yなどなど)

今後?
　残りの項目数の表示、なんかキャラクター設置(デスクトップマスコット？)
　時計、カレンダー、天気予報

"""

#----------------全体の設定？-------------------------------------------------------
import tkinter
#ウィンドウの設定
window = tkinter.Tk()
window.geometry("600x400")     #ウィンドウサイズ設定
window.title("時間管理")      #ウィンドウのタイトル設定
#window.resizable(width=False, height=False)     #ウィンドウのサイズを変更できないように設定

#--------------------全体配置用の関数設定---------------------------------------------------------------------------
#現在時刻
jikan_x    =10
jikan_y    =10
jikan_s    =20
#残り時間
nokori_x   =10
nokori_y   =50
nokori_s   =20
#canbas(項目を表示する)
canvas_x   =300
canvas_y   =50
canvas_w   =300
canvas_h   =350
#textbox(文字入力)
textbox_x  =300
textbox_y  =30
textbox_w  =45      #横幅
#checkbox(項目)　　　※canvasの中での開始地点の座標
checkbox_x =0
checkbox_y =0
checkbox_s =10    #項目の文字の大きさ
checkbox_n =30    #項目ごとの間隔（文字サイズによって変わる）
#削除ボタン
sakujo_x   =350
sakujo_y   =2
#追加ボタン
tuika_x    =300
tuika_y    =2
#一言表示
hitokoto_x =10
hitokoto_y =150
hitokoto_s = 15
#一言表示の付属の言葉
hitokotohuzoku_x =10
hitokotohuzoku_y =100
hitokotohuzoku_s =10

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
    #タイトルに日付を表示
    weeklist = ["月","火","水","木","金","土","日"]
    month = day.month
    day_n = day.day
    week  = weeklist[day.weekday()]
    title_word ="{0}月{1}日{2}曜日".format(month,day_n,week)
    window.title(title_word)
    #一秒毎（1000）にnow_timeを実行(ループ処理)
    window.after(1000, now_time)
#現在時刻の表示
jikan = tkinter.Label(font=("游ゴシック", jikan_s))
jikan.place(x=jikan_x ,y=jikan_y)
#残り時間の表示
nokori = tkinter.Label(font=("游ゴシック",nokori_s))
nokori.place(x=nokori_x, y=nokori_y)

#---------------------------------項目表示ようの枠作成--------------------------
#外枠（キャンパス）の作成
canvas = tkinter.Canvas(window ,background="#cccccc")#灰色
canvas.place(x=canvas_x, y=canvas_y, width=canvas_w, height=canvas_h )
#フレームの設定
#backgroundで背景色設定'#??????'で色を決める「#」がないと読み込めない、右から二つずつ赤緑青
frame = tkinter.Canvas(canvas ,background='#cccccc')#灰色
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
text_box = tkinter.Entry(width=textbox_w)
text_box.place( x=textbox_x ,y=textbox_y )
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
    check_box = tkinter.Checkbutton(frame , variable = joutai , text = text , font = ("游ゴシック",checkbox_s) )
    checkbox_list.append(check_box)         #チェックボックスをリストに追加
    joutai_list.append(joutai)
    hyouji()
#チェックボックスの表示
def hyouji():
    for i in range(len(checkbox_list)) :   #テキストリストの要素数(チェックボックスの数だけ繰り返す)
        checkbox_list[i].place(x=checkbox_x, y= i*checkbox_n + checkbox_y)     #チェックリストを表示
    #キャンバスのスクロール範囲を広げる
    #高さ
    zentai_height = len(checkbox_list)*31 +10
    #よこ
    zentai_word=[] #全体の文字数のリスト作成
    for i in range(len(checkbox_list)):
        zentai_word.append(len(checkbox_list[i]["text"]))
    #項目数が0の時の処理
    if len(zentai_word) == 0 :
        frame["height"]=0
        frame["width"]=0
    #項目数が２以外の時
    if len(zentai_word) != 0 :
        zentai_width = max(zentai_word)*15 + 20
        canvas.config(scrollregion=(0, 0, zentai_width, zentai_height))
        #フレームの範囲を広げる
        frame["height"]=zentai_height
        frame["width"]=zentai_width
# 削除ボタンの作成
sakujobotan = tkinter.Button(window, text="削除" , command = sakujo)
sakujobotan.place(x=sakujo_x, y= sakujo_y)
# 追加ボタンの作成
botan = tkinter.Button(window, text="追加" , command = tuika)
botan.place(x=tuika_x, y=tuika_y) #ボタンを配置する位置の設定

#-----------一言表示----------------------------------------------
#テキストファイルの読み込み
hitokoto_file = open("20201208 読み込み用.txt")
#ループ処理でリストに保存
hitokotolist = []
for date in hitokoto_file :     #ファイルの中にデータがあるだけ繰り返す？
    hitokoto_n =date.strip("\n")     #改行で区切りを作ってリストに１列ずつ
    hitokotolist.append(hitokoto_n)
#リストからランダムに一つ選出
import random     #ランダム関数のインポート
ransuu = random.randint(0,len(hitokotolist) -1)
#一言のラベル設定
hitokotoword = tkinter.Label(window, text=hitokotolist[ransuu] ,font=("游ゴシック" , hitokoto_s) )
hitokotoword.place(x=hitokoto_x , y= hitokoto_y )
#一言の上に「今日のひとこと」と表示する用のラベル
hitokonoto_huzoku = tkinter.Label(text="今日の一言" , font=("游ゴシック" , hitokotohuzoku_s) )
hitokonoto_huzoku.place(x=hitokotohuzoku_x , y=hitokotohuzoku_y)
#------------------------最後に回す必要があったもの------------------
now_time()
window.mainloop()
