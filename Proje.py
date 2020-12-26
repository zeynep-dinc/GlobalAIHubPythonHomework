import tkinter as tk

notlar={
    "midterm":0,
    "final":0,
    "project":0
}

student={
    "adi":"Zeynep",
    "soyadi":"Dinç",
    "notlar":notlar
}

durum=True
i=3
secilenler=[]

try:

    def puantablosu(a):                                                              # Notun olduğu harf aralığını bulan fonksiyon
            if(a<30):
                return   print("FF Başarısız")
            elif(a>=30 and a<50):
                return print("DD")
            elif(a>=50 and a<70):
                return print("CC")
            elif(a>=70 and a<90):
                return print("BB")
            else:
                return print("AA")

    def puanHesaplama():                                                           # Ağırlıklı Puan hesaplama
        return (notlar['midterm']*0.3)+(notlar['final']*0.5)+(notlar['project']*0.2)

    def dersSecimi(ad):                                                            # Ders seçimi yapna
        print("Hoşgeldiniz Sayın ",ad)
        dersSayisi=int(input("**En az üç (3) en fazla beş (5) adet ders alabilirsiniz.\n Kaç ders almak istiyorsunuz:"))
        while(dersSayisi>=3 or dersSayisi<=5):                                    # Ders sayisi eğer 3dem az veya 5den fazlaysa döngüye girer değilse for döngüsüne gidiyor
            if(dersSayisi<3):                                                     # Ders sayıs 3'den az ise Sınıfta kalabilirsiniz. En az 3 ders seçmelisiniz mesajı döndür
                print("En az 3 ders seçmelisiniz. Yoksa sınıfta kalırsın.\n")
                dersSayisi=int(input("**En az üç (3) en fazla beş (5) adet ders alabilirsiniz.\n Kaç ders almak istiyorsunuz:"))
            elif(dersSayisi>5):                                                   # Ders sayısı 5'den fazla olamaz
                print("En fazla 5 ders seçmelisiniz.\n")
                dersSayisi=int(input("**En az üç (3) en fazla beş (5) adet ders alabilirsiniz.\n Kaç ders almak istiyorsunuz:")) 
            else:                                                                 # 3 ile 5 arasındaysa 
                break
       
        for x in range(dersSayisi):                                               # Ders sayısı kadar ders adı, vize,final ve proje notları gösteriliyor
            secilenler.insert(x,input(format(x+1)+". Dersin Adı : "))
            notlar.update({
                "midterm":int(input("Vize: ")),                                     # Vize notunu al
                "final":int(input("Final: ")),                                      # Final Notunu al
                "project":int(input("Proje: "))                                     # Proje notunu al
            })
            a=puanHesaplama()
            puantablosu(a)
            
        print("Teşekkürler. Hoşçakalın")                                            # Veda mesajı yayınla

    while (durum!=False):                                                           # Durum pozitif olduğu sürece devam et
        if(i>0):
            print("Hoşgeldiniz")
            ad=input("Adınız: ")
            soyad=input("Soyadınız: ")

            if(ad in student['adi'] and soyad in student['soyadi']):                    # Eğer ad ve soyad sözlükte bulunan değerle aynıysa 
                dersSecimi(ad)                                                          # dersSecimi fonksiyonuna yolla
                durum=False                                                             # Durum False olarak atanır. Uygulama sonlandırılır
            else: 
                i-=1                                                                    # Değilse 3'den geriye doğru sayım başlat
                print("Şifre veya kullanıcı adı yanlış. Lütfen tekrar deneyiniz. Kalan deneme sayısı: ",i)
                
        else:
            print("3 hakkınız tükendi. Daha sonra deneyiniz.")                          # 3 hakkı tükendiğinde döngüden çık ve uygulamayı sonlandır
            break

except ValueError:                                                                     
    print("Yanlış karaktere bastınız!")

