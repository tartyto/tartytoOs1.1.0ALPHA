from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import colorchooser
from playsound import playsound
import os

def donothing():
    print("nothing")
def exitE():
    f = messagebox.askyesno("turn off", "do you really want to turn off?")
    if f:
        root.destroy()
        exit()
    elif not f:
        messagebox.showinfo("ok", "continue your sesion on tartyto os ;)")

root = Tk()
root.config(background="light blue")
root.title("tartyto os 1.1.0")
root.geometry("1920x1920")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
def about():
    ab = Tk()
    ab.geometry("330x110")
    ab.configure(background="blue")
    ab.title("about tartyto os 1.1.0")
    def abo():
            f = messagebox.showinfo("about tartyto os 1.1.0", "tartyto os 1.1.0 info:\nversion: 1.1.0 alpha python 3 tkinter\nend of support: 31th of December 2020")
    b = Button(ab, text="TARTYTO OS\n1.1.0", bg="light blue", command=abo).grid(row=1, column=1)
    l1 = Label(ab, text="data:\n230mb / 23TS\n200mb RAM / 20TS RAM\nUsed space:\n80mb / 8TS\nos space:\n6kb / 0,0006TS", bg="blue", fg="white").place(x=120, y=2)

def appm():
    ap = Tk()
    ap.configure(background="light yellow")
    ap.title("app manager")
    ap.geometry("400x300")
    b1 = Button(ap, text="app manager", command = appm).place(x=2, y=2)
    l1 = Label(ap, text="data:\nweight: 28mb\ncopyright: tartyto soft 2019", bg="light yellow").place(x=120, y=2)
    b2 = Button(ap, text="Tartyto\nDocument\nFundation\nwriter", command = tdf).place(x=2, y=35)
    l2 = Label(ap, text="data:\nweight: 39mb\ncopyright: tartyto soft 2019", bg="light yellow").place(x=120, y=50)
    b3 = Button(ap, text="About Tartyto\nOs.t", command = about).place(x=2, y=120)
    l3 = Label(ap, text="data:\nweight: 13mb\nlocation:\n/sys/prog/tarc/about/About\\ Tartyto\\ OS.t", bg="light yellow").place(x=120, y=110)

"""
IMPORTANTE:
TDF writer
"""

def tdf():
    top = Tk()
    top.title("TDF writer")
    E1 = Text(top)
    E1.pack()
    def crt():
        top.filename =  filedialog.asksaveasfilename(initialdir = "/ArchiveName.tdfw",title = "Select file",filetypes = (("TDF writer document","*.tdfw"),("text document","*.txt"),("all files","*.*")))
        lol = E1.get("1.0", "end-1c")
        tf = top.filename
        if not tf == ():
        
            f = open(tf, "w")
            f.write(lol)
            f.close()
    b1 = Button(top, text="create", fg="green", command=crt).pack()
    def tdfsal():
        f = messagebox.askyesnocancel("save changes", "do you want to save changes")
        if f == True:
            crt()
            top.destroy()
        if f == False:
            top.destroy()
    b2 = Button(top, text="exit", fg="red", command = tdfsal).pack()
    """
    tmenubar = Menu(top)
    tfilemenu = Menu(tmenubar, tearoff = 0)
    tfilemenu.add_command(label = "save as...", command = crt)
    tfilemenu.add_separator()
    tfilemenu.add_command(label = "exit", command = tdfsal)
    top.config(menu = tmenubar)
    top.mainloop()
    """
def ArcMan():
    ar = Tk()
    ar.title("ArcMan 1.1.0")
    ar.iconify()

    ar.filename =  filedialog.askopenfilename(title = "tartyto ARChive MANager \"v = 1.1.0\"", filetypes = (("select a archive to open","*.*"),("select a python archive to ejecute","*.py")))

    tf = ar.filename
    if tf.endswith(".gif"):
        i = PhotoImage(file=tf)
        l1 = Label(ar, image=i).pack()
    elif tf.endswith(".mp3"):
        l1 = Label(ar, text="playing...", fg="blue").pack()
        def pl():
            playsound(tf)
            ar.destroy()
        ar.after(1000, lambda: pl())
    elif tf.endswith(".wav"):
        l1 = Label(ar, text="playing...", fg="blue").pack()
        def pl():
            playsound(tf)
            ar.destroy()
        ar.after(1000, lambda: pl())
    elif tf.endswith(".py"):
        com = "python3" + " " + tf
        os.system(com)
        ar.configure(bg="#8cd3cb")
        l2 = Label(ar, text=":(\nerror launching the shell", fg="white", bg="#8cd3cb").place(x=10, y=10)
    else:
        ar.configure(bg="#8cd3cb")
        l3 = Label(ar, text=":(\ncan't open the file:\nunknow file extension", fg="white", bg="#8cd3cb").place(x=10, y=10)
    ar.deiconify()
filemenu.add_command(label = "app manager", command = appm)
filemenu.add_command(label = "ArcMan file manager", command = ArcMan)
filemenu.add_command(label = "TDF Writer", command = tdf)
filemenu.add_command(label = "about tartyto os", command = about)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = exitE)
menubar.add_cascade(label = "START", menu = filemenu)
def CBC():
    def Cbc():
        f = colorchooser.askcolor(title="Change Background Color", initialcolor="light blue")
        r = str(f)
        s = r.find("#")
        e = (len(r) - 2)
        d = r[s:e]
        root.configure(bg=d)

    """
    c = Tk()
    c.geometry("400x400")
    c.title("Desktop properties")
    b1 = Button(c, text="Change Background\nColor", bg="light green", command=Cbc).grid(row=0, column=0)
    """
    Cbc()
def CBCL():

    root.after(100, lambda: root.configure(bg="blue"))
    root.after(200, lambda: root.configure(bg="light blue"))
    root.after(300, lambda: root.configure(bg="light green"))
    root.after(400, lambda: root.configure(bg="green"))
    root.after(500, lambda: root.configure(bg="yellow"))
    root.after(600, lambda: root.configure(bg="light yellow"))
    root.after(700, lambda: root.configure(bg="light blue"))
    root.after(800, lambda: root.configure(bg="blue"))
    root.after(900, lambda: root.configure(bg="light blue"))
    root.after(1000, lambda: root.configure(bg="light green"))
    root.after(1100, lambda: root.configure(bg="green"))
    root.after(1200, lambda: root.configure(bg="yellow"))
    root.after(1300, lambda: root.configure(bg="light yellow"))
    root.after(1400, lambda: root.configure(bg="light blue"))
    root.after(1500, lambda: root.configure(bg="blue"))
    root.after(1600, lambda: root.configure(bg="light blue"))
    root.after(1700, lambda: root.configure(bg="light green"))
    root.after(1800, lambda: root.configure(bg="green"))
    root.after(1900, lambda: root.configure(bg="yellow"))
    root.after(2000, lambda: root.configure(bg="light yellow"))
    root.after(2100, lambda: root.configure(bg="light blue"))
    
root.config(menu = menubar)
root.bind("<Button-3>", lambda e: CBC())
root.bind("<Double-1>", lambda e: CBCL())
root.mainloop()
