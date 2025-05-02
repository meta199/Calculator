from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('Hello World')
GUI.geometry('500x500')

L1 = Label(GUI, text='Hello Meta', font=(None, 20))
L1.pack()

L2 = Label(GUI, text='Hello Roger', font=(None, 20))
L2.pack()

v1 = StringVar()
E1 = ttk.Entry(GUI, textvariable=v1)
E1.pack()

v2 = StringVar()
E2 = ttk.Entry(GUI, textvariable=v2)
E2.pack()

def cal():
    print(c := float(v1.get()) * float(v2.get()))
    text = f'{v1.get()}x{v2.get()}={c}'
    messagebox.showinfo('Result', text)

b1 = ttk.Button(GUI, text='Calcurate Now', command=cal)
b1.pack()

GUI.mainloop()