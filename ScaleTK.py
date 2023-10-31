from tkinter import *

layout =Tk()
s = Scale(layout, from_=0, to=42)
s.pack
s = Scale(layout, from_=0, to=200, orient=HORIZONTAL)
s.pack()
mainloop()
