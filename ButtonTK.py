import tkinter as tk

r = tk.Tk()
r.title('Membuat Button Close')
button = tk.Button(r, text='BACOD POKE DIEM AJA', width=25, command=r.destroy)
button.pack()
r.mainloop()