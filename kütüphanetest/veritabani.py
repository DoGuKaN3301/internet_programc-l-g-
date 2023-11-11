import sqlite3 

baglanti = sqlite3.connect("veriler.db")    #    veriler.bd isimli bir veri tabanı yaratır

# tablo yaratma ve silme ve diğer işlemler için cursor nesnesi yarat

imlec = baglanti.cursor()   # veri tabanını kullamka için cursor komutuna ihtiyacımız var


# sorgu = "CREATE TABLE IF NOT EXISTS kullanicilar (ad TEXT , email TEXT , sifre TEXT )"  # kullanıcılar adında bir tablo yatar eğer tablo yok ise - yazdığımız alanalr text olacak 

# imlec.execute(sorgu)  # sorgu kodunu çalıştırır.

# baglanti.commit # yapılan işlemleri kaydet - aktif hale getirmek için

# # tabloya veri kadetme 

# sorgu = "INSERT INTO kullanicilar VALUES ('Dogukan','d@gmail.com','123456')"
# imlec.execute(sorgu)
# baglanti.commit()




sorgu = """CREATE TABLE IF NOT EXISTS urunler (id INTEGER PRIMARY KEY AUTOINCREMENT , 
                                                kod TEXT , 
                                                ad TEXT , 
                                                fiyat REAL )"""  # kullanıcılar adında bir tablo yatar eğer tablo yok ise - yazdığımız alanalr text olacak real ondalılı sayı tutmak için

imlec.execute(sorgu)  # sorgu kodunu çalıştırır.

baglanti.commit # yapılan işlemleri kaydet - aktif hale getirmek için

# tabloya veri kadetme 
import random
semboller="0123456789abcdefghjklmnoprstABCDEFGHJKLMNOUPRST" 
urun_kodu = ""
urun_kodu = "".join(random.choices(semboller , k = 5))
sorgu = f"INSERT INTO urunler (kod,ad,fiyat) VALUES ('{urun_kodu}','elma',35)"
imlec.execute(sorgu)
baglanti.commit()


