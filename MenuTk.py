from tkinter import *

root = Tk()
menu = Menu(root)

root.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='new')
filemenu.add_command(label='open...')
filemenu.add_separator()
filemenu.add_command(label='exit', command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='help', menu=helpmenu)
helpmenu.add_cascade(label='about')

viewmenu = Menu(menu)
menu.add_cascade(label='view', menu=viewmenu)
viewmenu.add_command(label='tool windows')
viewmenu.add_command(label='Appereance')
viewmenu.add_separator()
viewmenu.add_command(label='Quick Definition')
viewmenu.add_command(label='Quick Type Definition')
viewmenu.add_command(label='Parameter Info')
viewmenu.add_command(label='Type Info')
viewmenu.add_command(label='Context Info')
mainloop()
