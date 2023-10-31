from tkinter import *

main = Tk()
ourmessage = "tulis pesan disini"
messageVar = Message(main, text= ourmessage)
messageVar.config(bg='lightgreen')
messageVar.pack()
mainloop()