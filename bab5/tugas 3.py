import csv
def menu():
    print("============================")
    print("Selamat Datang Pilih Menu :")
    print("1. Registrasi")
    print("2. Login")
    print("3. Selesai")
    print("============================") 
    
    pilih = int(input("Masukkan Keperluan : "))
    
    if pilih == 1:
         regis()
    elif pilih == 2:
          login()
    elif pilih == 3:
          selesai()
    else:
        print("Pilihan tidak ada")
        print("\n")
        menu()  

def regis():
    print("")
    print("***************************************")
    print("Selamat Melakukan Registrasi")  
    nama        = input("Masukkan Nama Anda : ")
    password    = input("Masukkan password Anda : ")
    print("***************************************")
    print("Apakah Anda user admin atau bukan ?")
    print("0. User")
    print("1. Admin")
    print("***************************************")   
    keyregis    = int(input("Pilih Hak Akses Anda :"))

    if keyregis == 0:
        regisguest(nama)
        simpanregis(nama, password, keyregis)
    elif keyregis == 1:
        regisadmin(nama)
        simpanregis(nama, password, keyregis)
    else:
        print("Pilihan tidak ada")
        regis()              

def regisguest(nama):
    print ("")
    print ("***Selamat Datang User " + nama +" ***")
    menu()
    
def regisadmin(nama):
    kodeadminregis = str(input("Masukan Kode Rahasia : "))
    if kodeadminregis == "iam god":
        print("***Selamat Datang Admin " + nama +" ***" ) 
    else:
        print ("Anda Bukan Admin")    
    menu() 
  
def simpanregis(nama, password, keyregis):
    judul = ["nama", "password", "keyregis"] 
    isi = {"nama" : nama, "password": password, "keyregis": keyregis}
    with open('users.csv','a', newline='') as file:
        writer = csv.DictWriter(file, delimiter = ';' , fieldnames=judul) 
        writer.writeheader()
        writer.writerow (isi)

def login():
    print("")
    print("#########################################")
    print("Silahkan Login")  
    nama        = input("Masukkan Nama Anda : ")
    password    = input("Masukkan password Anda : ")
    print("#########################################")
    print("Login Sebagai")
    print("0. User")
    print("1. Admin")
    print("#########################################")
    keylogin    = int(input("Pilih Hak Akses Anda :"))
    
    if keylogin == 0:
        loginguest(nama)
        simpanlogin(nama, password, keylogin)
    elif keylogin == 1:
        loginadmin(nama)
        simpanlogin(nama, password, keylogin)
    else:
        print("Pilihan tidak ada")
        login()
    
def loginguest(nama):
    print ("###Login Berhasil User " + nama +" ###")   
    file = open('hello.txt','w')
    file.write("Selamat Datang dan Selamat Bergabung User")
    file.close()
    
    with open('hello.txt', 'r') as file:
        print("")
        print("Pesan Dari Admin : " , file.read())
    menu()
    
def loginadmin(nama):
    kodeadminlogin = str(input("Masukan Kode Rahasia : "))
    if kodeadminlogin == "iam god":
        print("###Login Berhasil Admin " + nama +" ###") 
        
        file = open('hello.txt','w')
        pesanbaru = str(input("Ubah Pesan : "))
        file.write(pesanbaru)
        file.close()
        
        with open('hello.txt', 'r') as file:
            print("Pesan Baru : ",file.read())
            print ("")
    else:
        print ("***Anda Bukan Admin***")
    menu()   

def simpanlogin(nama, password, keylogin): 
    isi = {"nama" : nama, "password": password, "keylogin": keylogin}
    judul = ["nama", "password", "keylogin"] 
    
    with open('users.csv','a', newline='') as file:
          writer = csv.DictWriter(file, delimiter = ';' , fieldnames=judul) 
          writer.writeheader()
          writer.writerow (isi) 

def selesai():
    print (" ")
    print ("Terima Kasih")

menu () 

## proses loooping penyimpanan
## gabung di 1 file login sama regis

############################################################
# #write di csv cari tempat penyimpanan
# with open('tes.csv','w', newline='') as file:
#     judul = ["nama", "password", "keyregis"]
#     writer = csv.DictWriter(file, fieldnames=judul)
#     writer.writeheader()
#     # writer.writerow({'nama':"Budi Budiman", 'tgl':"17/11/2000"})
#     writer.writerow ({"nama" : nama, "password": password, "keyregis": keyregis})

# with open('tes.csv', 'r') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row['nama'], row['password'], row['keyregis'])
############################################################    

# def simpan(nama, password, keyregis, keylogin,):    
#     with open('gabung.csv','w', newline='') as file:
#         judul = ["nama", "password", "keyregis", "keylogin"]
#         writer = csv.DictWriter(file, fieldnames=judul, delimiter = '\t')
#         writer.writeheader()
#         writer.writerow ({"nama" : nama, 
#                           "password": password,
#                           "keyregis": keyregis,
#                           "keylogin": keylogin,})

# def simpan(nama, password, keyregis, keylogin,): 
#     isi = {"nama" : nama, "password": password, "keyregis": keyregis}
#     isi1 = {"nama" : nama, "password": password, "keylogin": keylogin}
    
#     judul = ["nama", "password", "keyregis", "keylogin"]
    
#     with open('gabung.csv','a', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=judul, delimiter = ';')
#         writer.writeheader()
#         writer.writerow (isi)
#         writer.writerow (isi1)
