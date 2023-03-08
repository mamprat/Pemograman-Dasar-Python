list_npm = []
list_nama = []
list_studi = []
list_ipk = []

class datamahasiswa :
    def __init__(self,npm,nama,studi,ipk):
        self.npm = npm
        list_npm.append(self.npm)
        self.nama = nama
        list_nama.append(self.nama)
        self.studi = studi
        list_studi.append(self.studi)
        self.ipk = ipk
        list_ipk.append(self.ipk)
       
    def tampildata(self):
        n = 0
        print("\nJumlah Mahasiswa Yang Sudah Terinput : ",x)
        for i in range(x):
            n+=1
            if list_ipk[i] >= 3.50:
                print("\n------mahahsiswa ke",n,"------")
                print("NPM Mahasiswa : ",list_npm[i])
                print("Nama Mahasiswa : ",list_nama[i])
                print("Prodi Mahasiswa : ",list_studi[i])
                print("IPK Mahasiswa : ",list_ipk[i])
                print("--------------------------------")
            else:
                i+=1
        print("Bila tidak tampil maka kurang")

stop = False
x = 0
while(not stop):
    inputnpm = input("Masukan NPM : ")
    inputnama = input("Masukan Nama : ")
    inputstudi = input("Masukan Studi : ")
    inputipk = float(input("Masukan IPK : "))
    mahasiswa = datamahasiswa(inputnpm,inputnama,inputstudi,inputipk)
    x+=1
    ulang = input ("apakah ingin input kemabali (y/t) ? : ")
    if ulang == 't':
        stop = True

mahasiswa.tampildata()

# class Hero:

# 	def __init__(self,name,health,attackPower,armorNumber):
# 		self.name = name
# 		self.health = health
# 		self.attackPower = attackPower
# 		self.armorNumber = armorNumber

# 	def serang(self, lawan):
# 		print(self.name + ' menyerang ' + lawan.name )
# 		lawan.diserang(self, self.attackPower)

# 	def diserang(self, lawan, attackPower_lawan):
# 		print(self.name + ' diserang ' + lawan.name)
# 		attack_diterima = attackPower_lawan/self.armorNumber
# 		print('serangan terasa : ' + str(attack_diterima))
# 		self.health -= attack_diterima
# 		print('darah ' + self.name + ' tersisa ' + str(self.health))


# sniper = Hero('sniper',100,10,5)
# rikimaru = Hero('rikimaru',100,20,10)

# sniper.serang(rikimaru)
# print("\n")
# rikimaru.serang(sniper)
# print("\n")
# rikimaru.serang(sniper)
# print("\n")
# rikimaru.serang(sniper)
# print("\n")
# rikimaru.serang(sniper)
# print("\n")
# rikimaru.serang(sniper)