# lat34.py

class Orang:
    # variabel class, untuk menghitung jumlah orang
    total = 0
    def __init__(self, nama):
        # inisiasi data, data yang dibuat pada self merupakan variabel obyek
        self.nama = nama

        # ketika ada orang yang dibuat, tambahkan total orang
        Orang.total += 1

    def __del__(self):
        # kurangi total orang jika obyek dihapus
        Orang.total -= 1

    def katakanHalo(self):
        print ('Halo, nama saya %s, apa kabar?' % self.nama)

    def total_populasi(cls):
        print ('Total Orang %s' % cls.total)

    # method class
    total_populasi = classmethod(total_populasi)

org = Orang('budi')
org.katakanHalo()
Orang.total_populasi()

org2 = Orang('andi')
org2.katakanHalo()
Orang.total_populasi()

print ('obyek dihapus')
del org
del org2

Orang.total_populasi()