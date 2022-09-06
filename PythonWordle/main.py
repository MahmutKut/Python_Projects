import random
import time

from colorama import Fore, Back, Style


def kelimebulucu(kategori):
    if(kategori == 1):
        dosya = open("futboltakımları.txt", "r", encoding="utf-8")
        kelimeler = list()
        rastgeleindeks: int = random.randint(0,42)
        for i in dosya:
            kelimeler.append(i)
        asil_kelime = str(kelimeler[rastgeleindeks])
        return asil_kelime
    elif(kategori == 2):
        dosya = open("hayvanisimleri.txt", "r", encoding="utf-8")
        kelimeler = list()
        rastgeleindeks : int = random.randint(0,42)
        for i in dosya:
            kelimeler.append(i)
        asil_kelime = str(kelimeler[rastgeleindeks])
        return asil_kelime



print("******************************************** KELİME OYUNUNA HOS GELDİNİZ ********************************************")

isim = input("İsiminizi Girin :\n")
print("Oyun Menüsüne Aktarılıyorsunuz\n")
for i in range(1, 4):
    print(Fore.BLUE + "*" * i,end=" ")
    time.sleep(0.5)
print('\n')
print(Fore.CYAN + isim, Fore.WHITE + "Hos Geldin\n")
döngü = True
while (döngü):
    secim = input(Fore.WHITE+"Oyuna Baslamak İstiyorsan E yada e ye Bas \nOyundan Çıkmak İstiyorsan H yada h ye Bas\n")
    if (secim == 'e' or secim == 'E'):
        devam = True
        kategori = int(input('Kategorinizi Seçin \n1-Futbol Takımları \n2-Hayvan Türleri\n'))
    elif (secim == 'h' or secim == 'H'):
        print(Fore.BLUE+"TEKRAR BEKLERİZ GÖRÜŞÜRÜZ")
        devam = False
        döngü = False
        break
    else:
        print("Yanlış Tuşlama")
        devam = False

    while (devam):
        print(Fore.WHITE+"Kelime Belirleniyor\n")
        while(True):
            if kategori == 1:
                kelime = kelimebulucu(1)
                break
            elif kategori == 2:
                kelime = kelimebulucu(2)
                break
            else:
                print("Geçersiz Tuşlama")

        for i in range(1, 4):
            print(Fore.BLUE + "*" * i, end=" ")
            time.sleep(0.5)
        print(Fore.WHITE+"\n!!!!!!!!! KELİMENİZ BULUNDU !!!!!!!!!")
        print(kelime)
        gizlikelime = "* " * (len(kelime) - 1)
        print("Kelimeniz = ", gizlikelime, "Kelimeniz", len(kelime) - 1, "Harfli")
        deneme_hakki = 5
        karsilastirma = list()
        while (deneme_hakki > 0):
            tahmin = input(Fore.YELLOW + "Lütfen Tahmin Kelimenizi Girin :")
            if len(kelime) - 1 == len(tahmin):
                for i in range(0, len(kelime) - 1):
                    if tahmin[i].lower() == kelime[i].lower():
                        karsilastirma.append(i)
                print(gizlikelime)

                kelimedogrulugu=0
                for i in range(0, len(kelime) - 1):
                    dogru = False
                    for j in karsilastirma:
                        if (j == i):
                            print(Fore.GREEN + tahmin[j], end=" ")
                            kelimedogrulugu=kelimedogrulugu+1
                            dogru = True
                            break
                        else:
                            continue
                    if (dogru != True):
                        print(Fore.RED + tahmin[i], end=" ")

                if kelimedogrulugu == (len(kelime)-1):
                    print(Fore.CYAN+"\nTEBRİKLER KELİMEYİ BİLDİNİZ ANA MENÜYE AKTARILIYORSUNUZ\n")
                    for i in range(1, 4):
                        print(Fore.BLUE+"*" * i)
                        time.sleep(0.5)
                    devam = False
                    break
                deneme_hakki = deneme_hakki - 1
                print(Fore.WHITE + "Kalan Deneme Hakkınız = ", deneme_hakki)
            else:
                print(Fore.RED + "Harf Sayısı Yeterli Degil")
            if(deneme_hakki==0):
                print(Fore.CYAN + "\n DOĞRU KELİME = ", kelime)

        break
