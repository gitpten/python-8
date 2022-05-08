from random import randint
from time import sleep
from tkinter import Button, Tk, mainloop


def door1_open():
    open(0)

def door2_open():
    open(1)

def door3_open():
    open(2)

def open(user):
    ghost = randint(0, 2)
    door = doors[user]
    door['font'] = 'Wingdings 30'
    if user == ghost:
        door['text'] = "N"
        return
    else:
        door['text'] = "J"
    
    win.update()

    sleep(1)
    reset()

def reset():
    door1['font'] = 'Arial 30' 
    door1['text'] = 1
    door2['font'] = 'Arial 30' 
    door2['text'] = 2
    door3['font'] = 'Arial 30' 
    door3['text'] = 3



win = Tk()
win.geometry("500x300")

door1 = Button(win, text='1', font='Arial 30', command=door1_open)
door1.place(relx=0.25, rely=0.5, width=50, height=100, anchor='center')

door2 = Button(win, text='2', font='Arial 30', command=door2_open)
door2.place(relx=0.5, rely=0.5, width=50, height=100, anchor='center')

door3 = Button(win, text='3', font='Arial 30', command=door3_open)
door3.place(relx=0.75, rely=0.5, width=50, height=100, anchor='center')

doors = [door1, door2, door3]

mainloop()