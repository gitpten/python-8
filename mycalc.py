from tkinter import Button, Entry, Label, Tk, mainloop

def plus():
    num1 = float(t_num1.get())
    num2 = float(t_num2.get())
    l_res['text'] = f"= {num1 + num2}"

def min():
    num1 = float(t_num1.get())
    num2 = float(t_num2.get())
    l_res['text'] = f"= {num1 - num2}"

def mult():
    num1 = float(t_num1.get())
    num2 = float(t_num2.get())
    l_res['text'] = f"= {num1 * num2}"

def div():
    num1 = float(t_num1.get())
    num2 = float(t_num2.get())
    l_res['text'] = f"= {num1 / num2}"


win = Tk()
win.geometry('500x300')

t_num1 = Entry(win, font=('Arial', 14))
t_num1.place(relx=0.2, rely=0.5, relwidth=0.2, anchor='center')

t_num2 = Entry(win, font=('Arial', 14))
t_num2.place(relx=0.6, rely=0.5, relwidth=0.2, anchor='center')

l_res = Label(win, font=('Arial', 14), text='=', anchor='center')
l_res.place(relx=0.8, rely=0.5, anchor='center')

b_plus = Button(win, text='+', command=plus, anchor='center')
b_plus.place(relx=0.4, rely=0.3, anchor='center', width='20')

b_min = Button(win, text='-', command=min, anchor='center')
b_min.place(relx=0.4, rely=0.4, anchor='center', width='20')

b_mult = Button(win, text='*', command=mult, anchor='center')
b_mult.place(relx=0.4, rely=0.5, anchor='center', width='20')

b_div = Button(win, text='/', command=div, anchor='center')
b_div.place(relx=0.4, rely=0.6, anchor='center', width='20')

mainloop()