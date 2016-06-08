from tkinter import *
from tkinter import ttk
import time
import os

color = "#FFFF99"
root = Tk()
root.attributes("-fullscreen", True)
root["background"] = color
frame = Frame(root)
#root.resizable(False, False)
root.title("PyOS")
#root.geometry("800x600")
frame["background"] = color
ctrlTestDir = StringVar()

def info(color):
    info = Toplevel()
    info["background"] = color
    info.resizable(False, False)
    info.title("Info")
    info.geometry("300x150")

    l = Label(info, text = "PyOS 0.5 Alpha", font = ("Tahoma", 20))
    l["background"] = color
    l.pack(side = "top")    

    l = Label(info, text = "Creato da: Niccolò Ciavarella")
    l["background"] = color
    l.place(y = 50)
    
    l = Label(info, text = "Data inizio: 04/06/2016")
    l["background"] = color
    l.place(y = 70)    

    l = Label(info, text = "Data fine: 04/06/2016")
    l["background"] = color
    l.place(y = 90)    

    l = Label(info, text = "Licenza: GNU Affero General Public License v3")
    l["background"] = color
    l.place(y = 110)
    
    info.mainloop()

def shutdown(root):
    root.destroy()
    root.quit()

    os.system("sudo poweroff")

def restart(root):
    root.destroy()
    root.quit()

    os.system("sudo reboot")

def refresh(l_time):
    l_time.config(text = time.strftime("%H:%M"), font = ("Tahoma", 50))
    l_time.pack()

    root.after(1000, refresh, l_time)

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

def theme(color, root, frame):
    frame.destroy()
    root.destroy()
    root.quit()

    root = Tk()
    root.attributes("-fullscreen", True)
    root["background"] = color
    frame = Frame(root)
    #root.resizable(False, False)
    root.title("PyOS")
    #root.geometry("800x600")
    frame["background"] = color

    main(root, frame, color)

def main(root, frame, color):
    menu1 = Menu(root)

    mStart = Menu(menu1, tearoff = 0)  
    mStart.config(font = ("Tahoma", 15))
    menu1.add_cascade(label = "Start", menu = mStart)

    mApp = Menu(mStart, tearoff = 0)
    mApp.config(font = ("Tahoma", 15))
    mStart.add_cascade(label = "Applicazioni", menu = mApp)
    mApp.add_command(label = "IDLE (Python 3.4)", command = lambda: os.system("sudo idle-python3.4"))

    mStr = Menu(mStart, tearoff = 0)
    mStr.config(font = ("Tahoma", 15))
    mStart.add_cascade(label = "Strumenti", menu = mStr)
    mStr.add_command(label = "Terminale", command = lambda: os.system("lxterminal"))
    mStr.add_command(label = "Text Editor", command = lambda: os.system("sudo python2.7 /home/pyos/pyos-master/editor.py"))
    mStr.add_command(label = "Calcolatrice", command = lambda: os.system("sudo python2.7 /home/pyos/pyos-master/calc.py"))

    mGam = Menu(mStart, tearoff = 0)
    mGam.config(font = ("Tahoma", 15))
    mStart.add_cascade(label = "Giochi", menu = mGam)
    mGam.add_command(label = "Nessun Gioco installato")

    mEx = Menu(mStart, tearoff = 0)
    mEx.config(font = ("Tahome", 15))
    mStart.add_cascade(label = "Esci", menu = mEx)
    mEx.add_command(label = "Spegni", command = lambda: shutdown(root))
    mEx.add_command(label = "Riavvia", command = lambda: restart(root))

    mFile = Menu(menu1, tearoff = 0)
    mFile.config(font = ("Tahoma", 15))
    menu1.add_cascade(label = "File", menu = mFile)

    mTema = Menu(mFile, tearoff = 0)
    mTema.config(font = ("Tahoma", 15))
    mFile.add_cascade(label = "Cambia Tema", menu = mTema)
    mTema.add_command(label = "Predefinito (PyOS)", command = lambda: theme("#FFFF99", root, frame))
    mTema.add_command(label = "Blu", command = lambda: theme("#87CEFA", root, frame))
    mTema.add_command(label = "Verde", command = lambda: theme("#98FB98", root, frame))
    mTema.add_command(label = "Argento", command = lambda: theme("#DCDCDC", root, frame))

    mHelp = Menu(menu1, tearoff = 0)
    mHelp.config(font = ("Tahoma", 15))
    menu1.add_cascade(label = "?", menu = mHelp)
    mHelp.add_command(label = "Info", command = lambda: info(color))
    
    frame.pack()

    l_time= Label(frame, text = time.strftime("%H:%M"))
    l_time.config(font = ("Tahoma", 50))
    l_time["background"] = color
    l_time.pack()

    day = time.strftime("%A")

    if(day == "Monday"):
        day = "Lunedì"

    if(day == "Tuesday"):
        day = "Martedì"

    if(day == "Wednesday"):
        day = "Mercoledì"

    if(day == "Thursday"):
        day = "Giovedì"

    if(day == "Friday"):
        day = "Venerdì"

    if(day == "Saturday"):
        day = "Sabato"

    if(day == "Sunday"):
        day = "Domenica"
        
    l = Label(frame, text = day + " " + time.strftime("%d/%m/%Y"))
    l.config(font = ("Tahoma", 30))
    l["background"] = color
    l.pack(side = "top")

    #frame.after(1000, refresh, frame, root)

    img = PhotoImage(file = "/home/pyos/pyos-master/file_manager.png")
    file_manager = Button(root, image = img, command = fm)
    file_manager.configure(width = 50, height = 50)
    file_manager.place(x = 20, y = 150)

    l = Label(root, text = "File Manager")
    l.config(font = ("Tahoma", 10))
    l["background"] = color
    l.place(x = 7, y = 210)

    imgte = PhotoImage(file = "/home/pyos/pyos-master/text_editor.png")
    text_editor = Button(root, image = imgte, command = lambda: os.system("sudo python2.7 /home/pyos/pyos-master/editor.py"))
    text_editor.configure(width = 50, height = 50)
    text_editor.place(x = 20, y = 250)

    l = Label(root, text = "Text Editor")
    l.config(font = ("Tahoma", 10))
    l["background"] = color
    l.place(x = 10, y = 310)

    imgc = PhotoImage(file = "/home/pyos/pyos-master/calc.png")
    calc = Button(root, image = imgc, command = lambda: os.system("sudo python2.7 /home/pyos/pyos-master/calc.py"))
    calc.configure(width = 50, height = 50)
    calc.place(x = 120, y = 150)

    l = Label(root, text = "Calcolatrice")
    l.config(font = ("Tahoma", 10))
    l["background"] = color
    l.place(x = 110, y = 210)

    l = Label(root, text = "Python OS")
    l.config(font = ("Tahoma", 20))
    l["background"] = color
    l.place(x = 600, y = 490)

    img2 = PhotoImage(file = "/home/pyos/pyos-master/agplv3.png")
    agpl = Button(root, image = img2, command = lambda: os.system("sudo gedit /home/pyos/pyos-master/agplv3.txt"))
    agpl.configure(width = 88, height = 31)
    agpl.place(x = 620, y = 540)
    
    root.config(menu=menu1)
    refresh(l_time)
    root.mainloop()

main(root, frame, color)
