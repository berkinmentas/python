import sqlite3

con = sqlite3.connect("rehber.db")
imlec = con.cursor()

def tabloolustur():
    imlec.execute("CREATE TABLE IF NOT EXISTS kisiler(isim TEXT, numara INT, aciklama TEXT)")
    con.commit()
tabloolustur()

print("---MENU---")
print("1- Yeni kişi ekle")
print("2 Kişiyi Sil")
print("3- Kişiyi düzenle")

secim = int(input("Yapmak istediğiniz işlemi seçiniz"))

if secim ==1:
    ad = input("Kişinin ismini yazınız")
    no = input("Numarayı giriniz.")
    detay = input("Kişi açıklamasını giriniz.")
    veriler = [(ad, no, detay)]

    def degerekle():
        for veri in veriler:
            imlec.execute("""INSERT INTO kisiler VALUES (?, ?, ?)""", veri)
            con.commit()
    degerekle()
elif secim ==2:
    sil = input("Silinecek kişinin ismi ?")

    def degersil():
        imlec.execute("""DELETE FROM kisiler WHERE isim = ?""", [sil])
        con.commit()
    degersil()
elif secim ==3:
    isim = input("Duzenlenecek kişinin ismi")
    numarası = input("Düzenlenecek kişinin numarası")
    yeniisim = input("Kişinin yeni ismini giriniz")
    def degerduzenle():
        imlec.execute("""UPDATE kisiler SET isim = ? WHERE numara = ?""",(yeniisim,numarası))
        con.commit()
    degerduzenle()
else:
    print("Yanlış değer girdiniz")