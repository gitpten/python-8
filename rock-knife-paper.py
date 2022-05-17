from random import choice
from tkinter import Button, Label, Tk, mainloop


def rock():
    checkwinner('камень')

def knife():
    checkwinner('ножницы')

def paper():
    checkwinner('бумага')

def checkwinner(player):
    bot = choice(['ножницы', 'бумага', 'камень'])
    if (player == 'ножницы' and bot == 'бумага') or \
        (player == 'бумага' and bot == 'камень') or \
            (player == 'камень' and bot == 'ножницы'):
            info['text'] = f"{bot}. You are win"
    elif player == bot:
        info['text'] = f"{bot}. There is draw"
    else:
        info['text'] = f"{bot}. You are loose"


win = Tk()
win.geometry('500x300')

info = Label(win, font='Verdana 15', text='Choose what throw you')
info.place(relx=0.5, rely=0.1, anchor='center')

b_rock = Button(win, text='камень', font='Verdana 15')
b_rock.place(relx=0.25, rely=0.5, width=100, height=50, anchor='center')

b_knife = Button(win, text='ножницы', font='Verdana 15')
b_knife.place(relx=0.5, rely=0.5, width=100, height=50, anchor='center')

b_paper = Button(win, text='бумага', font='Verdana 15')
b_paper.place(relx=0.75, rely=0.5, width=100, height=50, anchor='center')


mainloop()