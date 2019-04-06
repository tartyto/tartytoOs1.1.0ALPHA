from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import colorchooser
from playsound import playsound
from random import randint
import os

main = Tk()
main.geometry("430x500")
main.configure(cursor="arrow")
main.title("Launcher")
lx = Listbox(main, width=30, height=30) 
lx.insert(0, "Tartyto os \"v=1.1.0\"")
lx.insert(1, "Tartyto os Helper \"v=1.1.0\"")
lx.grid(row=1, column=0)
i = PhotoImage(file="Launcher_Data/Start.gif")
ima = PhotoImage(file="Launcher_Data/2699.gif")
def TosStart():
    main.configure(cursor="watch")
    def TosStart2():
        main.configure(cursor="arrow")
        def TosStart3():
            main.configure(cursor="watch")
            def TosStart4():
                main.configure(cursor="arrow")
                main.destroy()
                def ReallyStart():
                    def exitE():
                        playsound("T/Data/SistemData/STos/Snds/Shutdown.mp3")
                        root.destroy()
                        exit()
                    def reboot():
                            playsound("T/Data/SistemData/STos/Snds/Shutdown.mp3")
                            root.iconify()
                            def RBoot():
                                root.destroy()
                                ReallyStart()
                            pt = randint(2000, 4000)
                            root.after(pt, lambda: RBoot())

                    root = Tk()
                    root.config(background="light blue")
                    root.title("tartyto os 1.1.0")
                    root.geometry("1920x1920")
                    def Tsea():
                        ts = Tk()
                        ts.geometry("400x400")
                        ts.title("T searcher")
                        sv = StringVar()
                        
                        E = Entry(ts, width=40, textvariable=sv).grid(row=0, column=0)
                        B = Button(ts, text="Search").grid(row=0, column=1)
                    menubar = Menu(root)
                    filemenu = Menu(menubar, tearoff = 0)
                    exitmenu = Menu(filemenu, tearoff = 0)
                    def about():
                        ab = Tk()
                        ab.geometry("330x110")
                        ab.configure(background="blue")
                        ab.title("about tartyto os 1.1.0")
                        def abo():
                                f = messagebox.showinfo("about tartyto os 1.1.0", "tartyto os 1.1.0 info:\nversion: 1.1.0 alpha python 3 tkinter\nend of support: 31th of December 2020")
                        b = Button(ab, text="TARTYTO OS\n1.1.0", bg="light blue", command=abo).grid(row=1, column=1)
                        l1 = Label(ab, text="data:\nUsed space:\n80mb / 8TS\nOS weight:\n13kb / 0,0013TS", bg="blue", fg="white").place(x=120, y=2)

                    def appm():
                        ap = Tk()
                        ap.configure(background="light yellow")
                        ap.title("app manager")
                        ap.geometry("400x300")
                        b1 = Button(ap, text="app manager", command = appm).grid(row=0, column=0)
                        l1 = Label(ap, text="data:\nweight: kb\n", bg="light yellow").grid(row=0, column=1)
                        b2 = Button(ap, text="Tartyto\nDocument\nFundation\nwriter", command = tdf).grid(row=1, column=0)
                        l2 = Label(ap, text="data:\nweight: kb\n", bg="light yellow").grid(row=1, column=1)
                        b3 = Button(ap, text="About Tartyto\nOs", command = about).grid(row=2, column=0)
                        l3 = Label(ap, text="data:\nweight: kb\n", bg="light yellow").grid(row=2, column=1)
                        b4 = Button(ap, text="Arc Man", bg="light yellow", command = ArcMan).grid(row=3, column=0)
                        l4 = Label(ap, text="data:\nweight: kb\n", bg="light yellow").grid(row=3, column=1)

                    """
                    IMPORTANTE:
                    TDF writer
                    """

                    def tdf():
                        top = Tk()
                        top.title("TDF writer")
                        
                        def crt():
                            top.filename =  filedialog.asksaveasfilename(initialdir = "/ArchiveName.tdfw",title = "Select file",filetypes = (("TDF writer document","*.tdfw"),("text document","*.txt"),("all files","*.*")))
                            lol = E1.get("1.0", "end-1c")
                            tf = top.filename
                            if not tf == ():
                                print("")

                        def tdfsal():
                            f = messagebox.askyesnocancel("save changes", "do you want to save changes")
                            if f == True:
                                crt()
                                top.destroy()
                            if f == False:
                                top.destroy()
                                f = open(tf, "w")
                                f.write(lol)
                                f.close()
                                
                        scroll = Scrollbar(top)
                        
                        E1 = Text(top, yscrollcommand= scroll.set)
                        E1.pack(side=LEFT)
                        
                        b1 = Button(top, text="Save as...", bd=5, fg="green", command = crt)
                        b2 = Button(top, text="Exit", bd=5, fg="red", command = tdfsal)
                        b1.pack(side=TOP)
                        b2.pack(side=TOP)
                        scroll.pack(side=RIGHT, fill=Y)

                        scroll.config(command=E1.yview)
                        
                        
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

                    filemenu.add_cascade(label = "Shut Down...", menu = exitmenu)

                    exitmenu.add_command(label = "Shut Down", command = exitE)
                    exitmenu.add_command(label = "Reboot", command = reboot)
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
                    root.bind("<Button-2>", lambda e: CBCL())
                    root.after(1, lambda: playsound("T/Data/SistemData/STos/Snds/startup.mp3"))
                    root.mainloop()
                lo = Tk()
                lo.title("login in")
                lo.geometry("1920x1920")
                fdsa = PhotoImage(file="T/Data/SistemData/STos/Bg/LoginScreen/login.gif")
                
                bkg = Label(lo, image=fdsa).place(x=0, y=0)
                
                asdf = PhotoImage(file="T/Data/SistemData/STos/Bg/B/Logi.gif")
                bkg2 = Label(lo, image=asdf, bg="light blue").place(x=800, y=400)
                ch = Button(lo, text="Login in", bg="#00D6FF")
                ps = StringVar()
                pw = Entry(lo, fg="#0080FF", show="*", width=30, textvariable=ps)
                def chc():
                    d = ps.get()
                    try:
                        h = open("T/Data/SistemData/INI/psw/pswrd.txt", "r")
                        f = h.read()
                        h.close()
                        if d == f:
                            pw.config(fg="green")
                            pw.after(2000, lambda: ReallyStart())
                            pw.after(2001, lambda: lo.destroy())
                            
                        else:
                            pw.config(fg="red")
                            pw.after(2000, lambda: pw.config(fg="#0080FF"))
                    except FileNotFoundError:
                        lo.destroy()
                        err = Tk()
                        err.title("ERROR")
                        img = PhotoImage(file="Launcher_Data/BSod.gif")
                        er = Label(err, image=img).pack()
                        err.mainloop()

                ch.config(command = chc)
                ch.place(x=1020, y=520)
                pw.place(x=940, y=500)
                lo.mainloop()
            main.after(3000, lambda: TosStart4())
        main.after(500, lambda: TosStart3())
    main.after(2000, lambda: TosStart2())

def HelpDoc():
    main.config(cursor="arrow")
    doc = Tk()
    doc.title("Help Documents")

    sc = Scrollbar(doc)
    sc.pack(side=RIGHT, fill=Y)
    T = Text(doc, yscrollcommand= sc.set)
    sc.config(command=T.yview)
    f = ("#######################\n"
         "Tartyto os 1.1.0 helper\n"
         "#####################\n\n"

         "1. app manager:\n"
         "  This is an app where\n"
         "  you can see data about\n"
         "  the other apps\n\n"

         "2. Arc Man:\n"
         "  Arc Man is an\n"
         "  ARChive MANager\n"
         "  where you can see the\n"
         "  files of your real\n"
         "  computer\n\n"

         "  is a good way to have\n"
         "  shared folders with the\n"
         "  emulated system\n\n"

         "3. TDF writer:\n"
         "  Is a document creator\n"
         "  where you can create\n"
         "  text documents\n\n"

         "4. about:\n"
         "  Is interesant to now\n"
         "  about the system that\n"
         "  you use\n\n"

         "5. Easter eggs:\n"
         "  There are some easter\n"
         "  eggs\n"
         "  find them!\n")
         
    T.insert("1.0", f)
    T.config(state="disabled")
    T.pack()
    doc.mainloop()
def StartALL():
    a = lx.curselection()
    f = a[0]
    if f == 0:
        TosStart()
    elif f == 1:
        main.config(cursor="watch")
        main.after(2000, HelpDoc())
b = Button(main, image=i, state="disabled", command = StartALL)
b.place(x=310, y=10)
def f():
    b.config(state="normal")
lx.bind("<<ListboxSelect>>", lambda e: f())
main.mainloop()
