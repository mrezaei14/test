from tkinter import *
from tkinter import messagebox
import os

from matplotlib.pyplot import close




win = Tk()
win.title('login')
win.geometry('300x230+500+100')
win.config(bg='blue')


def open_sign_up():
    os.system('py sign_up.py')

def sign_in():
    if not os.path.exists('members.txt'):
        file = open('members.txt' , 'w')
        close()
    x = txt.get()
    file = open('members.txt')
    y = file.readlines()
    d=False
    for i in y:
        if x == i.split('\n')[0]:
            messagebox.showinfo('Welcome' , 'Welcome')
            d=True
            break
    if d !=True:
        messagebox.showerror("","You must register first ")




txt = Entry()
txt.place(x=25 , y= 15 , width = 250 , height = 30)
btn_sign_in=Button(win , text='Sign In' , command=sign_in)
btn_sign_in.place(x=25 , y= 55 , width = 250 , height = 40)

btn_sign_up=Button(win , text='Sign UP' ,command=open_sign_up)
btn_sign_up.place(x=25 , y= 110 , width = 250 , height = 40)

btn_exit=Button(win , text='Exit')
btn_exit.place(x=25 , y= 160 , width = 250 , height = 40)


















win.mainloop()