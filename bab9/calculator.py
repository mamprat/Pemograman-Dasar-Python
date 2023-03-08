#INHERITANCE
class kalkulator:
    def __init__(self,pertama,kedua):
        self.pertama=pertama
        self.kedua=kedua
    def hasil(self):
        pass

class tambah(kalkulator):
    def __init__(self,pertama,kedua):
        super().__init__(pertama,kedua)
    def hasil(self):
        return self.pertama+self.kedua

class kurang(kalkulator):
    def __init__(self,pertama,kedua):
        super().__init__(pertama,kedua)
    def hasil(self):
        return self.pertama-self.kedua

class kali(kalkulator):
    def __init__(self,pertama,kedua):
        super().__init__(pertama,kedua)        
    def hasil(self):
        return self.pertama*self.kedua
    
class bagi(kalkulator):
    def __init__(self,pertama,kedua):
        super().__init__(pertama,kedua)     
    def hasil(self):
        return self.pertama/self.kedua

pilih=1
while pilih!=0:
    print("==========Masukan Angka==========")
    pertama=int(input("Angka Pertama : ",))
    kedua=int(input("Angka Kedua   : "))
    print("=================================")
       
    print("=====Perhitungan=====")
    print("0. Keluar")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("====================")   
    pilih=int(input("Masukan Pilihan: "))
    
    if pilih==1:
        a = tambah(pertama,kedua)
        print("Hasil : ",a.hasil())
    if pilih==2:
        b = kurang(pertama,kedua)
        print("Hasil :",b.hasil())
    if pilih==3:    
        c = kali(pertama,kedua)
        print("Hasil :",c.hasil())
    if pilih==4:
        d = bagi(pertama,kedua)
        try:
            print("Hasil :",d.hasil())
        except:
            print("Tidak Bisa Dibagi 0")