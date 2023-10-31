from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Legend')
Lb.insert(2, 'Mythic')
Lb.insert(3, 'Mythic Honor')
Lb.insert(4, 'Mythic Glory')
Lb.insert(5, 'Mythic Immortal')
Lb.pack()
top.mainloop()