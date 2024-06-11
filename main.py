import pandas as pd
from hemsire import Hemsire
from personel import Personel
from hasta import Hasta
from doktor import Doktor

def main():
    try:
        # Personel oluşturma ve bilgilerini yazdırma
        personeller = [
            Personel(254, "Uygar", "Tüfekçi", "Mutfak", 3500),
            Personel(152, "Melis", "Beceren", "Yoğun Bakım", 7500)
        ]
        for personel in personeller:
            print(personel)

        # Doktor oluşturma ve bilgisini yazdırma
        doktorlar = [
            Doktor(23, "Bukre", "Canpolat", "Radyoloji", 44600, "Radyolog", 2, "Konak Hastane"),
            Doktor(10, "Anıl", "Hala", "Fizik Tedavi", 83000, "Fizik Tedavi", 5, "Karşıyaka Hastane"),
            Doktor(32, "Pelin", "Satar", "Mutemetlik", 65000, "Nöroloji", 19, "Urla Hastane")
        ]
        for doktor in doktorlar:
            print(doktor)

        # Hemşire oluşturma ve bilgisini yazdırma
        hemsireler = [
            Hemsire(45, "Doğukan", "Diker", "Üroloji", 38000, 30, "Ürolog Sertifikası", "Konak Hastane"),
            Hemsire(33, "Ilgaz", "Turhan", "Tıbbi Patoloji", 18000, 28, "Tıbbi Patoloji Sertifikası", "Karşıyaka Hastane"),
            Hemsire(85, "Furkan", "Biçer", "Radyoloji", 20000, 36, "Radyolog Sertifikası", "Urla Hastane")
        ]
        for hemsire in hemsireler:
            print(hemsire)

        # Hasta oluşturma ve bilgi yazdırma
        hastalar = [
            Hasta(3453, "Rana", "Biçen", "23.12.1956", "Soğuk algınlığı", "genel tedavi"),
            Hasta(3402, "Şimal", "Uyaran", "06.10.2003", "Zehirlenme", "genel tedavi"),
            Hasta(4023, "Eylül", "Yukarıca", "20.02.2000", "Covid-19", "bireysel tedavi")
        ]
        for hasta in hastalar:
            print(hasta)

        # Dataframe
        # Personel, doktor, hemşire, hasta, verilerini toplama
        personel_data = [[p.get_ad(), p.get_soyad(), p.get_departman(), p.get_maas(), None, None, None, None, None] for p in personeller]
        doktor_data = [[d.get_ad(), d.get_soyad(), d.get_departman(), d.get_maas(), d.get_uzmanlik(), d.get_deneyim_yili(), None, None, None] for d in doktorlar]
        hemsire_data = [[h.get_ad(), h.get_soyad(), h.get_departman(), h.get_maas(), None, None, None, None, None] for h in hemsireler]
        hasta_data = [[hs.get_ad(), hs.get_soyad(), None, None, None, None, hs.get_hastalik(), hs.get_tedavi(), hs.get_dogum_tarihi()] for hs in hastalar]

        # Tüm verileri birleştirme kısmı
        data = personel_data + doktor_data + hemsire_data + hasta_data

        # DataFrame oluşturma df diye kısalttık
        #columns'u DataFrame'deki sütun adlarını göstermek ve değiştirmek için kullanırız.
        df = pd.DataFrame(data, columns=["Ad", "Soyad", "Departman", "Maaş", "Uzmanlık", "Deneyim Yılı", "Hastalık", "Tedavi", "Doğum Tarihi"])

        # Boş değerleri doldurma
        df.fillna(0, inplace=True)

        #groupby metodu pandas'tan gelen sıralama için kullanılan bir metottur.
        #size'ı da boyutunu yani içindeki eleman sayısı için yazıyoruz.
        print("Doktorları uzmanlık alanlarına göre gruplandırma:\n", df[df["Uzmanlık"] != 0].groupby("Uzmanlık").size())
        print("5 yıldan fazla deneyime sahip olan doktorlar:\n", df[df["Deneyim Yılı"] > 5])

        #sort_values ile sıralamayı okunabilir hale getirir yani alfabetik sıraladık bir pandas metodudur.
        print("Hasta adına göre alfabetik sıralama:\n", df.sort_values("Ad"))
        print("Maaşı 7000 TL üzerinde olan personeller:\n", df[df["Maaş"] > 7000])
        #buradaki format tarihin day month year yani gün ay yıl şeklinde olmasını sağlar
        #buradaki errors'da hataya nasıl karşılık verilecek söyler "NaT" yani not a time şeklinde gösterir.
        df['Doğum Tarihi'] = pd.to_datetime(df['Doğum Tarihi'], format='%d.%m.%Y', errors='coerce')
        #buradaki dt pandastan date time anlamına gelir ve kolayca sıralamayı sağlar
        print("1990 ve sonrası doğumlu hastalar:\n", df[df['Doğum Tarihi'].dt.year >= 1990])

        print("Yeni DataFrame:\n", df[["Ad", "Soyad", "Departman", "Maaş", "Uzmanlık", "Deneyim Yılı", "Hastalık", "Tedavi", "Doğum Tarihi"]])

    #burada Exception bir hata türüdür burada ise tüm hata türlerini yakalayabildiği için kullandık.
    except Exception:
        print("Bir hata oluştu")

# main'i çağırdı
main()
