from random import randint
from tkinter import Button, Entry, Label, Tk, mainloop

def attempt():
    att = int(t_attempt.get())
    if att == goal:
        l_res['text'] = 'Молодець! Вгадав'
    elif att > goal:
        l_res['text'] += f'\nПереборщив! {att} — завелике'
    else:
        l_res['text'] += f'\nНедобрав! {att} — замале'

goal = randint(1, 100)

win = Tk()
win.geometry('300x300')

l_hello = Label(win, text='Вгадай число від 1 до 100')
l_hello.place(relx=0.5, rely=0.2, anchor='center')

t_attempt = Entry(win, width=10)
t_attempt.place(relx=0.25, rely=0.3, anchor='center')

b_attempt = Button(win, text='Спробувати', width=15, command=attempt)
b_attempt.place(relx=0.75, rely=0.3, anchor='center')

l_res = Label(win, text='Не бійся, не вкушу!')
l_res.place(relx=0.5, rely=0.4, anchor='n')

mainloop()