import sqlite3
import time
"""
BU KODDA SQLİTE3 VERİ TABANI KULLANILMAKTADIR KODDAN ÖNCE VERİ TABANININ KURULU OLDUĞUNDAN EMİN OLUN
"""

def veritabanınabaglan():
    tablo = sqlite3.connect("supermarket.db")
    düzenleyici=tablo.cursor()
    return düzenleyici,tablo
def veriyeislevekapat(tablo):
    tablo.commit()
    tablo.close()
def tabloyuoluşturma():
    düzenleyici,tablo =veritabanınabaglan()
    düzenleyici.execute("CREATE TABLE IF NOT EXISTS supermarket(ürün_markasi TEXT,ürün_adi TEXT, ürün_fiyati INT,sonkullanmatarihi TEXT)")
    veriyeislevekapat(tablo)

"""
'ürünekleme' FONKSİYONUNDAKİ MARKA ADA FİYAT KISMINI KENDİNİZE GÖRE DEĞİŞTİREBİLİRSİNİZ 
UYARI ------> ('ürünekleme' FONKSİYONUNDA BİR DEĞİŞİKLİK YAPACAKSANIZ  'ürünokuma' FONKSİYONUNDANDA AYNI ŞEKİLDE DEĞİŞİKLİK YAPMAYI UNUTMAYIN)
"""
def ürünekleme(marka,ad,fiyat,sonkullanma):
    düzenleyici, tablo = veritabanınabaglan()
    düzenleyici.execute("INSERT INTO supermarket VALUES(?,?,?,?)",(marka,ad,fiyat,sonkullanma))
    veriyeislevekapat(tablo)
def ürünokuma():
    düzenleyici, tablo = veritabanınabaglan()
    düzenleyici.execute("SELECT * FROM supermarket")
    ürünbilgisi = düzenleyici.fetchall()
    print("\nMARKA \t ÜRÜN ADI \t FİYAT \t SON KULLANMA TARİHİ")
    for i in ürünbilgisi:
        print(i)
        time.sleep(0.1)
    time.sleep(1)
    tablo.close()
def ürünsilme(silinecekürün):
    if(silinecekürün=="hepsi"):
        düzenleyici, tablo = veritabanınabaglan()
        düzenleyici.execute("DELETE FROM supermarket")
        veriyeislevekapat(tablo)
    else:
        düzenleyici, tablo = veritabanınabaglan()
        düzenleyici.execute("DELETE FROM supermarket where ürün_adi = ?", (silinecekürün,))
        veriyeislevekapat(tablo)
def fiyatdegistirme(ürünadi, yenifiyat):
    düzenleyici, tablo = veritabanınabaglan()
    düzenleyici.execute("UPDATE supermarket SET ürün_fiyati = ? where ürün_adi = ? ",(yenifiyat, ürünadi,))
    veriyeislevekapat(tablo)

"""
DOSYADAN BİLGİ ALMAK İÇİN KOD KLASÖRÜNÜN İÇİN 'ürünlergirdi.txt' ADLI DOSYAYI EKLEYİNİZ VE İÇERİSİNDE ÜRÜN BİLGİLERİ OLSUN. ( DOSYANIN ADINI -> İSMİNİ KOD İÇERİSİNDEN DEĞİŞTİREBİLİRİSİN)
"""

def dosyadanbilgial():
    ürünler=list()
    file = open("ürünlergirdi.txt","r",encoding="utf-8")
    print("\nDOSYADAKİ BİLGİLERİNİZ")
    time.sleep(0.7)
    for i in file:
        print(i[:-1])
        time.sleep(0.7)
        i_elemanları = i.split("-")
        ürünekleme(i_elemanları[0], i_elemanları[1], i_elemanları[2],i_elemanları[2])

"""
DOSYAYA BİGLİ AKTARIMINI 'ürünlercikti.txt' ADLI TEXT DOSYASININ İÇERİSİNE AKTARMAKTADIR.
"""
def dosyayaaktar():
    düzenleyici, tablo = veritabanınabaglan()
    düzenleyici.execute("SELECT * FROM supermarket")
    ürünbilgisi = düzenleyici.fetchall()
    ürünbilgisi=str(ürünbilgisi)
    ürünbilgisis=ürünbilgisi.split("),")
    file = open("ürünlercikti.txt", "a", encoding="utf-8")
    for i in ürünbilgisis:
        file.write(i)
        file.write("\n")

"""
'süslügecisekrani' FONKSİYONU GÖRÜNTÜ GÜZELLEŞTİRMEK İÇİN YAPILMIŞTIR İÇİNE BİR YERDEN BAŞKA MENÜYE GEÇİŞ YAPMADAN ÖNCEKİ SON CÜMLENİN UZUNLUĞUNU GÖNDERİN,
OTOMATİK OLARAK ONUN BOYUTUNDA '*' EKLEYECEKTİR.
CÜMLENİN UZUNLUĞUNU BULMAK ---> CÜMLEYİ SEÇİNİZ VE SAĞ ALTTA PARANTEZ İÇERİSİNDE (SAYİ chars) YAZACAKTIR.
"""
def süslügecisekrani(kelimeninuzunluğu):
    for i in range(1, kelimeninuzunluğu+1):
        print("*", end="")
        time.sleep(0.02)
    print("\n")

print("******************************** SÜPER MARKET BİLGİLERİ DÜZENLEYİCİYE HOŞGELDİNİZ ********************************")
time.sleep(0.5)
print("ANA MENÜYE AKTARILIYORSUNUZ")
süslügecisekrani(27)

devammi = True

while(devammi):
    secim = int(input("\n 1-ÜRÜN EKLEMEK\n 2-ÜRÜN BİLGİLERİNİ GÖSTER\n 3-ÜRÜN ÇIKART\n 4-ÜRÜN FİYATI DEĞİŞTİR\n 5-DOSYADAN BİLGİLERİ AKTARMA\n 6-DOSYAYA ÜRÜN BİLGİLERİNİZİ AKTARMAK\n 7-UYGULAMADAN ÇIKIŞ\n= "))

    # TABLOYU BİR KERE OLUŞTURMAMIZ LAZIM EĞER BU KOD BİR KERE ÇALIŞACAKTIR ZATEN ÖNCEDEN ÇALIŞMIŞSA TABLOYU OLUŞTURMA KODUNDA KULLANDIĞIMIZ 'REATE TABLE IF NOT EXISTS' KISMI BİR DAHA ÇALIŞMASINI ENGELLEMEYİ SAĞLAMAKTADIR
    tabloyuoluşturma()

    if (secim == 1):
        tekrar=True
        while tekrar:
            print("EKLEMEK İSTEDİGİNİZ ÜRÜNÜN : ")
            marka = input('MARKASINI GİRİNİZ=')
            ad = input('ADINI GİRİNİZ=')
            fiyat = float(input("FİYATINI GİRİNİZ ="))
            skt = input('SON KULLANMA TARİHİNİ GİRİNİZ=')
            ürünekleme(marka, ad, fiyat, skt)
            print("ÜRÜNLERİNİZ BAŞARIYLA EKLENMİŞTİR")
            istiyormusun = input("\nÜRÜN EKLEMEYE DEVAM ETMEK İSTİYOR MUSUNUZ? (devam etmek için 'e', durmak için = 'h')")
            if (istiyormusun == 'h' or  istiyormusun=='H'):
                tekrar = False
            elif(istiyormusun == 'e' or  istiyormusun=='E'):
                continue
        print("\nANA MENÜYE AKTARILIYORSUNUZ\n")
        süslügecisekrani(27)
    elif (secim == 2):
        ürünokuma()
        print('ÜRÜNLERİNİZ BAŞARIYLA OKUNMUŞTUR')
        print("\nANA MENÜYE AKTARILIYORSUNUZ\n")
        süslügecisekrani(27)
    elif (secim == 3):
        ürünokuma()
        çıkarılacakürün = input('\nÇIKARTMAK İSTEDİGİNİZ ÜRÜNÜN ADINI YAZINIZ BÜTÜN LİSTEYİ ÇIKARTMAK İÇİN (hepsi) YAZINIZ= ')
        ürünsilme(çıkarılacakürün)
        print("ÜRÜN ÇIKARILIYOR")
        süslügecisekrani(16)
        print("ÜRÜN BAŞARILI ŞEKİLDE ÇIKARILDI")
        print("GÜNCEL ÜRÜN LİSTENİZ")
        ürünokuma()
        print("\nANA MENÜYE AKTARILIYORSUNUZ\n")
        süslügecisekrani(27)
    elif (secim == 4):
        print("GÜNCEL ÜRÜN LİSTENİZ")
        ürünokuma()
        ürün = input("\nFİYATINI DEĞİŞTİRMEK İSTEDİĞİNİZ ÜRÜNÜ GİRİNİZ = ")
        yenifiyat = float(input("YENİ FİYATINI GİRİNİZ = "))
        fiyatdegistirme(ürün, yenifiyat)
        print("YENİ ÜRÜN LİSTENİZ:")
        ürünokuma()
        print("\nANA MENÜYE AKTARILIYORSUNUZ\n")
        süslügecisekrani(27)
    elif(secim==5):
        dosyadanbilgial()
        print("\nBİLGİLER TABLOYA AKTARILIYOR")
        süslügecisekrani(28)
        print("BAŞARIYLA BİLGİLERİNİZ DOSYAYA AKTARILDI")
        print("\nANA MENÜYE AKTARILIYORSUNUZ\n")
        süslügecisekrani(27)
    elif(secim==6):
        print("\nŞUANKİ ÜRÜNLERİNİZ VE BİLGİLERİ : ")
        time.sleep(0.8)
        ürünokuma()
        print("\nBİLGİLERİNİZ DOSYAYA AKTARILIYOR")
        süslügecisekrani(32)
        dosyayaaktar()
        print("BAŞARIYLA DOSYAYA BİLGİLERİNİZ AKTARILDI")
        print("\nANA MENÜYE AKTARILIYORSUNUZ\n")
        süslügecisekrani(27)
    elif (secim == 7):
        devammi = False
        print("UYGULAMADAN ÇIKILIYOR")
        süslügecisekrani(21)
    else:
        print("GEÇERSİZ SEÇİM")