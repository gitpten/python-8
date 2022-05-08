from tkinter import Button, Entry, Label, Tk, mainloop

def task1():
    w = int(t1_w.get())
    m = int(t1_m.get())
    y = int(t1_y.get())
    d = w * 7 + m * 30 + y * 12 * 30
    l1_res['text'] = f'{d} днів'

win = Tk()
win.geometry('500x700')

#week
l1_w = Label(win, text='2')
l1_w.place(relx=0.05, rely=0.05, anchor='center')
l1_w = Label(win, text='w')
l1_w.place(relx=0.1, rely=0.05, anchor='center')
t1_w = Entry(win, width=15)

#month
t1_w.place(relx = 0.3, rely = 0.05, anchor='center')
l1_m = Label(win, text='m')
l1_m.place(relx=0.1, rely=0.1, anchor='center')
t1_m = Entry(win, width=15)
t1_m.place(relx = 0.3, rely = 0.1, anchor='center')

#year
l1_y = Label(win, text='y')
l1_y.place(relx=0.1, rely=0.15, anchor='center')
t1_y = Entry(win, width=15)
t1_y.place(relx = 0.3, rely = 0.15, anchor='center')

#result
b1 = Button(win, text='→', command=task1)
b1.place(relx=0.5, rely=0.1, width=20, anchor='center')

l1_res = Label(win, text='= ?')
l1_res.place(relx=0.7, rely=0.1, anchor='center')

mainloop()
