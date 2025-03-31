"""
ubf-8    20201106
削除ボタンを押すとチェック済みは消えるようにする

今回使うリストまとめ
チェックボックスのリスト、テキストのリスト、チェック状態のリスト


---------------仕組み？------------------------------
チェックボックスを名前にしてリストに入れる
　　　チェックリストのリスト（C_list）　＝　[チェックボックス１,チェックボックス２,チェックボックス３ , ......]
　　

チェックボックスの場所は削除したときにfor文で繰り返しながら変更させる
for i in range(?):
    C_list[i].place(なんとかかんとか)

---------------------------------------------------------
"""

import tkinter

#ウィンドウの設定
window = tkinter.Tk()
window.geometry("600x400")
window.title("チェック済みの削除")
#テキストボックスの設定
text_box = tkinter.Entry(width=20)
text_box.place(x=10, y=10)

#使うリストをあらかじめ作成
checkbox_list = []
joutai_list = []
sakujo_list =[]
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
    check_box = tkinter.Checkbutton( window , variable = joutai , text = text , font = ("游ゴシック",10) )
    checkbox_list.append(check_box)         #チェックボックスをリストに追加
    joutai_list.append(joutai)
    hyouji()


#チェックボックスの表示
def hyouji():
    for i in range(len(checkbox_list)) :   #テキストリストの要素数(チェックボックスの数だけ繰り返す)
        checkbox_list[i].place(x=10, y= 40+ i*30)



# 削除ボタンの作成
sakujobotan = tkinter.Button(window, text="削除" , command = sakujo)
sakujobotan.place(x=190,y=10)
# 追加ボタンの作成
botan = tkinter.Button(window, text="追加" , command = tuika)
botan.place(x=150,y=10) #ボタンを配置する位置の設定

window.mainloop()
