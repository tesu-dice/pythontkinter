"""
utf-8    20210424
import time で起動してからの時間を測る

"""
import tkinter as tk
import time

window =tk.Tk()
window.geometry("600x400")
window.title("起動後の経過時間")

time_l = tk.Label(font=("游ゴシック",20))
time_l.place(x=50,y=10)

time_la = tk.Label(font=("游ゴシック",20))
time_la.place(x=50,y=100)

start = time.time()

def update():
    timer = time.time() - start
    time_l["text"] = timer
    time_la["text"] = timer//1
    window.after(10,update)
update()
window.mainloop()
  