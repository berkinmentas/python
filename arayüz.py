from tkinter import *
pencere = Tk()
pencere.title("Telefon Rehberi")
pencere.geometry("700x400")

baslik = Label(text="Adres Defteri",font=("arial",15))
baslik.place(x=1, y=1)

arama = Label(text=("İsme Göre Ara"))
arama.place(x=320,y=1)
agiris = Entry()
agiris.place(x=430,y=1)

arama2 = Label(text=("Telefona Göre Ara"))
arama2.place(x=320,y=30)
agiris2 = Entry()
agiris2.place(x=430,y=30)


etiket = Label(text= "İsim" )
etiket.place(x=1, y=60)
giris =  Entry(width=40)
giris.place(x=60, y=61)

etiket2 = Label(text= "Numara" )
etiket2.place(x=1, y=90)
giris2 =  Entry(width=40)
giris2.place(x=60, y=90)

etiket3 = Label(text= "Fotoğraf" )
etiket3.place(x=1, y=120)
giris3 =  Entry(width=30)
giris3.place(x=60, y=120)

buton2 = Button(text="Gözat", fg=("black"), bg=("yellow"))
buton2.place(x=265, y=118)

etiket4 = Label(text= "Açıklama" )
etiket4.place(x=1, y=150)
giris4 =  Entry(width=40)
giris4.place(x=60, y=150)

buton = Button(text= "Kaydet",fg="black", bg="yellow" )
buton.place(x=260, y=175)
buton2 = Button(text= "Yeni Kayıt Ekle",fg="black", bg="yellow" )
buton2.place(x=1, y=220)
buton3 = Button(text= "Kayıt Sil",fg="black", bg="yellow" )
buton3.place(x=1, y=250)
buton4 = Button(text= "Kaydı Düzenle",fg="black", bg="yellow" )
buton4.place(x=1, y=280)
buton5 = Button(text= "İsme Göre Sırala",fg="black", bg="yellow" )
buton5.place(x=1, y=310)
buton6 = Button(text= "Çıkış",fg="black", bg="yellow" )
buton6.place(x=1, y=340)

tablo = Listbox(width=65)
tablo.place(x=300, y=210)








pencere.mainloop()