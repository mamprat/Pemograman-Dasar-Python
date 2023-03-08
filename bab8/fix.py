list_nama = []
list_nip = []
list_status = []

class datakaryawan :
    def __init__(self,nama,nip,status):
        self.nama = nama
        list_nama.append(self.nama)
        self.nip = nip
        list_nip.append(self.nip)
        self.status = status
        list_status.append(self.status)

    def data(self):
        ke = 0
        print("\nJumlah Karyawan Yang Terinput : ",x)
        for i in range(x):
            ke+=1
            if list_status[i] == "kontrak":
                print("\n------Karyawan Yang Ke",ke,"------")
                print("Nama Karyawan : ",list_nama[i])
                print("NIP Karyawan : ",list_nip[i])
                print("Status Karyawan : ",list_status[i])
                print("--------------------------------")
                print("Selamat " + list_nama[i] + " Anda Mendapatkan Bonus")
            else:
                print("\n------Karyawan Yang Ke",ke,"------")
                print("Nama Karyawan : ",list_nama[i])
                print("NIP Karyawan : ",list_nip[i])
                print("Status Karyawan : ",list_status[i])
                print("--------------------------------")
                print("Mohon Maaf " + list_nama[i] + " Anda Tidak Mendapatkan Bonus")
                # i+=1                 
    
stop = False
x = 0
print("**Selamat Datang Silahkan Masukan Data**")
while(not stop):
    inputnama = input("Masukan Nama Karyawan : ")
    inputnip = input("Masukan NIP Karyawan : ")
    inputstatus = input("Masukan Status Karyawan : ")  
    karyawan = datakaryawan(inputnama,inputnip,inputstatus)  
    x+=1
    tambah = input ("Apakah Ingin Input Data Karyawan Kemabali (y/t) ? : ")
    if tambah == 't':
        stop = True  
karyawan.data()
