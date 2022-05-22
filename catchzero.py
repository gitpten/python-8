from time import sleep
from tkinter import Button, Label, Tk, mainloop

def catch():
    global running, time
    running = False
    res = int(cather["text"])
    if res == 0:
        time /= 2
    
    cather['text'] = 20
    info['text'] = f'Твій результат — {res}'

def start():
    global running
    running = True
    while running:
        num = int(cather['text'])
        num -= 1
        cather['text'] = f'{num}'
        win.update()
        sleep(time)

win = Tk()
win.geometry('300x300')

info = Label(win, text='Злови нуль!')
info.place(relx=0.2, rely=0.1, anchor='w')

cather = Button(win, text='10', command=catch)
cather.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor='center')

starter = Button(win, text='Go!', command=start)
starter.place(relx=0.8, rely=0.1, relwidth=0.2, relheight=0.1, anchor='center')

running = True
time = 0.2

mainloop()