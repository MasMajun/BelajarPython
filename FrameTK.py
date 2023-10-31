from tkinter import *
root = Tk()

frame = Frame(root)
frame.pack()
buttonFrame = Frame(root)
buttonFrame.pack(side=BOTTOM)
redbutton = Button(frame,text='RED', fg='RED')
redbutton.pack(side=LEFT)

bluebutton = Button(frame,text='BLUE', fg='BLUE')
bluebutton.pack(side=LEFT)

greenbutton = Button(frame,text='GREEN', fg='GREEN')
greenbutton.pack(side=LEFT)

blackbutton = Button(frame,text='BLACK', fg='BLACK')
blackbutton.pack(side=LEFT)
root.mainloop()



