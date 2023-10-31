from tkinter import *

layout = Tk()
scrollbar = Scrollbar(layout)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(layout, yscrollcommand=set)
for line in range(500):
    mylist.insert(END, 'List Data Ke'+ str(line))
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
mainloop()