from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

s = Tk()
s.config(bg="#cccccc")
s.geometry("500x480")
im = PhotoImage(file="setup_data/LFTsTp.gif")
l1 = Label(s, image=im)
ima = PhotoImage(file="setup_data/RGHgR.gif")
l2 = Label(s, image=ima, bd=0)


def install():
    l1.place_forget()
    l2.place_forget()
    b2.config(state="disabled")
    sc = Scrollbar(s)
    t = Text(s, yscrollcommand= sc.set)
    sc.config(command=t.yview)
    d = "###########\n  LICENSE  \n###########\n\ntartyto soft\nwants to give\nits users the\nbest experience\n\n############\n THANKS FOR\n  READING\n############\n"
    t.insert(1.0, d)
    t.config(state="disabled")

    iv = IntVar()
    def rc():
        a = iv.get()
        if a == 1:
            b2.config(state="active")
        if a == 0:
            b2.config(state="disabled")
    r1 = Radiobutton(s, text="I agree the license", variable=iv, value=1, command=rc, bg="#cccccc", bd=0)
    r2 = Radiobutton(s, text="I don't agree license", variable=iv, value=0, command=rc, bg="#cccccc", bd=0)
    def inst():
        b2.config(text="  > INSTALL >  ")
        sc.pack_forget()
        t.pack_forget()
        r1.place_forget()
        r2.place_forget()
        ll = Label(s, text="password for the system", bg="#cccccc")
        e = Entry(s, show="*")
        def instaLL():
            ll.grid_forget()
            e.grid_forget()
            b2.pack_forget()
            l3 = Label(s, text="Installing...", bg="#cccccc")
            pb = ttk.Progressbar(s, length=490, mode="indeterminate")
            def st():
                pb.start()
            def p():
                pb.stop()
            d = e.get()
            st()
            f = open("TartytoOs/T/Data/SistemData/INI/psw/pswrd.txt", "w")
            f.write(d)
            f.close()
            s.after(1679, lambda: p())
            def ind():
                l3.place_forget()
                pb.place_forget()
                l1.place(x=0, y=0)
                l5 = Label(s, text="The Tartyto os 1.1.0\ninstalation has\nfinished", bg="#cccccc").place(x=230, y=0)
                b2.place_forget()
                b1.config(text="finish")
                b1.config(command = lambda: s.destroy())
            s.after(1680, lambda: ind())
            pb.place(x=5, y=100)
            l3.place(x=5, y=5)
        
        ll.grid(row=0, column=0)
        e.grid(row=1, column=0)
        b2.config(command = instaLL)
    b2.config(command = inst)
    sc.pack(side=RIGHT, fill=Y)
    t.pack(side=RIGHT)
    r1.place(x=5, y=415)
    r2.place(x=5, y=435)
def canc():
    f = messagebox.askyesno(title="cancel", message="Do you want to cancel the instalation?")
    if f:
        s.destroy()

l1.place(x=0, y=0)
l2.place(x=230, y=0)
b1 = Button(s, text="cancel", command = canc)
b2 = Button(s, text=">>> next >>>", command = install)
b1.place(x=430, y=450)
b2.place(x=305, y=450)
s.mainloop()
