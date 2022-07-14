from tkinter import *
from tkinter import messagebox
import os

def save():
    if not os.path.exists('remembers.txt'):
        file = open ('members.txt' , 'a')
    x = txt.get()
    y=x+'\n'
    file.write(y)
    txt.delete(0 , 'end')
    txt.focus()


def exit():
    z = messagebox.askokcancel("Ok Cancel","آیا مطمئنی؟")
    if z:
        win1.destroy()



win1 = Tk()
win1.title('login')
win1.geometry('300x230+500+100')
win1.config(bg='green')

txt = Entry(justify='center' , font=('tahoma',14))
txt.focus()
txt.place(x=25 , y= 15 , width = 250 , height = 40)

btn_save=Button(win1 , text='Save' ,command=save)
btn_save.place(x=25 , y= 110 , width = 250 , height = 40)

btn_exit=Button(win1 , text='Exit' , command=exit)
btn_exit.place(x=25 , y= 160 , width = 250 , height = 40)

win1.mainloop()