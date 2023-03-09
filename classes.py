class Bank:
    def krediBasvur(self):
        print("Kredi Başvurusu Yapıldı.")
    def krediHesapla(self):
        print("Kredi Hesaplaması Yapıldı.")
bank = Bank()
bank.krediBasvur()
bank.krediHesapla()

class Mat:
    def __init__(self, sayi1, sayi2): #constructor
        self.s1 = sayi1
        self.s2 = sayi2
        print("Fonksiyon Çalıştı")
    def topla(self):
        return self.s1 + self.s2
    def fark(self):
        return self.s1 - self.s2
    def carp(self):
        return self.s1 * self.s2
    def oran(self):
        return self.s1 / self.s2


matematik = Mat(14,7)

##
#print("Toplam:", (matematik.topla(sayi1=5, sayi2=8)))
#print("Carpim", (matematik.carp(sayi1=9, sayi2=8)))
#print("Fark :", (matematik.fark(sayi1=9, sayi2=10)))
#print("Bölüm : ", (matematik.oran(sayi1=10, sayi2=8)))
sonucToplam = matematik.topla()
sonucCarpim = matematik.carp()
sonucFark = matematik.fark()
sonucOran = matematik.oran()

print("Toplam Sonucu : ", sonucToplam)
print("Carpim Sonucu : ", sonucCarpim)
print("Fark Sonucu : ", sonucFark)
print("Bolum Sonucu : ", sonucOran)