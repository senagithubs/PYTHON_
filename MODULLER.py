# # import random
#
# #ÖRNEK:  BİR ZAR ATTIĞIMIZDA HANGİ SAYININ KAÇ KERE GELECEĞİNİN OLASILIĞINI HESAPLAYALIM.
#
# # zarlar={1:0,2:0,3:0,4:0,5:0,6:0} # başlangıçta her yüzeyin 0 adet geldiğini belirten sözlük oluşturduk
# #
# # for i in range(100): # zarı 100 kere attık
# #     zar = random.randint(1,6)
# #     zarlar[zar]+=1
# #
# # for zar in zarlar:
# #     print(f"{zar}gelme olasılığı: {zarlar[zar]/100}")
#
#
# # 10 kere 6:6 gelmesi için kaç sefer zar atmalıyız?
#
#
#
#
# #TİME MODÜLÜ:
#
# # import time
#
# # zaman = time.time()  # kabul edilen başlangıç zamanından itibaren geçen zamanın saniye karşılığı
# # print(zaman)
# #
# # baslangic =time.time()
# # liste =[]
# # for i in range(100000):
# #       liste.append(i)
# #
# # bitis = time.time()
# # print(bitis-baslangic)   # programın çalışma süresini öğrendik.
#
# # zaman = time.ctime()  # şu anınn zamanını gün saat sene verdi. içine bir değer girersem o kadar saniye sonraki zamanı verir
# # print(zaman)
# #
# # zaman =time.localtime()
# # print(zaman)
#
# # zaman =time.asctime() # içine time tuple veya struct time alır
# # print(zaman)
#
# # localtime ın verddiği kullanışsız sonucu asctime ile kullanışlı hale getirebliriz
# # zaman=time.localtime()
# # zaman2 = time.asctime(zaman)
# # print(zaman2)
#
#
# #EN ÇOK KULLANACAĞIM FONKSİYON: strftime() : zamanı  istediğim gibi yazdırmamı sağlar
#
# # zaman =time.strftime("%d:%m")
# # print(zaman)
# #
#
#
#
# # print("program başladı")
# # time.sleep(1)  # belirli bir süre uyumasını sağlar.  önemli bir fonksiyon
# # print("program sonlandı")
#
#
# #DATİME MODÜLÜ
#
# from datetime import date
# # import datetime
# # bugun = date.today()
# # print(bugun)
# # print(type(bugun))  #class yani kullanabileceğim fonk ları var
# #
# # print(bugun.day) # bugun classının özelliklerini
# #
# # print(bugun.weekday())  # pazartesi 0 alıp başlar . 0 6
# # print(bugun.isoweekday()) # pazartesi 1 alıp başlar.. 1 7
# #
# # gecmistarih =date(2002,5,23)
# #
# # print(gecmistarih.isoweekday()) # o günün perşembe olduğunu öğrendik
# # gecenzaman = bugun-gecmistarih
# # print(gecenzaman)
#
#
#
#
# from datetime import datetime

# suan = datetime.now()
# print(suan)
# print(suan.year)
# print(type(suan)) # class yani kendine ait fonk var
#
# print(suan.ctime())
# print(suan.month)

#TİMEDELTA
# şu andan belirli bir zaman sonrasını hesaplayalım.
# from datetime import timedelta

# suan = datetime.now()
# tdelta = timedelta(days=7)
# print(suan+tdelta)
# print(suan-tdelta)


# örnek: 1 ocak 1901 den 31 aralık 2000 e kadar kaç sefer bir ayın ilk günü pazar olur?



# OS MODÜLÜ:

# import os
# print(os.getcwd()) #bilgisayarımızda hangi klasörde olduğumuzu gösterir
#
# os.chdir("/Users/senai/OneDrive/Masaüstü/OSMODUL") # klasör değiştirmemizi sağlar. (change directory) içine klasör adresi gireriz
# print(os.getcwd())
#
# print(os.listdir()) # klasörün içeriğini listeler. bulunduğumuz klasör dışında başka bir klasörün içeriğini de listeleyebiliriz. bunun için parantez içine içeriğini görüntülemek istediğimiz dosya yolunu yazarız.
#
# # listdirin döndürdüğü klasör içeriğini daha okunabilir görmek için for döngüsü kullanabilirim
#
# for i in os.listdir():
#     print(i)
# #os.mkdir("DenemeKlasörü") #yeni bir dosya oluştururum.
# #os.makedirs("Deneme1/Deneme2/Deneme3")  # iç içe dosya oluşturdum
#
# #os.rmdir("DenemeKlasörü")   # klasör silmemi sağlar
# #os.removedirs("Deneme1/Deneme2/Deneme3")  # iç içe olan klasörleri silmemizi sağlar.silebilmesi için klasör içleri boş olmalı .Macte  sadece Deneme3 silinir. Deneme2 ve Deneme1 kalır. çünkü sadece içi boş olan dosyalar bu 2 satırda olduğu gibi silinir.
#
# # Macte o zaman önce dosya içini silinir. Mac in biz koymasak da kendi oluşturduğu klasörler var. onlar silinmeli
# #bu da os. remove() ile yapılır  . içine silinecek olan konur
#
# #os.rename("Book1.xlsx","BOOK1.xlsx")  # dosya ismini değiştirdim
#
# # burada adres girmedim çünkü zaten içinde bulunduğum klasördeki dosyada değişiklik yaptım . eğer farklı bir klasçr içerisindeki dosya ismini değiştirmek isteseydim, adresini de girmem gerekirdi.
#
#
# #os.rename("Deneme3.docx","/Userssenai/OneDrive/Masaüst/OSMODU/Books")  # bu şekilde dosyayı yeniden isimlendirirken onun adresini de değiştirebiliriz
# from datetime import datetime
# os.chdir("/Users/senai/OneDrive/Masaüstü/OSMODUL")
# print(os.stat("Books"))  # dosyayla ilgili bilgi verir
#
# print(os.stat("Books").st_atime)
#
# zaman = datetime.fromtimestamp(os.stat("Books").st_atime)  # daha anlaşılır bir tarih olarak görüntüledik
# print(zaman)

# for gecerliklasor,icindekiklasorler,icindekidosyalar in os.walk("/Users/senai/OneDrive/Masaüstü/OSMODUL"):  # os.walk() içine girdiğimiz dosyanın içindeki tüm dizinleri görüntüler
#     print("geçerli klasör:",gecerliklasor)
#     print("içideki klasörler:",icindekiklasorler)
#     print("içindeki dosyalar:",icindekidosyalar)

# print(os.path.join("BOOK1","/Book2","Book3"))  # dosya yollarını birleştirir. başına slash koyduğun dosyayı başlangıç dosyası kabul eder
# # başına / koyduklarından öncesini görmez. slashın olduğu yerden itibaren alır
#
# # print(os.path.isfile("")) # içine girdiğimiz adresteki şeyin dosya olup olmadığnı söyler.
#
# # print(os.path.isdir(""))  içine girdiğimiz adresteki şeyin klasör olup olmadığını söyler
#
#
# print(os.path.splitext("/Users/senai/OneDrive/Masaüstü/OSMODUL/Images/zkitap.exe.txt")) # . dan bölüyor. dosya uzantılarını elde etmede kullanılabilir
#


# DOSYALARI UZANTILARINA GÖRE FARKLI KLASÖRLERDE SINIFLANDIRMA PROJESİ

# dosya olup olmadığına göre ve uzantılarına göre listele
#
# import os
#
# os.chdir("/Users/senai/OneDrive/Masaüstü/PROJE")
#
# def duzenle():
#     klasor=input("Düzenlenecek Klasör:")
#     dosyalar=[] # dosyalar depolanacak
#     klasorler=[]   # klasorler depolanacak
#     uzantilar=[] # uzantılar depolanacak
#     def  list_dir():
#         for dosya in os.listdir(klasor):
#             if os.path.isdir(os.path.join((klasor,dosya))): # dosyamız klasor mu?
#                 continue
#             if dosya.startswith((".")):  # dosyamız gizli bir dosya mı?
#                 continue
#             else:
#                 dosyalar.append(dosya)
#
#
#     list_dir()
#
#
#      # uzantıları alma
#     for dosya in dosyalar:
#         uzanti= dosya.split(".")[-1]
#         if uzanti in uzantilar: # uzantı daha önce eklendi mi?
#             continue
#
#         else:
#             uzantilar.append(uzanti)
#
#     for  uzanti in uzantilar: # klasörler oluşturuluyor
#         if os.path.isdir(os.path.join(klasor,uzanti)):
#          continue
#         else:
#             os.mkdir(os.path.join(klasor,uzanti))
#
#
#
#     for dosya in dosyalar:
#         uzanti = dosya.split(".") [-1]
#         os.rename(os.path.join(klasor,dosya),os.path.join((klasor,uzanti,dosya)))
#
#
# if   __name__=="__main__":
#
#    duzenle()



# DOSYALARI  TARİHLERE GÖRE SIRALAMA



























#DOSYA İŞLEMLERİ





# 16 ve 21. videolar arası





#                                        LİST COMPREHENSİON

#
numbers = [1,2,3,4,5,6,7,8,9]
# # verilen listedeki rakaamlardan oluşan bir liste oluşturalım
#
# list2 =[]
# for number in numbers:
#     list2.append(number)
# print(list2)
#
#
#
# list3= [number for number in numbers]   # tek satırda yaptk:   [ listeye eklenecek olan eleman, elemanın nerede bluunduğu]
#
#
# print(list3)
#

#verilen listedeki elemanların karelerinden bir liste oluşturalım
#
# list4 =[number*number for number in numbers]
# print(list4)
#
#
#
# # verilen listedeki çift rakamlardan oluşan rakamlarla yeni bir liste oluşturalım
#
# list5=[number for number in numbers if number %2==0]
#
# # bi koşulumuz vaesa  bu koşul en sona if ilee eklenir
#
# listedeki çift rakamların karelerinden oluşan bir liste oluşturalım

#
# list =[number*number for number in numbers if number %2==0]
# print(list)


# 4 ten büyük çift sayıların karelerinden oluşan bir liste oluştur

# list =[ number*number for number in numbers if number>4 and number %2 ==0]
# print(list)


#
# numbers =[1,2,3,4]
# letters ="abcd"

#[(1,a),(1,b),1,c,1,d,2,a,  4,d     biçiminde ikililerde oluşan liste
# normalde şöyle yaparız

# list2=[]
# for number in numbers:
#     for letter in letters:
#         list2.append((number,letter))  # append fonk tek bir argüman alır o yüzden parantezle 2 elemanı 1 elemana getirerek ekledik
#
#
# print(list2)
#
#

# list=[(number,letter)for number in numbers for letter in letters]
# print(list)


#
# list1=[1,2,3,4,5,6,7,8,9]
# list2=[2,3,6,9,5]
#
# # birinci listede bulunup 2. listede bulunmayan rakamların karesinden oluşan bir liste oluşturalım
#
# list=[number*number for number  in  list1  if not number in list2]
# print(list)


# list=[[1,2,3],[4,5,6,7],[8,9,10,11,12]]
#
# # verilen listeden elemanları tek tek alan [1,2,3,4,5,6,7,8,9,10,11,12] biçiminde bir liste oluştur
#
# # normal yol:
#
# # liste2=[]
# #
# # for number in list:
# #     for i in number:
# #         liste2.append(i)
# #
# # print(liste2)
# liste=[i for number in list for i in number]
# print(liste)




#    TRY -EXCEPT(HATA AYIKLAMA)


# hata varsa program hata verip sonlanmasın çalışmaya devam etsin istiyoruz
#
# try:
#     # hata üretmesi muhtemel kodlar yazılır.
#     a=5
#     b=8
#     c=a/b
#
# except:  #try bloğunun içindeki kodlarda hata yoksa except bloğuna atlar ve çalışmaya kaldığı yerden devam eder
#
#
#     print("hata oluştu")
#
#
#
# print(a,b,c,sep="-")
#
# try:
#
#     a=5
#     b=8
#     c=a/b
#     d=x
#
# except Exception:
#     print("hata oluştu")
#     print("hatayı düzelten kodlar çalışmalı")


#birden fazla türde hata oluştuğunda oluşn türe göre mesaj
#
# try:
#
#         a = 5
#         b = 7
#         if b ==7:
#           raise ZeroDivisionError   # kendimiz de hata fırlatabiliriz
#
#         c = a / b
#         x=4
#         d=x
#         isim="Ali"
#         karakter=isim[2]
#
# except ZeroDivisionError:
#     print("payda 0 olmamalı")
#
#
# except NameError:
#     print("bu değişken daha önce tanımlanmamış")
#
#     # aslında burada  hatayı giderecek kodlar yer alır
#
# except IndexError:
#     print("böyle bir indeks bulunmuor")
#
#
# except Exception: # en alta konur
#     print("bilinmeyen bir hata oluştu")
#
#     #aklıma gelmeyen bir hata olursa bu gidecek
#
#
# else:
#     print("else bloğu çalışıor")
#
#      # try bloğunda herhangi bir hata yoksa else bloğu çalışır.
#
#
# finally:
#     print("finally bloğu çalışıyor")
#
#     # finally bloğu hata olsa da olmasa da kesinlikle hep çalışır.
#

#
#
# try:
#
#         a = 5
#         b = 2
#
#
#         c = a / b
#         x=4
#         d=x
#         isim="Ali"
#         karakter=isim[4]
#
# except ZeroDivisionError as e:
#     print(e)
#
#
# except NameError as e:
#     print(e)
#
#
#
# except IndexError as e:
#     print(e)
#
#
#
# except Exception as e: # en alta konur
#     print(e)
#
#
#
# else:
#     print("else bloğu çalışıor")
#
#
#
#
# finally:
#     print("finally bloğu çalışıyor")
# NESNE YÖNELİMLİ PROGRAMLAMA


# CLASS : ORTAK ÖZELLİKLERİ OLAN NESNELERİ GRUPLADIĞIMIZ BİR YAPI
# instance : o classtan oluşmuş nesne

# bir class oluşturma
#
# class calisan:
#     pass
#
# calisan1=calisan() # calisan 1 calisan classından üretilmiş örnek nesne(instance)
#
# calisan1.name="ali"
# calisan1.surname="veli"
# calisan1.age=20
# print(calisan1.age) # bu böyle çok zaman alır. class içinde ortak olan özelliklleri gruplandırmalıyız.


#
# class calisan:
#     def __init__(self,name,surname="girilmedi",age=0 ):
#         #age e deger girmezsen otomatik 0 # self mesela calisan1,calisan2  dir.  yani  üzernde çalıştığımız nesneelr
#         self.name=name # attribiutelar(özellikler)
#         self.surname =surname
#         self.age=age
#     # bir classa bağlı fonksiyonlara method denir. method oluşturalım
#     def showinfo(self):
#         print(f"Ad: {self.name},Soyad:{self.surname} yas:{self.age}")
#
#
#
# calisan1=calisan("ali,","veli",20)
# print(calisan1.name,calisan1.surname,calisan1.age)
#
#
# calisan2=calisan("ahmet","mehmet,",25)
# print(calisan2.name,calisan2.surname,calisan2.age)
#
# #calisan1.showinfo()
#
# calisan2.showinfo()
#
#
# calisan.showinfo(calisan2)# class üzerinden bunu çağırdığımızda içine inheritance(nesne) girmeliyiz.
#
# # diyelim ki mesela surname i girmek istemiyorum:
# calisan1=calisan("ali",age=20)   # bu şekilde girmelisin.
# calisan1.showinfo()



#OOP Class Variables vs Instance Variables( sınıf değişkenleri ve nesne değişkenleri)
#
# class calisan:
#     zam_orani = 1.1
#     def __init__(self,isim,maas):  # self üzerinde çalışılan nesne yerini alor
#         self.isim=isim # parametre içinde girilen isim olmuş oldu
#         self.maas=maas# parametrede girilen maas olmuş oldu
#
# calisan1=calisan("ali",5000)
# calisan2 =calisan("sena",100000)
#
# print(calisan1.isim)
#
#
# print(calisan1.__dict__)# caliasan 1 in sahip olduğu özellikleri bana sözlük olarak yazar
#
# print(calisan.__dict__)  # clssında bu şekilde özellikleri görebilir
#
# nesnelerin değişkenleri:  instance variables
#
#
# print(calisan1.zam_orani)
# print(calisan.zam_orani)
#
# print(calisan.__dict__)  # classsın özelliklerinde zam oranını görürüm.
# print(calisan1.__dict__)# ama  nesne özelliklerinde zam oranını göremem.
#
# #calisan.zam_orani=1.2  #herkesi günceller
# print(calisan1.zam_orani)
# print(calisan.zam_orani)
#
#
# # ama mesela ben istiyorum ki sadece 1 calisanıma farklı zam yapayım
#
# calisan2.zam_orani=3.3  # calisan2 disinda hepsi 1.1 sadece calisn2 değişir
# print(calisan1.zam_orani)
# print(calisan.zam_orani)
# print(calisan2.zam_orani)
#
#
# #özetle: classın kendi ismi üzerinden erişip güncellediğimde class dahil hepsini etkiledi,ama nesne üzerinden erişip değiştirdiğimizde sadec o nesneyi etkiledi
#
#
# class calisan:
#     personelsayisi=0
#     def __init__(self,isim,maas):
#         self.isim=isim # parametre içinde girilen isim olmuş oldu
#         self.maas=maas# parametrede girilen maas olmuş oldu
#         calisan.personelsayisi+=1
#
# print(calisan.personelsayisi)  #0
# calisan1=calisan("ali",2000)
# print(calisan.personelsayisi)#1
# calisan2=calisan("sena",25555555)
# print(calisan.personelsayisi)#2
#
# # self.personelsayisi yapsaydım o nesnenin kendi içindeki personel sayıısına ulaşırdım. ben classın genel personelsayisina erişmek istediğim için class ismi üzerinden çağırdım


# Instance Methods | Static Mthods
# from datetime import date #yasa göre sınıflandırma yaptığımz class methodunda kullanıcaz
# class kisi:
#     zamorani=1.1#class variable :tüm nesnelere etki eder. hem nesne üzerinden hem de sınıf üzerinden ulaşabiilirim
#     kisisayisi=0#class variable : classın kendine ait değişkenler
#     def __init__(self,isim,yas):  # içine girdiğimiz değişkenler nesne oluşturuken girilmesi gereken değişknler
#         self.isim=isim   # instance variables : ürettiğimiz nesneye ait değişkenler
#         self.yas=yas
#         kisi.kisisayisi +=1
#
#     def bilgilerinisoyle(self):#INSTANCE METHOD
#         return f"Ad:{self.isim} Yas:{self.yas}"
#
#     @classmethod
#     def kisisayisial(cls) : #CLASS METHOD
#         return cls.kisisayisi   #nesne üretmesek de class method çalışır.
#
#
#     @classmethod
#     def stringile(cls,str_):  # pythondaki str ile çakışmasın  diye _ekledim
#         isim,yas=str_.split("-")
#         return cls(isim,yas)
#     @classmethod
#     def dogumyili(cls,isim,dogumyili):
#         return cls(isim,date.today().year-dogumyili)
#
#
#     @staticmethod   #statik method un class method ve instance methoddan farkı içine bir şey almak zorunda değil. self,cls gibi. ama biz istersek girebiliriz
#     def dogumyilihesapla(yas):
#         return date.today().year-yas
#
#
# kisi5=kisi("x",21)
# print(kisi.dogumyilihesapla(kisi5.yas))
#
#
#
#
#
#
#
#
# kisi3= kisi.stringile("Ayse-25")
#
# print(kisi3.isim)
#
#
# kisi4 = kisi.dogumyili("elif",2002)
# print(kisi4.isim,kisi4.yas)
#
# #Statik (static) metotlar (methodlar), sınıfın bir örneğine (instance) veya sınıfın kendi içindeki değişkenlere doğrudan erişemezler.
# # Bu, statik metodların özelliğidir ve Python dilinde belirlenmiş bir kuraldır.
# #yani classta versek bile statik methodu kullanırken gerekli değişkeni parametre olarak girip tekrar almalıyız
#
#
#
#
#
#
#
# # print(kisi.kisisayisi) #o
#
# # print(kisi.kisisayisi)#1
# # kisi2=kisi("sena",22)
# # print(kisi.kisisayisi)#2
# #
# # kisi2.zamorani=1.2
# # print(kisi2.zamorani)  #sadece kisi2 yi etkiledi
# #
# # print(kisi1.zamorani)
# # print(kisi1.__dict__)
# # print(kisi.zamorani)
# # print(kisi1.bilgilerinisoyle())
# # #print(kisi.bilgilerinisoyle())   böyle kullanılamaz,instance method sadece nesnelerle kullanılır.
# #
# # print(kisi.kisisayisial())
# #
# #
# #
# #INSTANCE METHOD KULLANMAK İÇİN NESNE OLUŞTURMAK GEREKİR VE DEF İLE BAŞLAR(SELF)
# #CLASS METHOD KULLANMAK İÇİN NESNE ÜRETİLMİŞ OLMASINA GEREK YOK VE @CLASSMETHOD İLE CAĞIRIP KULLANDIK(CLS)
#


#                 INHERİTANCE
#
# class calisan:
#     zamorani=1.1
#     def __init__(self,isim,soyisim,maas):
#         self.isim=isim
#         self.soyisim=soyisim
#         self.maas=maas
#         self.email=isim+soyisim+ "@sirket.com"
#
#
#     def bilgilerigoster(self):
#        return "Ad:{} Soyad:{} Maas:{} EMAİL:{}".format(self.isim ,self.soyisim,self.maas,self.email)
#
# calisan1=calisan("ali","caliskan",5000)
# calisan2=calisan("veli","tembel",20000)
#
# # şimdi üstteki calisan classından miras alan başka bir class tanımlıyorum:
# class Yazilimci(calisan):  # normalde class oluştururken parantez olmaz . ama eğer miras alacaksak paraantez açılır ve içine miras alacağımız class ismi yazılır!
#
#      zamorani=1.2
#
#      # yazılımcıya ekstra özellik init fonk da  tanımlayalım.
#
#      def __init__(self,isim,soyisim,maas,dil): #AYNI OLAN ÖZELLİKLERİ MİRAS ALDIĞIN SINIFLA AYNI SIRADA YAZ Kİ MİRAS SINIFINDAN ÖZELLİKLER KULLANIRKEN SIKINTI ÇEKME
#          # yani şöyle:
#          super().__init__(isim, soyisim, maas)
#          self.dil = dil
#
#          #super().__init__(isim, soyisim, maas)_# böyle başlarsak zaten kalıtım aldığı sınıftaki özellikleri tekrar yazmama gerek kalmaz.buna ek farklı özellikleri eklriz
#          # self.isim = isim
#          # self.soyisim = soyisim
#          # self.maas = maas
#          # self.email = isim + soyisim + "@sirket.com"
#          # self.dil=dil
#
#
#
#
#
#      def bilgilerigoster(self):  # MİRAS ALDIĞIMIZDAKİ AYNI ADLI METHODU OVERRİDE ETTİK. ARTIK BU METHOD GEÇERLİ
#          return "Ad:{} Soyad:{} Maas:{} EMAİL:{},Dil:{}".format(self.isim ,self.soyisim,self.maas,self.email,self.dil)
#   # kalıtım aldığımız classta olmayan methodda tanımlayabiliriz
#      def dilinisoyle(self):
#         return f"bildigim dil: {self.dil}"
#
#
#
#
#
#
# yazilimci1= Yazilimci("ayse","yıldız",299,"python")
# yazilimci2=Yazilimci("sena","neya",12121212,"java")
#
# print(yazilimci1.bilgilerigoster())
# print(yazilimci1.dilinisoyle())
# # print(yazilimci1.email)
# # print(yazilimci2.email)
# #
# # print(calisan1.zamorani)
# # print(yazilimci2.zamorani)# içine yeni zam orani tanımlamadığımda 1.1 di tanımlayınca kendi classında   tanımladığım oldu
# #
# #
# # print(calisan1.bilgilerigoster())
# # print(yazilimci2.bilgilerigoster())
#
#
#
# class yonetici(calisan):
#
#     def __init__(self,isim,soyisim,maas,calisanlar=None):
#         super().__init__(isim, soyisim, maas)  # miras aldığım classla ortak kullanmak istediğim özellikler
#
#         if calisanlar==None:  #calisan yoksa boş liste
#            self.calisanlar=[]
#
#         else:
#             self.calisanlar=calisanlar  # varsa yönetici çalışan eşleşti
#
#     def calisanekle(self,calisan):
#             if calisan not in self.calisanlar: # o yöneticinin calisanlarında yoksa ekledik
#                 self.calisanlar.append(calisan)
#
#     def calisansil(self,calisan):   # silmek istediğim çalışan listede varsa siliyom
#            if calisan in self.calisanlar:
#                self.calisanlar.remove(calisan)
#
#     def calisanlarigoster(self): #bu içine sadece self alacak. çünkü benim göndermem gereken bi şey yok. içindekileri bana sunacak.
#           for calisan in self.calisanlar:
#              print(calisan.bilgilerigoster())
#
# yonetici1=yonetici("mehmet","ali",20000)  # yöneticiyi oluşturup çalışanlarını sonradan ekledim
# yonetici1.calisanekle(calisan1)
# yonetici1.calisanekle(yazilimci2)
#
# yonetici1.calisanlarigoster()
#
# yonetici1.calisansil(calisan1)
#
#
# yonetici2=yonetici("feyyaz","besiktas",10000,[yazilimci1,yazilimci2,calisan2])   #calisanlarını yöneticiyi oluştururken ekledim
# yonetici2.calisanlarigoster()
#
# # bir sınıf başka bir sınıfın alt class ımı ya da ondan üretilmiş bir nesne mi?
#
# print(isinstance(yonetici2,calisan))  # yonetici2 calisandan üretilmiş bir instance(ornek nesne)
#
# print(isinstance(yonetici1,Yazilimci))
#
# print(issubclass(calisan,Yazilimci)) # çalışan class ı yazılımcı class ın dan mı türedi?
# print(issubclass(Yazilimci,calisan))


#  Dunder Methods ( Magic )Methods


#__ double underscore kısaltması dunder  . yani bu methodlar __ ile başlıyor
#
# print(2+5)
# print(int.__add__(2,5))
# print("ali"+" veli")
# print(str.__add__("ali"," veli"))
# print([1,2,3] +[4,5,6])
# print(list.__add__([1,2,3],[4,5,6]))
#
# # 3 + nın işlevi de altında görüldüğü gibi farklı
#
#
# class Mylist(list): #list classından miras aldı
#     # biz kendi toplama işlem kurllarımızı tanımlayalım
#     def __add__(self, other):
#         if len(self)!=len(other):
#             return "Bu Elemanlar Toplanamaz"
#
#         else:
#             result= Mylist()
#             for i in range(len(self)):
#                 result.append(self[i]+other[i])
#         return result
#
#     def __sub__(self,other):
#        if len(self) != len(other):
#            return "Bu Elemanlar Çıkarılamaz"
#
#        else:
#            result = Mylist()
#            for i in range(len(self)):
#                result.append(self[i] - other[i])
#        return result
#
#     def __eq__(self, other):  # kendi eşit olma tanımıma göre fonk oluşturdum.
#         if sum(self)==sum(other):
#             return True
#         return False
#     def __abs__(self):
#         result=Mylist()
#         for i in self:
#             if i>=0:
#                 result.append(i)
#             else:
#                 result.append(-1*i)
#         return result
#
#
# liste1= Mylist([1,2,3])
# liste2 = Mylist([4,5,6])
# liste3=Mylist([-2,-6,7,-8])
#
# print ( liste1+liste2)
# print(liste1-liste2)
# print(liste1 == liste2)
# print(abs(liste3))
# print ( liste1+liste2)   #Mylist class ı içine bir özellik tanımlamadığımızda toplama işlemini liste mantığıyla yapar.

#print(liste1-liste2)  çıkartma fonk tanmlamadan yapınca error verir. çünkü listelerde çıkartma işlemi yok

#
# class futbolcu:
#     def __init__(self,isim,soyisim,yas):
#         self.isim=isim
#         self.soyisim=soyisim
#         self.yas=yas
#
#     def __eq__(self,other):
#         if self.isim ==other.isim  and self.soyisim==other.soyisim:
#             return True
#         return False
#
#     def __add__(self,other):
#         isim= self.isim[0]+other.isim[0]
#         soyisim=self.soyisim[0]+self.soyisim[0]
#         yas=self.yas+other.yas
#
#         return futbolcu(isim,soyisim,yas)
#
#     def __lt__(self, other):# küçüktür için
#         if self.yas < other.yas:
#             return True
#         return False
#     def __gt__(self,other):  # büyüktür için
#         if self.yas>other.yas:
#             return True
#         return  False
#
#
#
#
# futbolcu1=futbolcu("ali","x",21 )
# futbolcu2=futbolcu("arda","guler",19)
#
# print(futbolcu1==futbolcu2)
# futbolcu3=futbolcu1+futbolcu2
# print(futbolcu3)
#
# print(futbolcu1>futbolcu2)


#  İÇ İÇE FONKSİYON KULLANIMI
#
# def disfonk():
#     print("dış fonksiyon çalışıyor")
#     def icfonk():
#         print("iç fonksiyon çalışıyor")
#
#     print("dis fonksiyon sonlanıyor")
#     icfonk()
#
# disfonk()   # iç fonk sadece oluşturulur ama çalışöaz eğer iç  fionksiyonu oluşturduktan sonra dış fonk içersiinde  çağırırsak, dış fonksiyonu çağırdığımızda iç fonksiyon da çalışır.
#
#
#
# def hesaplamalar(x):
#     def kareal(a):
#         return a**2
#     def karekokal(a):
#         return a**0.5
#     def faktoriyel(a):
#         carpim =1
#         for i in range(1,a+1):
#             carpim *=i
#         return carpim
#
#     kare =kareal(x)
#     karekok=karekokal(x)
#     fak=faktoriyel(x)
#     return(f"karesi: {kare},karekoku{karekok},faktoriyeli:{fak}")
# #kareal  bu şekilde bu fonksiyonlara  fonksiyonların dışından  ulaşamayız çünkü fonksiyonların dışında
#
# print(hesaplamalar(6))

# def toplamcarpim(*args): #sayisi belli olmayan adette değerle işem yapacağım için parametre içine *arg girerim . *arg girildiğinde girdiğim sayılar demet olarak depolanır
#     def toplama(demet):
#         return sum(demet)
#     def carpma(demet):
#         carpim=1
#         for i in demet:
#             carpim *=i
#         return carpim
#
#     return f"carpimlari:{carpma(args)},toplamları:{toplama(args)}"
#
# print(toplamcarpim(3, 5, 6))

# FONKSİYONLARDAN FONKSİYON DÖNDÜRME
# def fonk(x):
#     return x*x
# a = fonk(3)
# print(a)
#
#
# b = fonk  # fonksiyonu b ye atadım.
# print(b)  #fonksiyon
# print(type(b))  # artık fonksiyo türünde.
#
#
# print(b(5))  # artık b(5) demek ile fonk(5) demek arasında hiçbir fark yok.

# yani fonksiyonlar da bir değişkene atanabilir ve o değişken artık o fonk gibi davranır
#
# def islemsec(islem):
#     def toplama(*args):
#         return sum(args)  #demetteki elemanları toplarım
#     def carpma(*args):
#         carpim =1
#         for i in args:
#             carpim  *=i
#
#         return carpim
#
#     def ortalama(*args):
#         toplam=0
#         adet=0
#         for i in args:
#             toplam+=i
#             adet +=1
#         ortalama=toplam/adet
#         return ortalama
#
#     if islem == "toplama":
#         return toplama
#
#     elif islem =="carpma":
#         return carpma
#     elif islem == "ortalama":
#         return ortalama
#
#
# toplamfonk = islemsec("toplama")
# print(toplamfonk(2,3,4,5))
#
#
#
# def kisisec(kisi):
#     def takimsec(takim):
#         return f"{kisi} {takim} takımını tutuyor "
#     return takimsec
#
#
# a=kisisec("ali")
# b=kisisec("veli")
#
# print(a("fenerbahçe"))   # ali fenerbahçe takımını tutuyor
# print(b("beşiktaş"))    # veli beşiktaş takımını tutuyor


#Fonksiyonlara Parametre Olarak Fonksiyon Göndermek
#
# def topla(x,y):
#     return x+y
# def carpma(x,y):
#     return x*y
#
# def islemyap(fonk,a,b):
#     return fonk(a,b)

#print(islemyap(topla,3,4))  #dikkat islemyap fonk tanımladığım şekilde koyduğum . topla fonk yanına parntez koymadım çünkü amacım işlem yap fonk çalıştırmak. o kendi içinde zaten topla(3,4) olarak return edecek

#yani fonksiyona parametre olarak fonk gönderirken gönderdiğimiz fonk nun sadece ismini yzarız. parantez koymayız


#liste =[1,2,3,4,5,6,7,8]
# fonk=x*x
# sonuc  = [1,4,9,16,25,36,49,64]

# liste1 =[1,2,3,4,5]
# liste2=[1,3,4,5,8,9,11]
#
# def kareal(x):
#     return x*x
# def kupal(x):
#     return x**3
#
# def mapfonk(fonk,list):
#     sonuc=[]
#     for i in list:
#         sonuc.append(fonk(i))
#     return sonuc
# print(mapfonk(kareal,liste2))


#Decorators | Python Decorator Kullanım
# var olan fonksiyonumuza özellikler eklememizi sağlayan fonksiyondur.
#mesela programımızda 100 tane fonk var ve biz bu 100 fonk nun ne kadar sürede çalıştığını öğrenmek istiyoruz,decorator kullanmalıyız.


# def decorator(fonk):   #içine parametree olarak fonksiyon alır
#     def wrapper():
#         print("fonksiyon çalışmadan önceki işlemler")
#         fonk()
#         print("fonksiyon çalıştktan sonraki işlemler")
#     return wrapper
# @decorator   # tanımladığım fonksiyonu al decoratora gönder anlamına geliyor
# def fonksiyon():
#     print("fonksiyon çalışıyor")
#
#
# fonksiyon2 = decorator(fonksiyon) # parantez koyarsak fonksiyonun kendisini değil fonksiyoun sonucunu decoratora göndermiş oluruz. o yüzden parantez YOK
# fonksiyon2()
import time
#
# def zamanhesapla(fonksiyon):  # 3 fonksiyondada decorator fonk sayesinde istediğimiz verileri hesapladık ve daha az uğraştık
#     def wrapper(*args,**kwargs):
#         baslangic=time.time()
#         fonksiyon(*args,*kwargs)
#         bitis=time.time()
#         print(f"islem{bitis-baslangic} saniye sürdü")
#     return wrapper
#
#
#
# def zamanhesapla(fonksiyon):
#    def wrapper(*args,**kwargs):
#       baslangic=time.time()
#       fonksiyon(*args,**kwargs)
#       bitis =time.time()
#       print( f"islem {bitis-baslangic} saniye sürdü")
#    return wrapper
#
#
#
# @zamanhesapla
# def karelerial(liste):
#     for i in liste:
#         print(i**2)
# @zamanhesapla
# def kuplerial(liste):
#     for i in liste:
#         print(i**3)
#
# @zamanhesapla
# def topla(a,b):
#     time.sleep(1)
#     print(a+b)
#
#
# karelerial(range(100000))
#
# kuplerial(range(1000000))
#
# topla(10,20)
#
#
#
#
#
#
#
#
#
#
# def zamanhesapla(fonk):
#     def wrapper(*args,**kwargs):
#         baslangic=time.time()
#         sonuc=fonk(*args,**kwargs)  # wrapper fonksiyonunda return edilen bir değer varsa onu kaybetmemek için değeri bir değişkene atıcaz.
#         bitis=time.time()
#
#         print(f"islem{bitis-baslangic} saniye sürdü")
#         return sonuc
#
#     return wrapper
#
#
#
# @zamanhesapla
#
# def karelerial(liste):
#     sonuc=[]
#     for i in liste:
#         sonuc.append(i**2)
#     return  sonuc
#
# @zamanhesapla
# def kuplerial(liste):
#     sonuc=[]
#     for i in liste:
#         sonuc.append(i**3)
#     return sonuc
# @zamanhesapla
# def topla(*args ):
#     time.sleep(1)
#     return sum(args)

#print(karelerial(range(100)))  #NONE  #çünkü döndürdü ama o değeri herhangi bir değişkene atamdm


# print(karelerial(range(110)))

#*args   değişken sayısını bilmediğimde
#**kwargs değişken türünü bilmediğimde eklerim

#31.video anlamadığım yer var!!!!!










#PYTHON OOP PROPERTY, SETTER, DELETER DECORATOR KULLANIMI

class kisi:
    def __init__(self,ad,soyad ):
              self.ad=ad
              self.soyad=soyad
              #self.adsoyad=ad+" "+soyad


    @property
    def adsoyad(self):
        return  f"{self.ad} {self.soyad}"
    @property
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"
    @adsoyad.setter
    def adsoyad(self,isim):
        ad,soyad=isim.split(" ")
        self.ad=ad
        self.soyad = soyad
    @adsoyad.deleter
    def adsoyad(self):
        print("silindi")
        self.ad=None
        self.soyad=None



kisi1=kisi("ali", "x")
# kisi1.adsoyad="ali sc" property method kullanırsam bu tarz durumlarda hata alırım.
# bu  durumu nasıl aşıcam?
kisi1.adsoyad="Ayşe Yıldız"
# emaili artık property ile tanımladığım için parantez kullanmıyorum


#ÖNEMLİ

#kisi1.ad="ahmet" #yaparsam ne olur?
# mail adresi init içinde tanımlanmadığı için en güncel halini kullandı
# ama adsoyad da öyle olmadı. çünkü sadece en başta oluştururken okuduğu veriden faydalandı ve  ad değişkeniyle bağlantısını kopardı. ad değişkeni üzerinde sonradan yapıılan değişikliklerle ilgilenmedi
# peki onu da nsl güncel yaparız?   adsoyadı init içinden kaldırıp onu da email gibi ayrı bir method olarak tanımlayabiliriz.
# ama bu yol büyükprogramlarda tek tek kullandığmız adsoyadı da etkileyiciğinden işlevsel değil

#bu yüzden PROPERTY DECORATOR un dan faydalanırız.  property decorator methodlarımıza bir özellik gibi erişmemizi sağlar (en başta yaptığımız adsoyad özelliği gibi init içinde tanımlarmış gibi kullanmamızı sağladı) ve  büyük projelerde  bahsettiğimiz tarzda bir problem yaşamamıza engel oldu.




# bir şeyi silmek istersek:
#del kisi1
#del kisi1.adsoyad

del kisi1.adsoyad   #silindi der  ama bi şey silmedim çünkü silcek kod yazmadım. şimdi adı soyadını değiştirecek kodlar yazıyorum yani ssadece silmek için değil kafamaa göre istediğim işleme yönelik kullanabilirim.

print(kisi1.ad)
print(kisi1.adsoyad)
print(kisi1.email)  # parantez olma sebebi self.ad self.soyad self.adsoyad özelliklerini classın içinde oluşturduk. o yüzden onlar paranez istemedi. ancak email diye bir özellik tanımlamadık. tanımadığı için tanımladığımız methodda işlem yapmak için bizden parantez koyarız






