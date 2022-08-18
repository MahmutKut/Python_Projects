import time
class üyeler():
    def __init__(self,isim="BİLGİ GİRİLMEDİ",soyisim="BİLGİ GİRİLMEDİ",mevki="BİLGİ GİRİLMEDİ",yas="BİLGİ GİRİLMEDİ",tc="BİLGİ GİRİLMEDİ"):
        self.isim = isim
        self.soyisim = soyisim
        self.mevki = mevki
        self.yas = yas
        self.tc = tc
    def bilgilerioku(self):
        print("İSMİ = {}\nSOYİSMİ ={}\nKADEMESİ = {}\nYAŞI={}\nKADEMESİ = {}\n".format(self.isim,self.soyisim,self.mevki,self.yas,self.tc))
    def mevkidegistir(self,yenimevki):
        self.mevki=yenimevki
def dosyayayazdir(liste):
    file = open("kisibilgileri.txt", "w")
    print("KİSİLER DOSYAYA YAZDİRİLİYOR\n")
    time.sleep(2)
    for i in liste:
        file.write(i.isim)
        file.write("\t")
        file.write(i.soyisim)
        file.write("\t")
        file.write(i.mevki)
        file.write("\t")
        file.write(i.yas)
        file.write("\t")
        file.write(i.tc)
        file.write("\n")

    print("BAŞARIYLA KİŞİLER DOSYAYA YAZILDI\n")
    file.close()
    time.sleep(0.5)
    print("ANA MENÜYE AKTARILIYORSUNUZ \n")
    time.sleep(2)
def kisikaydetme():
    kisisayisi = int(input("KAÇ KİŞİYİ KAYIT EDECEKSİNİZ = "))
    kisiler = []
    for i in range(0, kisisayisi):
        oyuncular = üyeler(input("İSİMİ = "), input("SOYİSMİ = "), input("KADEMESİ = "), input("YAŞI = "), input("TC = "))
        kisiler.append(oyuncular)
        print("\n")
    dosyayayazdir(kisiler)
def uyeekleme(liste):
    file = open("kisibilgileri.txt", "a")
    print("YENİ ÜYE DOSYAYA EKLENİYOR\n")
    time.sleep(2)
    for i in liste:
        file.write(i.isim)
        file.write("\t")
        file.write(i.soyisim)
        file.write("\t")
        file.write(i.mevki)
        file.write("\t")
        file.write(i.yas)
        file.write("\t")
        file.write(i.tc)
        file.write("\n")
    print("BAŞARIYLA YENİ ÜYE DOSYAYA EKLENDİ\n")
    file.close()
    time.sleep(0.5)
    print("ANA MENÜYE AKTARILIYORSUNUZ \n")
    time.sleep(2)
def kisikaydetme1():
    kisisayisi = int(input("KAÇ KİŞİYİ KAYIT EDECEKSİNİZ = "))
    kisiler = []
    for i in range(0, kisisayisi):
        oyuncular = üyeler(input("İSİMİ = "), input("SOYİSMİ = "), input("KADEMESİ = "), input("YAŞI = "), input("TC = "))
        kisiler.append(oyuncular)
        print("\n")
    uyeekleme(kisiler)
def kisilerioku():
    file = open("kisibilgileri.txt", "r")
    kisiler=[]
    kisiler.append(file.read())
    for i in kisiler:
        print(i)
    print("KİŞİLER BAŞARIYLA OKUNDU \n")
    time.sleep(0.5)
    print("ANA MENÜYE AKTARILIYORSUNUZ \n")
    time.sleep(2)

print("*************************** ÜYE BİLGİLERİ KONTROL VE DÜZENLEME PROGRAMINA HOŞGELDİNİZ *************************** ")
devammi = True
while(devammi):
    secim = int(input(
        " 1-ÜYE EKLEME\n 2-ÜYELERİ VE BİLGİLERİNİ GÖRMEK\n 3-LİSTE YENİLEMEK(DİKKAT : ÖNCEKİ BİLGİLERİNİZ SIFIRLANACAKTIR.)\n 4-PROGRAMDAN ÇIKMAK\nHANGİ İŞLEMİ YAPACAKSINIZ ="))
    if (secim == 1):
        print("YENİ ÜYE İÇİN YER AÇILIYOR...")
        print("\n")
        time.sleep(2)
        kisikaydetme1()
    elif (secim == 2):
        print("ÜYELER LİSTELENİYOR...")
        print("\n")
        time.sleep(2)
        kisilerioku()
    elif (secim == 3):
        print("DOSYA OLUŞTURULUYOR...")
        print("\n")
        time.sleep(2)
        kisikaydetme()
    elif(secim == 4):
        print("\n")
        print("PROGRAMDAN ÇIKILIYOR")
        time.sleep(2)
        devammi=False
    else:
        print("Gecersiz Bir İşlem Seçtiniz")