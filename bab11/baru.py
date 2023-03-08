from time import *
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
        print("Ulangi Prosedur Kembali")

def selesai():
    print ("Terima Kasih")
    
def regis():
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
        simpan(nama, password, keyregis)
        regisguest(nama)
    elif keyregis == 1:
        simpan(nama, password, keyregis)
        regisadmin(nama)            
    else:
        print("****Ulangi Registrasi*****")
        regis()
        
def regisguest(nama):
    print ("")
    print ("***Selamat Datang User " + nama +" ***")
    menu()
    
def regisadmin(nama):
    kodeadminregis = str(input("Masukan Kode Rahasia : "))
    if kodeadminregis == "iam god":
        print("***Selamat Datang Admin " + nama +" ***" )
        menu()
    else:
        print("*******Kode Rahasia Salah*******")
        
def simpan(nama, password, keyregis):
    data=[nama, password, keyregis]
    with open('users.csv', 'a',newline='') as csvfile: 
        writer=csv.writer(csvfile,delimiter = ';')
        writer.writerow(data)    

def login():
    print("")
    print("#########################################")
    print("Silahkan Login")  
    nama        = input("Masukkan Nama Anda : ")
    password    = input("Masukkan password Anda : ")
    print("#########################################")
    
    with open('users.csv','r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=";")
        for row in csv_reader :         
            if row [0] == nama and row [2] == '0':
                loginguest (nama)   
            elif row [0] == nama and row [2] == '1':   
                loginadmin (nama)   
                
def loginguest():
    print ("###Login Berhasil User " + nama +" ###")      
    selesai() 
    
def loginadmin():
    kodeadminlogin = str(input("Masukan Kode Rahasia : "))
    if kodeadminlogin == "iam god":
        print("###Login Berhasil Admin " + nama +" ###") 
    else:
        print ("***Anda Bukan Admin***")  


# start = time()
# loginguest(nama)
# loginadmin(nama)
# end = time()

# start = time()
# t1 = loginguest()
# t2 = loginadmin()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# end = time()

menu () 

# print("Waktu mulai             :", start)
# print("Waktu selesai           :", end)
# print("Durasi eksekusi program :", end-start)



