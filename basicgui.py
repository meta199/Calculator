from tkinter import *

GUI = Tk()
GUI.title('Hello World')
GUI.geometry('500x500')

L1 = Label(GUI, text='Hello Meta', font=(None, 20))
L1.pack()

L2 = Label(GUI, text='Hello Roger', font=(None, 20))
L2.pack()

GUI.mainloop()