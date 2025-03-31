"""
ubf-8   2021116
リストの中の文字の最大数を取得
"""


import tkinter
#ウィンドウの設定
window = tkinter.Tk()
window.geometry("400x500")     #ウィンドウサイズ設定
window.title("チェックボックスのテキストリスト")      #ウィンドウのタイトル設定
check1 = tkinter.Checkbutton(window,text="あいうえお")
check1.place(x=10, y=10)
check2 = tkinter.Checkbutton(window,text="あいうえおかきくけこ")
check2.place(x=10, y=30)
check3 = tkinter.Checkbutton(window,text="あいうえおかきくけこさしすせそ")
check3.place(x=10, y=50)

word_list =[]
word_list.append(check1["text"])
print(word_list)
print()


window.mainloop()
