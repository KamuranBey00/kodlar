from random import randint

rand = randint(1, 100)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasında bir sayı giriniz (0 çıkış) :"))

    if sayi == 0:
        print("Oyunu iptal ettiniz.")
        break
    elif sayi < rand:
        print("Daha büyük bir sayı giriniz.")
        continue
    elif sayi > rand:
        print("Daha küçük bir sayı giriniz.")
        continue
    else:
        print("Rastgele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))
        break  
