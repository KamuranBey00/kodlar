#f = open("deneme.txt","r")
#icerik = f.read()
#print(icerik)
#f.close()

#with open("deneme.txt","r") as f:
#    icerik = f.read()
#    print(icerik)
#    for satir in icerik:
#        print(satir,end="")

#with open ("deneme.txt","r") as f:
#    okunacak_miktar = 10
#    icerik = f.read(okunacak_miktar)
#    while len(icerik)>0:
#        print(icerik,end="")
#        icerik = f.read(okunacak_miktar)
#with open("deneme2.txt","w") as f: a modu ile açılırsa textin içindekilere ekler append
#    f.write("Python")

#with open("deneme.txt") as okunacak:
#    with open("deneme2.txt","w") as yazilacak:
#        for satir in okunacak:
#            yazilacak.write(satir)

#with open("download.png","rb") as okunacak:
#    with open("python2.png","wb") as yazilacak:
#        okunacak_miktar = 1024
#        icerik = okunacak.read(okunacak_miktar)
#        while len(icerik)>0:
#            yazilacak.write(icerik)
#            icerik = okunacak.read(okunacak_miktar)
                    
#bu ikisi de aynı

#with open("download.png","rb") as okunacak:
#    with open("python3.png","wb") as yazilacak:
#        for satir in okunacak:
#            yazilacak.write(satir)


   

