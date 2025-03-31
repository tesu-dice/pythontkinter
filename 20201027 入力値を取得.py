"""
ubf-8      20201027
ウィンドウで入力値を取得
"""
import tkinter          #tkinterインポート
#ウィンドウ設定
uxindou = tkinter.Tk()     #uxindouという名のウィンドウを作成
uxindou.geometry("500x400")          #サイズ設定
uxindou.title("ウィンドウで入力値を取得")         #タイトル設定

#ボタンクリックでの処理
koumoku = []
bikou = []
list=[]
def botan_click():
    print("メッセージ:入力してください　（項目と備考でスペース一つあける）")       #個々の処理はコマンドプロンプトで行う
    word = input()
    print("入力された文字：" + word)
    word = word.split()
    print(word[0])
    print(word[1])
    koumoku.append(str(word[0]))
    bikou.append(str(word[1]))
    print(koumoku)
    print(bikou)
    #リストで項目と備考を表示
    for i in range(len(koumoku)):
        if i == 0 :
            list = koumoku[i] + "  " + bikou[i] + "\n"
        elif i > 0 :
            list = list + koumoku[i] + "  " + bikou[i] + "\n"
        print(list)
    chart = tkinter.Label(uxindou , text=list , font=("游ゴシック" , 20))
    chart.place(x=10,y=100)






# ボタンの作成
botan = tkinter.Button(uxindou , text='入力してください', command = botan_click)
botan.place(x=10,y=10) #ボタンを配置する位置の設定

#説明文の設定
moji1 = tkinter.Label(uxindou , text="ボタンを押して入力しましょう\n"  + "コマンドプロンプトで入力してください", font=("游ゴシック", 10))
moji1.place(x=10, y=50)

uxindou.mainloop()
