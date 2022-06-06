
# class (sınıf)


class Departman:
    DepartmanAdi: str


class Eleman:
    Ad: str
    Soyadi: str
    Dogum_tarihi: str
    Telefon: str
    EhliyetNo: str = None
    Departman: Departman

    def is_can_fly(self):
        pass

    def ehliyeti_var_mi(self) -> bool:
        # bazı bilgilerine bakarız
        # EhliyetNo var ve en az iki yıllıksa True dön
        return self.EhliyetNo is not None

sayi1: int = int(22)
print(type(sayi1))


calisan: Eleman = Eleman()
calisan.Ad = "Ahmet"
calisan.Soyadi = "Çoban"
calisan.Telefon = "5433434343"
calisan.Dogum_tarihi = "1111111"
calisan.EhliyetNo = "BU4332"

departman: Departman = Departman()
departman.DepartmanAdi = "Muhasebe"

calisan.Departman = departman

print(type(calisan))

print(dir(calisan))


print(calisan.ehliyeti_var_mi())
print(calisan.Ad)


calisan.EhliyetNo = "BU434343"

print(calisan.Ad, " isimli elemanın ", "Ehliyeti Var" if calisan.ehliyeti_var_mi() else "Ehliyeti Yok")

if calisan.ehliyeti_var_mi():
    print(calisan.Ad, " isimli kullanıcının ehliyeti var")
else:
    print(calisan.Ad, " isimli kullanıcının ehliyeti yok")



class YakitTuru:
    Id: int
    Adi: str

dizel: YakitTuru = YakitTuru()
dizel.Adi = "Dizel"
dizel.Id = 1

dizel: YakitTuru = YakitTuru()
dizel.Adi = "Benzin"
dizel.Id = 2

dizel: YakitTuru = YakitTuru()
dizel.Adi = "Gaz"
dizel.Id = 3


class Renk:
    Kod: str
    Adi: str

    def __init__(self, kod, adi):
        self.Kod = kod
        self.Adi = adi
        print(self.tanimla(sadece_kod=True))

    def tanimla(self, sadece_kod: bool):
        if sadece_kod:
            return f"Bu rengin kod {self.Kod}"
        else:
            return f"Bu rengin Adı: {self.Adi}, kodu ise: {self.Kod}"


renk1: Renk = Renk(kod="#343433", adi="Mavi")


class Araba:
    PlakaNo: str
    Renk: str
    ModelYili: int
    Model: str
    YakitTuru: YakitTuru
    Kilometre: int

    def durumu(self):
        # sasasa
        return


araba1: Araba = Araba()
araba1.PlakaNo = "34DF077"
araba1.Renk = "Mavi"
araba1.ModelYili = 2020
araba1.Model = "Polo"
araba1.YakitTuru = dizel
araba1.Kilometre = 22222


arabalar: list = []

for i in range(100):
    arabalar.append(Araba())


print(arabalar)


class Personel(object):
    Ad: str
    Soyad: str
    Telefon: str

    def __init__(self, ad, soyad, telefon):
        self.Ad = ad
        self.Soyad = soyad
        self.Telefon = telefon

    def tam_adi(self):
        return f"{self.Ad} {self.Soyad}"


class Yonetici(Personel):
    Sorumluluklari: list

    def __init__(self, ad, soyad, telefon, sorumluklari: list):
        super(Yonetici, self).__init__(ad, soyad, telefon)
        self.Sorumluluklari = sorumluklari


class Outsource(Personel):
    Ad: str
    Soyad: str
    Telefon: str
    KayitliSirketi: str

    def tam_adi(self):
        return f"{self.Ad} {self.Soyad}"

    def numarasi(self):
        return self.Telefon


eleman: Outsource = Outsource(ad="Hüseyin", soyad="Yiğit", telefon="9090999")
print(eleman.numarasi())

yonetici: Yonetici = Yonetici(ad="Ayşe", soyad="Kaplan", telefon="90990090", sorumluklari=["A deparment", "İK"])
print(yonetici.tam_adi())


# www.github.com
# https://desktop.github.com/
