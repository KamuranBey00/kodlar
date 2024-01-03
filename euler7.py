def asal_sayi_bul(n):
    asal_sayilar = []
    sayi = 2

    while len(asal_sayilar) < n:
        for i in range(2, int(sayi**0.5) + 1):
            if sayi % i == 0:
                break
        else:
            asal_sayilar.append(sayi)
        sayi += 1

    return asal_sayilar[-1]

print(f"10.0001'inci asal sayı=",asal_sayi_bul(100001))
