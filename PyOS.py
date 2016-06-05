from tkinter import *
from tkinter import ttk
import time
import os

root = Tk()
root.attributes("-fullscreen", True)
ctrlTestDir = StringVar()

def info():
    info = Toplevel()
    info["background"] = "#FFFF99"
    info.resizable(False, False)
    info.title("Info")
    info.geometry("250x150")

    l = Label(info, text = "PyOS 0.1 Alpha", font = ("Tahoma", 20))
    l["background"] = "#FFFF99"
    l.pack(side = "top")    

    l = Label(info, text = "Creato da: Niccolò Ciavarella")
    l["background"] = "#FFFF99"
    l.place(y = 50)
    
    l = Label(info, text = "Data inizio: 04/06/2016")
    l["background"] = "#FFFF99"
    l.place(y = 70)    

    l = Label(info, text = "Data fine: 04/06/2016")
    l["background"] = "#FFFF99"
    l.place(y = 90)    

    l = Label(info, text = "Licenza: GNU Affero General Public License v3")
    l["background"] = "#FFFF99"
    l.place(y = 110)
    
    info.mainloop()

def restart(root):
    root.destroy()
    root.quit()

    root = Tk()
    root.attributes("-fullscreen", True)   
    
    main(root)

def refresh(frame, root):
    frame.destroy()
    frame = Frame(root)
    frame.pack()

    l = Label(frame, text = time.strftime("%H:%S"))
    l.config(font = ("Tahoma", 50))
    l.pack()

def fm():
    tr = Toplevel()
    tr.title("File Manager")
    
    tree = ttk.Treeview(tr)
     
    tree["columns"]=("uno","due")
    tree.column("uno", width=100 )
    tree.column("due", width=100)
    tree.heading("uno", text="colonna A")
    tree.heading("due", text="colonna B")
     
    tree.insert("" , 0, text="Linea 1", values=("1A","1b"))
     
    id2 = tree.insert("", 1, "dir2", text="Dir 2")
    tree.insert(id2, "end", "dir 2", text="sub dir 2", values=("2A","2B"))
    tree.insert("", 3, "dir3", text="Dir 3")
    tree.insert("dir3", 3, text=" sub dir 3",values=("3A"," 3B"))
     
    tree.pack()
    tr.mainloop()

def main(root):
    frame = Frame(root)
    root.resizable(False, False)
    root.title("PyOS")
    root.geometry("800x600")
    root["background"] = "#FFFF99"

    menu1 = Menu(root)

    mStart = Menu(menu1, tearoff=0)  
    mStart.config(font = ("Tahoma", 15))
    menu1.add_cascade(label="Start", menu = mStart)

    mApp = Menu(mStart, tearoff = 0)
    mApp.config(font = ("Tahoma", 15))
    mStart.add_cascade(label="Applicazioni", menu = mApp)
    mApp.add_command(label = "Nessuna App installata")

    mStr = Menu(mStart, tearoff = 0)
    mStr.config(font = ("Tahoma", 15))
    mStart.add_cascade(label="Strumenti", menu = mStr)
    mStr.add_command(label = "Nessuno Strumento installato")

    mGam = Menu(mStart, tearoff = 0)
    mGam.config(font = ("Tahoma", 15))
    mStart.add_cascade(label="Giochi", menu = mGam)
    mGam.add_command(label = "Nessun Gioco installato")

    mEx = Menu(mStart, tearoff = 0)
    mEx.config(font = ("Tahome", 15))
    mStart.add_cascade(label = "Esci", menu = mEx)
    mEx.add_command(label = "Chiudi", command = root.destroy)
    mEx.add_command(label = "Riavvia", command = lambda: restart(root))

    mHelp = Menu(menu1, tearoff = 0)
    mHelp.config(font = ("Tahoma", 15))
    menu1.add_cascade(label = "?", menu = mHelp)
    mHelp.add_command(label = "Info", command = info)
    
    frame.pack()

    l = Label(frame, text = time.strftime("%H:%M"))
    l.config(font = ("Tahoma", 50))
    l["background"] = "#FFFF99"
    l.pack()

    img = PhotoImage(file = "file_manager.png")
    file_manager = Button(root, image = img, command = fm)
    file_manager.configure(width = 50, height = 50)
    file_manager.place(x = 20, y = 150)

    l = Label(root, text = "File Manager")
    l.config(font = ("Tahoma", 10))
    l["background"] = "#FFFF99"
    l.place(x = 7, y = 210)

    l = Label(root, text = "Python OS")
    l.config(font = ("Tahoma", 20))
    l["background"] = "#FFFF99"
    l.place(x = 600, y = 490)

    img2 = PhotoImage(file = "agplv3.png")
    agpl = Button(root, image = img2, command = lambda: os.system("notepad agplv3.txt"))
    agpl.configure(width = 88, height = 31)
    agpl.place(x = 620, y = 540)
    
    root.config(menu=menu1)

    root.mainloop()

main(root)
