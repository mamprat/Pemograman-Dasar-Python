class Orang:
    total = 0
    def __init__(self, nama):
        self.nama = nama  
        Orang.total += 1
    
    def __del__(self):
        Orang.total -= 1
    
    def katakanHalo(self):
        print ('Halo, nama saya %s, apa kabar?' % self.nama)
    
    def total_populasi(cls):
        print ('Total Orang %s' % cls.total)
    total_populasi = classmethod(total_populasi)

org = Orang('budi')
org.katakanHalo()
Orang.total_populasi()

org2 = Orang('andi')
org2.katakanHalo()
Orang.total_populasi()
    
#penambahan    
jumlah = int(input('jumalah data:'))
for i in range(jumlah):
    masukan = input('masukan namamu: ')
    org3 = Orang (masukan)
    org3.katakanHalo()
    Orang.total_populasi()
    Orang.total += 1

#hapus
hapus = int(input('data yang dihapus (0 = tidak /1 = ya):'))
for i in range(hapus):
    if hapus == 1 :
        del org
        del org2
    else :
        break
Orang.total_populasi()

#ubah
