from tkinter import *
from tkinter import PhotoImage

lo = Tk()
lo.geometry("1920x1920")
p = PhotoImage(file="T/Data/SistemData/STos/Bg/LoginScreen/login.gif")

bkg = Label(lo, image=p).place(x=0, y=0)

from tkinter import PhotoImage

b = PhotoImage(file="T/Data/SistemData/STos/Bg/B/Logi.gif")
bkg2 = Label(lo, image=b, bg="light blue").place(x=800, y=400)
ch = Button(lo, text="Login in", bg="#00D6FF")
ps = StringVar()
pw = Entry(lo, fg="#0080FF", show="*", width=13, textvariable=ps)
def chc():
    d = ps.get()
    print(d)
    if d == "password":
        pw.config(fg="green")
    else:
        pw.config(fg="red")
        pw.after(2000, lambda: pw.config(fg="#0080FF"))

ch.config(command = chc)
ch.place(x=1100, y=590)
pw.place(x=1080, y=570)
