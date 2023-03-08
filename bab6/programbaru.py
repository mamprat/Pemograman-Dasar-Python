def menu():
    print("============================")
    print("Selamat Datang Pilih Menu :")
    print("1. List")
    print("2. Tuple")
    print("3. Dictionaries")
    print("4. Selesai")
    print("============================") 
    
    pilih = int(input("Masukkan Keperluan : "))
    
    if pilih == 1:
        List()
    elif pilih == 2:
        Tuple()
    elif pilih == 3:
        Dictionaries()
    elif pilih == 4:
        selesai()
    else:
        print("Ulangi Prosedur Kembali")

def selesai():
    print ("Terima Kasih")

def List():
    print("*****Data Mahasiswa*****")
    masukan =[]
    key = 0
    while key == 0:
        nama = list(input("Masukan Nama: " ))
        jurusan = input("Jurusan : " )
        masukan.append(["nama :",nama, "jurusan :",jurusan]) ##???
        pilihan = input ("Ingin Menambah Data Mahasiswa ? (Y/T)")
        if pilihan == "y":
            key==1
        else:
            print("Hasil Data: ", masukan)
            menu()        
            break

def Tuple():
    print("*****Data Mahasiswa*****")
    nama  = tuple(input("Masukan Nama Mahasiswa: " ))  
    print("Pisahkan Huruf :", nama)
    print("Jumlah Karakter: %d" % len(nama))  
    menu()

def Dictionaries():
    print("*****Data Mahasiswa*****")
    nama  = input("Masukan Nama : " )
    alias = input("Masukan Alias : " )
    masukan = dict({"Nama: " : nama, "Alias: ": alias})  

    pilihan = input ("Apa Data Mahasiswa Benar ? (Y/T)")
    
    if pilihan == "t":
        namabaru  = input("Masukan Nama Baru : " )
        aliasbaru= input("Masukan Alias Baru : " )
        masukanbaru = dict({"Nama: " : namabaru , "Alias: ": aliasbaru}) 
        masukan.update (masukanbaru)
        print("Hasil Data Baru: ", masukan) 
        menu()
    else:
        print("Hasil Data: ", masukan)   
        menu()
menu()