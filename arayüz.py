from tkinter import *
import sqlite3

con = sqlite3.connect("rehber.db")
imlec = con.cursor()

pencere = Tk()
pencere.title("Telefon Rehberi")
pencere.geometry("700x350")

baslik = Label(text="Adres Defteri", font=("Calibri",15))
baslik.place(x=1, y=1)

metin = Label(text="İsim",font=("Calibri",15))
metin.place(x=1, y=30)
giris = Entry(width=30)
giris.place(x=85, y=35)

metin2 = Label(text="Numara",font=("Calibri",15))
metin2.place(x=1, y=60)
giris2 = Entry(width=30)
giris2.place(x=85, y=65)

metin3 = Label(text="Fotoğraf",font=("Calibri",15))
metin3.place(x=1, y=90)
giris3 = Entry(width=30)
giris3.place(x=85, y=95)

metin4 = Label(text="Açıklama",font=("Calibri",15))
metin4.place(x=1, y=120)
giris4 = Entry(width=30)
giris4.place(x=85, y=125)

metin5 = Label(text=("İsme Göre Ara"), font=("Calibri",13))
metin5.place(x=300, y=1)
giris5 = Entry(width=25)
giris5.place(x=450,y=5)

metin5 = Label(text=("Numaraya Göre Ara"), font=("Calibri",13))
metin5.place(x=300, y=25)
giris5 = Entry(width=25)
giris5.place(x=450,y=28)

liste = Listbox(width=60)
liste.place(x=300, y=170)

def degerekle():
    ad = giris.get()
    no = giris2.get()
    detay = giris4.get()
    liste.insert(END, (ad, no, detay))
    def kayitekle():
        imlec.execute("""INSERT INTO kisiler VALUES (?, ?, ?)""", [ad, no, detay])
        con.commit()
    kayitekle()
def degersil():
    sil = giris.get()
    liste.delete(ACTIVE)
    def kayitsil():
        imlec.execute("""DELETE FROM kisiler WHERE isim = ?""", [sil])
        con.commit()
    kayitsil()
buton = Button(text=("Kaydet"), fg=("Black"), bg=("Yellow"),width=15, command=degerekle)
buton.place(x=150, y=150)

buton2 = Button(text=("Yeni kayıt ekle"),fg=("Black"), bg=("Yellow"),width=15, command=degerekle)
buton2.place(x=1, y=180)

buton3 = Button(text=("Kayıt Sil"),fg=("Black"), bg=("Yellow"), width=15, command=degersil)
buton3.place(x=1, y=210)

buton4 = Button(text=("Kaydı Düzenle"),fg=("Black"), bg=("Yellow"), width=15)
buton4.place(x=1, y=240)

buton5 = Button(text=("İsme Göre Sırala"),fg=("Black"), bg=("Yellow"), width=15)
buton5.place(x=1, y=270)

buton6 = Button(text=("Çıkış"),fg=("Black"), bg=("Yellow"),width=15, command=exit)
buton6.place(x=1, y=300)

buton7 = Button(text=("Gözat"),fg=("Black"), bg=("Yellow"))
buton7.place(x=275, y=92)




pencere.mainloop()
