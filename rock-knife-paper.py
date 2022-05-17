from multiprocessing import Event
from random import choice
from tkinter import Button, Label, Tk, mainloop


def checkwinner(event: Event):
    bot = choice(FIGURES)
    player = event.widget['text']
    if WINNERS[player] == bot:
            info['text'] = f"{bot}. You are win"
    elif player == bot:
        info['text'] = f"{bot}. There is draw"
    else:
        info['text'] = f"{bot}. You are loose"

FIGURES = ['камень', 'ножницы', 'бумага']
WINNERS = {
    'камень': 'ножницы',
    'ножницы': 'бумага',
    'бумага': 'камень',
}

win = Tk()
win.geometry('500x300')


buttons = []

info = Label(win, font='Verdana 15', text='Choose what throw you')
info.place(relx=0.5, rely=0.1, anchor='center')

pos = 1 / (len(FIGURES) + 1)
for f in FIGURES:
    b = Button(win, text=f, font='Verdana 15')
    b.place(relx=pos, rely=0.5, width=100, height=50, anchor='center')
    b.bind("<Button-1>", checkwinner)
    buttons.append(b)
    pos += 1 / (len(FIGURES) + 1)



mainloop()