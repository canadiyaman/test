
def toplama(sayi1: int, sayi2: int) -> int:
    toplam: int = sayi1+sayi2
    return toplam


sayi1: int = 14
sayi2: int = 19

toplam: int = toplama(sayi1, sayi2)
toplam2: int = toplama(55, 33)

print(toplama(22, 17))

toplam3: float = toplama(100.4, 42)


def ortalama_hesapla(liste: list):
    elemanlarin_toplami: int = 0
    eleman_sayisi: int = 0
    for eleman in liste:
        elemanlarin_toplami += eleman
        eleman_sayisi += 1

    ort = elemanlarin_toplami / eleman_sayisi
    return ort


elemanlar: list = [55,55,55,55,55,55,55]

print(ortalama_hesapla(elemanlar))

sayi: int = 44

def fibonacci(sayi):
    if sayi == 0:
        return 0
    if sayi == 1:
        return 1
    return fibonacci(sayi-1) + fibonacci(sayi-2)


# fibonacci(sayi)


# iki sayı arasındaki kalan sayıların toplamını buldurun.

#sayi1 = int(input("Birinci sayıyı girin: "))  # 40
#sayi2 = int(input("İkinci sayıyı gitin: "))  # 60

# Fonksiyon kullanmadan yazacak olsaydık

toplam: int = 0
if sayi1 < sayi2:
    # range(40, 60)
    for i in range(sayi1, sayi2):
        if i == sayi1:
            continue
        toplam += i
elif sayi2 < sayi1:
    for i in range(sayi2, sayi1):
        if i == sayi2:
            continue
        toplam += i
else:
    print("Sayılar eşit olduğundan sonuç 0 dır")

print("İki sayı arasındaki sayılar toplamı: ", toplam)


# fonksiyon ile yazacak olursak
def hesapla(sayi1: int, sayi2: int) -> int:
    toplam: int = 0
    if sayi1 < sayi2:
        for i in range(sayi1, sayi2):
            if i == sayi1:
                continue
            toplam += i
    elif sayi2 < sayi1:
        for i in range(sayi2, sayi1):
            if i == sayi2:
                continue
            toplam += i
        else:
            print("Sayılar eşit olduğundan sonuç 0 dır")
    return toplam

#sayi1 = int(input("Birinci sayıyı girin: "))  # 40
#sayi2 = int(input("İkinci sayıyı gitin: "))  # 60

toplamlari: int = hesapla(sayi1, sayi2)
print("sayi1 ve sayi2 arasındaki sayıların toplamı: ", toplamlari)


def	celsius_to_fahrenheit(celsius_sicaklık: float) -> float:
    celsius	= celsius_sicaklık
    fahrenheit = (9/5) * celsius + 32
    print(locals())
    return fahrenheit

print(celsius_to_fahrenheit(26))

print(abs(-100))
print(sum([2, 1, 100]))
print(round(3.143242323523532532, 2))

print(all(["dsadasdsa", True, 1]))
print(any(["", True, False]))

isim: str = 'Cem'
print(any([isim == 'Can', "", False]))

bool("Ahbap")

print(callable(isim))

print('Kalem')

deger: bool = isim == 'Can'

a = 'Kalem'
#print(eval(a))

a = 'print(3+5)'

print(exec(a))

def global_degiskenler():
    print(globals())
    a = 1222
    print(a)
    fonksiyon_ici_local_degisken = 'Deneme'
    print(fonksiyon_ici_local_degisken)


global_degiskenler()


def listeyi_degistir(bir_liste: list):
    bir_liste.append(10)
    bir_liste.append(100)
    bir_liste.append(1000)


listem: list = []
listeyi_degistir(listem)
print(listem)
