import tkinter

def Messagebox():
    main = tkinter.Tk()
    lbl = tkinter.Label(main, text="LOGIN SUCCESFULLY!", anchor='e')
    lbl.grid(column=0, row=0)
    
def Messagebox1():
    main = tkinter.Tk()
    lbl = tkinter.Label(main, text="INVALID LOGIN!", anchor='e')
    lbl.grid(column=0, row=0)

window = tkinter.Tk()
window.title("FORM LOGIN.co.id")
window.geometry('340x440')
window.configure(bg='#333333')

def login():
    username = "KELOMPOK4"
    password = "123456789"
    if username_entry.get()==username and password_entry.get()==password:
        Messagebox()
    else:
        Messagebox1()

frame = tkinter.Frame(bg='#333333')

logo = tkinter.PhotoImage(file="LOGO WEH.png")
logoo = tkinter.Label(frame, image=logo)

login_label = tkinter.Label(
    frame, text="FORUM LOG IN", bg='#333333', fg="#FF3399", font=("Aial", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Aial", 16))
username_entry = tkinter.Entry(frame, font=("Aial", 16))
password_entry = tkinter.Entry(frame,    show="*", font=("Aial", 16))
password_label = tkinter.Label(
    frame, text="Password",bg='#333333', fg="#FFFFFF", font=("Aial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Aial", 16), command=login)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)
logoo.grid(row=5, column=1)

frame.pack()

window.mainloop()
