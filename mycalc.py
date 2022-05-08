from tkinter import Button, Entry, Label, Tk, mainloop


def plus():
    num1 = float(t_num1.get())
    num2 = float(t_num2.get())
    l_res['text'] = f'= {num1 + num2}'

def div():
    num1 = float(t_num1.get())
    num2 = float(t_num2.get())
    l_res['text'] = f'= {num1 / num2: .5f}'

win = Tk()
win.geometry('500x300')

t_num1 = Entry(win, width=15)
t_num1.place(relx = 1 / 5, rely = 1 / 2, anchor='center')

t_num2 = Entry(win, width=15)
t_num2.place(relx = 0.6, rely = 0.5, anchor='center')

b_plus = Button(win, text='+', command=plus)
b_plus.place(relx=0.4, rely=0.45, width=20, anchor='center')

b_div = Button(win, text='/', command=div)
b_div.place(relx=0.4, rely=0.55, width=20, anchor='center')

l_res = Label(win, text='= ?')
l_res.place(relx=0.8, rely=0.5, anchor='center')





mainloop()