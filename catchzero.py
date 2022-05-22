from time import sleep
from tkinter import Button, Tk, mainloop

def catch():
    global running
    running = False

win = Tk()
win.geometry('300x300')

cather = Button(win, text='10', command=catch)
cather.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor='center')

running = True
while running:
    num = int(cather['text'])
    num -= 1
    cather['text'] = f'{num}'
    win.update()
    sleep(0.1)

mainloop()