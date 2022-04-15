from tkinter import Button, Entry, Label, Tk, mainloop

def answer():
    answ = t_answ.get()
    l_phrase['text'] = f'Всі кажуть {answ}, а ти придбай слона!'
    t_answ.delete(0, 'end')

win = Tk()
win.geometry('500x500')

l_phrase = Label(win, font=('Arial', 14), text='— Привіт, придбай слона!')
l_phrase.place(relx=0.5, rely=0.2, anchor='center')

l_answ = Label(win, font=('Arial', 14), text='Відповідь: ')
l_answ.place(relx=0.2, rely=0.6)

t_answ = Entry(win, font=('Arial', 14))
t_answ.place(relx=0.5, rely=0.6, relwidth=0.25)

b_answ = Button(win, text='Відповісти', command=answer)
b_answ.place(relx=0.5, rely=0.8, anchor='center')

mainloop()