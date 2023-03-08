class buruh:
    def __init__(self, nama, nip, status, gajih):
        self.nama = nama
        self.nip = nip
        self.status = status
        self.gajih = gajih
    
    def perkenalan(self):
        print("Nama saya : " + self.nama + 
              " nip : " + self.nip)
              
    
    def kelayakan(self):
        print(" status : " + self.status + 
              " gajih : " + self.gajih)

nama_karyawan = input(str('nama: '))
nip_karyawan = input('nip: ')
status_karyawan = input(str('status: '))
gajih_karyawan = input('gajih: ')

for i in range(nama_karyawan, nip_karyawan, status_karyawan, gajih_karyawan):
    karyawan = buruh(nama_karyawan, nip_karyawan)
    karyawan.perkenalan()
    karyawan.kelayakan()

hapus = int(input('apa akan menghapus data (0 = tidak /1 = ya):'))
for i in range(hapus):
    if hapus == 1 :
        del karyawan
    else :
        break
        print("terimakasih")



# karyawan1 = buruh("Tom", "1360010007", "kontrak", "1000")
# karyawan2 = buruh("Jerry", "1360010008", "tetap", "5000")

# karyawan1.perkenalan()
# karyawan2.perkenalan()


# class Robot:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight

#     def introduce_self(self):
#         print("My name is " + self.name + self.color)


# r1 = Robot("Tom", "red", 30)
# r2 = Robot("Jerry", "blue", 40)

# r1.introduce_self()
# r2.introduce_self()