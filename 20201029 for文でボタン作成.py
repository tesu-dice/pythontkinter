"""
ubf-8    20201029
for文でボタンたくさん
"""
import tkinter
window = tkinter.Tk()
window.geometry("600x400")
window.title("for文でボタンたくさん")

def botan_click():
    print("ボタンが押されました")

for i in range(10) :
    # ボタンの作成
    botan1 = tkinter.Button(window, text='ボタン', command = botan_click)
    botan1.place(x=i * 10,y= i *20) #ボタンを配置する位置の設定

window.mainloop()
