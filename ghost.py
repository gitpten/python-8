from random import randint
from time import sleep
from tkinter import Button, Label, Tk, mainloop


def open_door1():
    open_door(0)

def open_door2():
    open_door(1)

def open_door3():
    open_door(2)

def open_door(user):
    ghost = randint(0, 2)

    door = doors[user]
    door['font'] = 'Wingdings 30'
    if ghost == user:
        door['text'] = 'N'
        info['text'] = "— Ха-ха! Я тебе з'їв"
        return

    door['text'] = 'J'
    info['text'] = "— Пощастило! Але я до тебе доберуся"

    win.update()
    sleep(2)
    info['text'] = "— Я знову за однією з дверей! Пробуй ще."
    door['font'] = 'Arial 30'
    door['text'] = f'{user + 1}'

win = Tk()
win.geometry('500x300')

info = Label(win, font='Verdana 15', text='— У-у-у-у!\nЯ за однією з дверей! Дивись не наткнись!')
info.place(relx=0.5, rely=0.1, anchor='center')

door1 = Button(win, text='1', font='Verdana 30', command=open_door1)
door1.place(relx=0.25, rely=0.5, width=50, height=100, anchor='center')

door2 = Button(win, text='2', font='Verdana 30', command=open_door2)
door2.place(relx=0.5, rely=0.5, width=50, height=100, anchor='center')

door3 = Button(win, text='3', font='Verdana 30', command=open_door3)
door3.place(relx=0.75, rely=0.5, width=50, height=100, anchor='center')

doors = [door1, door2, door3]

mainloop()