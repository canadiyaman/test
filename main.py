

isim: str = "Can"
telefon: int = "90443434343"
tc_no: int = 2722222222
ders_notu: float = 90.33

kullanici: list = [isim, telefon, tc_no, ders_notu]


print(kullanici[0])
print(kullanici[1])
print(kullanici[2])
print(kullanici[3])

kullanici.remove("Can")

print(kullanici)

kullanici[0] = "Beşiktaş"

print(kullanici)

kullanici.insert(0, "Galatasaray")

print(kullanici)

print("########################################################")


kullanici_2: tuple = (isim, telefon, tc_no, ders_notu)

print(kullanici_2)

print(kullanici_2.index("Can"))


kullanici_3: dict = {
    "isim": "Can",
    "telefon": 90443434343,
    "tc_no": 2722222222,
    "ders_notu": 90.33
}

print(kullanici_3["isim"])

kullanici_3["isim"] = "Salih"

print(kullanici_3["isim"])
print(kullanici_3.get("isim"))

takim: str = kullanici_3.get("takim", "Galatasaray")
print(takim)

yeni_sozluk: dict = {"takim": "Galatasaray"}

kullanici_3.update(yeni_sozluk)

print(kullanici_3)


print(kullanici_3.get("Galataray", "Beşiktaş"))


kullanici_3: dict = {
    "kullanici_bilgileri": {
        "ad": "",
        "soyad": "Adıyaman",
        "kardesleri": ["Ali", "Yusuf"]
    },
    "hobileri": ["Futbol", "Yürüyüş"],
    "notlar": {
        "matetmatik": 0
    }
}

print(kullanici_3["kullanici_bilgileri"]["soyad"])


# Herkes yukarıdaki örnek gibi karmaşık bir sözlük yapısı oluştursun.
# Amaç kullanabildiğiniz kadar farklı değişken türünü bir arada kullanmak.
# Yukarıdaki gibi İç içe listeler sözlükler kullanıp sonra spesifik bir
# değere ulaşmaya çalışın
