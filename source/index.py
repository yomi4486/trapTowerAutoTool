import tkinter as tk
import tkinter.font
import time
import threading
import pyautogui
import sys,keyboard

auto_clicking = False

def exit_all():
    sys.exit()

def auto_click():
    global auto_clicking
    time.sleep(3)
    while auto_clicking:
        pyautogui.click()
        time.sleep(var.get())
def esc_to_exit():
    global auto_clicking
    while True:
        time.sleep(0.5)
        if keyboard.is_pressed('escape'):
            auto_clicking = False
            
            button.config(text="放置を開始")
def update_countdown(count):
    if count > 0:
        button.config(text=str(count))
        window.after(1000, update_countdown, count - 1)
    else:
        button.config(text="停止")

def start_countdown():
    update_countdown(3)

def click_start():
    global auto_clicking
    if not auto_clicking:
        auto_clicking = True
        start_countdown()
        auto_click_thread = threading.Thread(target=auto_click)
        auto_click_thread.start()
        esc_to_exit_thread = threading.Thread(target=esc_to_exit)
        esc_to_exit_thread.start()
        
    else:
        # Stop auto-clicking
        auto_clicking = False
        
        button.config(text="放置を開始")

# Create a GUI window
window = tk.Tk()
window.title("トラップタワー放置ツールv1")
window.geometry("400x120")
try:
    photo = tk.PhotoImage(file = "./data/icon.png")  
    window.iconphoto(False, photo)
except:
    pass
# Create a button
font = tkinter.font.Font(
    window,
    name="Helvetica",
    size=14,
    family="bold"
    
)

text = tk.Label(window, text="Escキー長押しで止めても構わない",font=font)

button = tk.Button(window, text="放置を開始", command=click_start)
var = tkinter.IntVar(window)
var.set(8)  #初期値

#スピンボックスの設定
s = tkinter.Spinbox(
    window,
    textvariable=var,   #変数
    from_=1,          #下限値
    to=99,              #上限値
    increment=1,        #増減ステップ
    )
sub_text = tk.Label(window, text="秒間隔で攻撃を行います")
s.place()
text.place(x=10,y=0)
s.place(x=10,y=40)
sub_text.place(x=45,y=38)
button.place(x=10,y=75)

window.mainloop()