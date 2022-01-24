from tkinter import *
import sqlite3

con = sqlite3.connect("todolist.db")
db = con.cursor()

def tabloolustur():
    db.execute("CREATE TABLE IF NOT EXISTS todolist(aciklama TEXT, gun TEXT)")
    con.commit()
tabloolustur()

pencere = Tk()
pencere.title("ToDoList")
pencere.geometry("600x700")

baslik = Label(text="Not Defteri",font=("Times New Roman", 30))
baslik.place(x=200, y=1)

metin = Label(text="Yapılacak : ", font=("Calibri",20))
metin.place(x=1, y=60)

veri = Entry(width=50)
veri.place(x=140, y=73)

metin = Label(text="Tarih : ", font=("Calibri",20))
metin.place(x=1, y=140)

veri2 = Entry(width=50)
veri2.place(x=80, y=155)

tablo = Listbox(width=200)
tablo.place(x=20, y=250)

def degerekle():
    ekle = veri.get()
    ekle2 = veri2.get()
    tablo.insert(END, (ekle, ekle2))
    db.execute("""INSERT INTO todolist VALUES (?,?)""", [ekle, ekle2])
    con.commit()
degerekle()

btn = Button(text=("Ekle"), fg=("black"), width=20, command=degerekle)
btn.place(x=20, y=500)

def degersil():
    sil = veri.get()
    tablo.delete(ACTIVE)
    db.execute("""DELETE FROM todolist WHERE aciklama = ?""",[sil])
    con.commit()
degersil()

btn2 = Button(text=("Sil"), fg=("black"), width=20, command=degersil)
btn2.place(x=20, y=540)

btn3 = Button(text=("Cikis"), fg=("black"), width=20, command=exit)
btn3.place(x=20, y=580)

pencere.mainloop()