import os 
from datetime import datetime
def duzenle():
    klasor = input("Düzenlenecek Klasör : ")
    dosyalar = [] #dosyalar depolanacak
    tarihler = [] #tarihler depolanacak
    def list_dir():
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor,dosya)):#dosyamız bir klasör mü?
                continue
            if dosya.startswith("."): #dosya gizli dosya mı?
                continue
            else:
                dosyalar.append(dosya) #herşeyi tamamsa dosyayı ekle
    list_dir()
    #tarihleri alma
    for dosya in dosyalar:
        item = os.path.getctime(os.path.join(klasor, dosya))
        tarih = datetime.fromtimestamp(item).strftime("%d-%m-%Y")
        if tarih in tarihler:
            continue
        else:
            tarihler.append(tarih)

    for tarih in tarihler:
        if os.path.isdir(os.path.join(klasor,tarih)):
            continue   
        else:
            os.mkdir(os.path.join(klasor,tarih))
    for dosya in dosyalar:
        item = os.path.getctime(os.path.join(klasor, dosya))
        tarih = datetime.fromtimestamp(item).strftime("%d-%m-%Y")

        os.rename(os.path.join(klasor,dosya),os.path.join(klasor,tarih,dosya))

if __name__ == "__main__":
    duzenle()       



