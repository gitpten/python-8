from random import choice
from tkinter import Button, Label, Tk, mainloop

def rock():
    winner('камінь')

def knife():
    winner('ножиці')

def paper():
    winner('папір')

def winner(player):
    bot = choice(['камінь', 'ножиці', 'папір'])
    if player == bot:
        info['text'] = f'Бот поклав {bot}\n Нічия!'
    elif (player == 'камінь' and bot == 'ножиці') or \
         (player == 'ножиці' and bot == 'папір') or \
             (player == 'папір' and bot == 'камінь'):
        info['text'] = f'Бот поклав {bot}\n Ти виграв!!!'
    else:
        info['text'] = f'Бот поклав {bot}\n Ти програв...'


win = Tk()
win.geometry("500x300")

info = Label(win, font="Consolas 12", text="Камінь, ножиці, папір! 1-2-3!")
info.place(relx=0.5, rely=0.2, anchor='center')

b_rock = Button(win, text='камінь', command=rock)
b_rock.place(relx=0.25, rely=0.6, width=100, height=50, anchor='center')

b_knife = Button(win, text='ножиці', command=knife)
b_knife.place(relx=0.5, rely=0.6, width=100, height=50, anchor='center')

b_paper = Button(win, text='папір', command=paper)
b_paper.place(relx=0.75, rely=0.6, width=100, height=50, anchor='center')

mainloop()