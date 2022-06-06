
isim: str = "selih"
ders_notu: int = 90

print(ders_notu > 70 and isim == "Can")

if type(ders_notu) == int and isim == "Can":
    print("Kullanıcı login olabilir")
else:
    print("Kullanıcı bilgilerinizi yanlış girdiniz")


# yon = input("yön girin: ")

#if yon == "sag":
#    print("sağa kaydır")
#    #sağ tarafa yönlendirme komutları burada çalışacak
#elif yon == "sol":
#    print("sola kaydır")
#    # sol tarafa yönlendirme komutları çalışacak
#elif yon == "arka":
#    print("arkaya kaydır")
#else:
#    print("Hatalı yön")



def is_number(deger: str) -> bool:
    try:
        int(deger)
        return True
    except ValueError:
        return False

#birinci_deger: str = input("Bir değer girin: ")


#if birinci_deger.isnumeric():
#    print("Bir sayı değeri girdiniz")
#elif type(birinci_deger) == str:
#    print("Bir metin değeri girdiniz")
#else:
#    print("Girilen değer tanımlanmadı")

ders_notu = 90
baraj = 60

#if ders_notu >= baraj:
#    print("Geçti")
#elif ders_notu < baraj:
#    print("Kaldı")
#else:
#    print("Hatalı ders notu girilmiş")



ders_notu: int = 49
baraj: int = 60
kosullu_baraj: int = 50

kaldigi_diger_dersler: list = ["Matematik", "İngilizce"]

# <= >= == != is not
# and or
# True ve True ise -> True
# True ve False ise -> False
# True ya da True ise -> True
# True ya da False ise -> True


if not ders_notu >= baraj:
    print("Kaldı")
elif ders_notu >= kosullu_baraj and len(kaldigi_diger_dersler) <= 2:
    print("Koşullu geçti")
else:
    print("Kaldı")

a = type(ders_notu) is int


