from time import sleep
from tkinter import Button, Label, Tk, mainloop

def catch():
    global run, delay
    run = False
    res = int(catcher['text'])
    
    if res == 0:
        info['text'] = "О! Ти справний! Давай швидше"
        delay /= 2
    else:
        info['text'] = f"Твій результат — {res}"

    catcher['text'] = 20

def start():
    global run
    run = True
    while run:
        num = int(catcher['text'])
        num -= 1
        catcher['text'] = num
        win.update()
        sleep(delay)

win = Tk()
win.geometry("300x300")

info = Label(win, text='Спіймай нуль!')
info.place(relx=0.1, rely=0.1, anchor='w')

catcher = Button(win, text='20', command=catch)
catcher.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor='center')

starter = Button(win, text='Go!', command=start)
starter.place(relx=0.8, rely=0.1, relwidth=0.2, relheight=0.1, anchor='center')

run = True
delay = 0.2

mainloop()