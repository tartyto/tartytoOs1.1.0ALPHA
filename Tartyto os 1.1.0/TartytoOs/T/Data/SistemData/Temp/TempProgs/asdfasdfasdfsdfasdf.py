from tkinter import *

doc = Tk()

sc = Scrollbar(doc)
sc.pack(side=RIGHT, fill=Y)
T = Text(doc, yscrollcommand= sc.set)
sc.config(command=T.yview)
f = ("#####################\n"
     "Tartyto os 1.1.0 help\n"
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
