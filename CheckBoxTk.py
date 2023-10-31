from tkinter import *
master = Tk()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
Checkbutton(master, text="MALE", variable=var1).grid(row= 0, sticky=W)
Checkbutton(master, text="FEMALE", variable=var2).grid(row= 1, sticky=W)
Checkbutton(master, text="I'M MECHANIC", variable=var3).grid(row= 2, sticky=W)
mainloop()