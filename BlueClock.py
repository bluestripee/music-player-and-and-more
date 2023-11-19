from tkinter import *
from ttkbootstrap import Style
from time import strftime
import tkinter as tk

root=Tk()
root.title('Time')
style = Style(theme='solar')

def time():
    string = strftime('%H:%M:%S')
    tik.config(text=string)
    tik.after(1000, time)

tik = tk.Label(root, font=('Arial', 80, "bold"), text = '')
tik.pack(anchor='center')
time()

mainloop()
