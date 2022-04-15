from tkinter import Button, Entry, Label, Tk, mainloop

def answer():
    answ = t_answ.get()
    l_phrase['text'] = f"Всі кажуть '{answ}', а ти придбай слона"

win = Tk()
win.geometry('500x300')

l_phrase = Label(win, text='— Придбай слона!')
l_phrase.place(relx=0.5, rely=0.2, anchor='center')

t_answ = Entry(win, width=50)
t_answ.place(relx=0.5, rely=0.6, anchor='center')

b_answ = Button(win, text='Відповісти', command=answer)
b_answ.place(relx=0.5, rely=0.7, anchor='center')

mainloop()