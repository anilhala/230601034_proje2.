from personel import Personel  #personel.py'den Personel sınıfını alıyoruz

class Hemsire(Personel):  # Personel sınıfından hemşire sınıfını türetiyoruz
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    # Hemşirelere ait get ve set metotları

    def get_calisma_saati(self):
        return self.__calisma_saati

    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def get_sertifika(self):
        return self.__sertifika

    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika

    def get_hastane(self):
        return self.__hastane

    def set_hastane(self, hastane):
         self.__hastane = hastane

    def maas_arttir(self, oran):
        yeni_maas = self.get_maas() * (1 + oran) # Hemşirelerin maaşını arttır
        self.set_maas(yeni_maas)

    # Hemşirelere ait bilgileri yazdıran __str__ metodu
    def __str__(self):
        return f"{super().__str__()}, Çalışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"