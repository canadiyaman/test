

kullanicilar: list = ['Ahmet', 'Can', 'Ali']

kullanicilar2: tuple = ('Ahmet', 'Can', 'Ali')

kullanicilar3: dict = {
    "kullanicilar": ['Ahmet', 'Can', 'Ali'],
}

for anahtar in kullanicilar3:
    print("Kullanıcı ->", kullanicilar3[anahtar])

ogrenciler = {
    "101": {
        "Adi": "Ahmet",
        "Soyadi": "Solmaz"
    },
    "102": {
        "Adi": "Can"
    },
    "103": {
        "Adi": "Leyla",
        "Soyadi": "Pak"
    },
}

for ogrenci_no, ogrenci in ogrenciler.items():
    print("Adı: ", ogrenci["Adi"])
    if ogrenci.get("Soyadi") is None:
        continue
    print("Soyadı: ", ogrenci["Soyadi"])


# -> listeyi tersten okumaya başlama

notlar: list = [1, 5, 100, 55, 200, 2]

dersler: list = ["Matematik", "Fizik", "Kimya"]

dersler.sort()

for ders in reversed(dersler):
    print(ders)

for ders_notu in reversed(notlar):
    print("not -> ", ders_notu)


# -> listeyi sıralayarak okuma
ders_notlari: list = [1, 5, 100, 55, 200, 2]

ders_notlari.sort(reverse=True)

for d_n in ders_notlari:
    print("not ->", d_n)

# [0,1,2,3...99]
# [5,10,15,20,25]
for i in range(101, 5, -5):
    print(i)


sira: int = 100

while True:
    if sira == 2:
        break

    print("çalışmaya devam et", sira)
    sira -= 1

# continue
# break

durum: bool = True
sira: int = 0
limit: int = 100

ogrenci_listesi: list = []

while durum:
    ogrenci_listesi.append({"Ad": "Can"})
    sira += 1
    if sira == limit:
        break

print(ogrenci_listesi)


ogrenciler: dict = {
    "101": {
        "Adi": "Ahmet",
        "Soyadi": "Solmaz"
    },
    "102": {
        "Adi": "Can"
    },
    "103": {
        "Adi": "Leyla",
        "Soyadi": "Pak"
    },
}
ogrenci_listem: list = []

for ogr_no, ogrenci in ogrenciler.items():
    if not ogrenci.get('Soyadi'):
        continue
    ogrenci_listem.append(ogrenci)

print(ogrenci_listem)


tavan: int = 100
while True:
    print(tavan * "*")

    tavan -= 1

    if tavan == 1:
        tavan: int = 100
