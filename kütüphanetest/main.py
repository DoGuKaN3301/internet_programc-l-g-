from flask import Flask,render_template, request,redirect ,session #    flask kütüphanesinden Flask sınıfını getir. render_template html sayfasını yüklemeye yarıyor
import sqlite3

app = Flask(__name__)      #    flask nesnesi oluştur app isimli değişkende sakla  __name__ dosyanın adını belirtiyor
app.secret_key= "1234" 

# @app.route("/")            #    anasayfa açıldığında ne yapayım
# def hello_world():         #    hello word isismli fonsiyon çalışacak
#   #  icerik= "<p>Hello, World</p>"       # 
#    # icerik += '<a href="/dogukan">dogukanın sayfası için tıkayın</a>' 
#     # return icerik




# @app.route("/dogukan")            #    anasayfa açıldığında ne yapayım
# def dogukan():         #    hello word isismli fonsiyon çalışacak
#     icerik = "<h1>Doğukan in VİP sayfasi</h1>"  
#     icerik += '<a href="/">anasayfa için tıkta </a>'
#     return icerik 

@app.route("/")            #    anasayfa açıldığında ne yapayım
def hello_world():         #    hello word isismli fonsiyon çalışacak
     if "ad" in session: 
          return render_template("index.html") # html sayfasına yönlendiriyor
     else:
          return render_template("login.html")


@app.route("/dogukan")            #    anasayfa açıldığında ne yapayım
def dogukan():                                           #    hello word isismli fonsiyon çalışacak
     return render_template("dogukan.html")              # html sayfasına yönlendiriyor

@app.route("/kaydol")                                    #    anasayfa açıldığında ne yapayım
def kaydol():                                            #    hello word isismli fonsiyon çalışacak
     return render_template("kaydol.html")               # html sayfasına yönlendiriyor

@app.route("/kayitbilgileri",methods=["post"])           #    anasayfa açıldığında ne yapayım post  gizli
def kayit():                   
     isim = request.form["isim"]
     email= request.form["email"]
     sifre = request.form["sifre"]
     baglanti = sqlite3.connect("veriler.db")           #    veriler.bd isimli bir veri tabanı yaratır
     sorgu = f"SELECT * FROM kullanicilar WHERE ad = '{isim}' "
     imlec = baglanti.cursor()
     imlec.execute(sorgu)
     kayitlar = imlec.fetchall()                        #        .fetchall() tüm kayıtlar gelir 
     if len(kayitlar) == 0:
          sorgu = f"INSERT INTO kullanicilar VALUES ('{isim}','{email}','{sifre}')"
          imlec.execute(sorgu)
          baglanti.commit()
          return render_template("index.html")
     else:
          return render_template("kaydol.html", hata="kullanici zaten kayıtlı")



@app.route("/login")                                   #    login açıldığında ne yapayım
def login():                                           #    hello word isismli fonsiyon çalışacak
     return render_template("login.html") 

@app.route("/loginbilgileri",methods=["post"])         # anasayfa açıldığında ne yapayım post  gizli
def login_kontrol():                   
     isim = request.form["isim"]
     sifre = request.form["sifre"]
     baglanti = sqlite3.connect("veriler.db")          #  veriler.bd isimli bir veri tabanı yaratır
     sorgu = f"SELECT * FROM kullanicilar WHERE ad = '{isim}' AND  sifre='{sifre}' "
     imlec = baglanti.cursor()
     imlec.execute(sorgu)                              # sorguyu çalıştırır
     kayitlar = imlec.fetchall()                      # .fetchall() tüm kayıtlar gelir 
     baglanti.close
     if len(kayitlar) == 0:
          return render_template("login.html",hata = "kullanici bilgileri hatali")
     else:
          session["ad"] = isim
          session["sifre"] = sifre
          return redirect("/")

@app.route("/cikis")                                   #    anasayfa açıldığında ne yapayım
def cikis():                                           #    hello word isismli fonsiyon çalışacak
     session["ad"]= None
     session["sifre"]= None
     return redirect("/login")
     


@app.route("/urunler")                                   #    anasayfa açıldığında ne yapayım
def urunler():  
     baglanti = sqlite3.connect("veriler.db")          #  veriler.bd isimli bir veri tabanı yaratır
     sorgu = "SELECT * FROM urunler"
     imlec = baglanti.cursor()
     imlec.execute(sorgu)                              # sorguyu çalıştırır
     kayitlar = imlec.fetchall()                       # .fetchall() tüm kayıtlar gelir 
     baglanti.close()
     return render_template("urunler.html", urunler = kayitlar)



@app.route("/urunler/sil/<id>")                                   #    anasayfa açıldığında ne yapayım
def urun_sil(id):  
     baglanti = sqlite3.connect("veriler.db")          #  veriler.bd isimli bir veri tabanı yaratır
     sorgu = f"DELETE FROM urunler WHERE id={int(id)}"
     imlec = baglanti.cursor()
     imlec.execute(sorgu)
     baglanti.commit()  
     baglanti.close()
     return redirect ("/urunler")      



@app.route("/urunler/guncelle/<id>")                                   #    anasayfa açıldığında ne yapayım
def urun_guncelle(id):  
     baglanti = sqlite3.connect("veriler.db")          #  veriler.bd isimli bir veri tabanı yaratır
     sorgu = f"SELECT * FROM urunler WHERE id={int(id)}"
     imlec = baglanti.cursor()
     imlec.execute(sorgu)                              # sorguyu çalıştırır
     kayit = imlec.fetchone()                       # .fetchall() tüm kayıtlar gelir 
     baglanti.close()     
     return render_template ("urun_guncelle.html", urun = kayit)



@app.route("/urunler/guncelle" ,methods=["post"])                                   #    anasayfa açıldığında ne yapayım
def urun_kaydet():  

     id = request.form["id"]
     kod = request.form["kod"]
     ad = request.form["ad"]
     fiyat = request.form["fiyat"]
     baglanti = sqlite3.connect("veriler.db")          #  veriler.bd isimli bir veri tabanı yaratır
     sorgu = f"UPDATE urunler SET kod = '{kod}' , ad= '{ad}', fiyat = {float(fiyat)} WHERE id={int(id)}"
     imlec = baglanti.cursor()
     imlec.execute(sorgu)                              # sorguyu çalıştırır
     kayit = imlec.fetchone()                       # .fetchall() tüm kayıtlar gelir 
     baglanti.commit()
     baglanti.close()     
     return redirect("/urunler")




@app.route("/urunler/urun_ekle",methods=['GET','POST'])                                   #    anasayfa açıldığında ne yapayım
def urun_ekle():  
     if request.method == "POST":
          ad = request.form["ad"]
          fiyat = request.form["fiyat"]

          baglanti = sqlite3.connect("veriler.db")          #  veriler.bd isimli bir veri tabanı yaratır
          imlec = baglanti.cursor()

          import random
          semboller="0123456789abcdefghjklmnoprstABCDEFGHJKLMNOUPRST" 
          urun_kodu = "".join(random.choices(semboller , k = 5))
          
          sorgu = f"INSERT INTO urunler (kod,ad,fiyat) VALUES ('{urun_kodu},'{ad}',{float(fiyat)})"
          
          imlec.execute(sorgu)                              # sorguyu çalıştırır
          baglanti.commit()
          baglanti.close()     
          return redirect("/urunler")
     else:
          return render_template("urun_ekle.html")
     
app.run(debug=True)               # program yayınlayacaksak debub false yapmamız gerek