def menu():
    print("=========================")
    print("Selamat Datang")
    print("1. Registrasi")
    print("2. Login")
    print("========================")  
    pilih = int(input("Masukkan pilihan : "))
    print("\n")
    
    if pilih == 1:
         regis()
    elif pilih == 2:
         login()
    else:
        print("Pilihan tidak ada")
        print("\n")
        menu()    
   
#registrasi data
def regis():
    nama        = input("Masukkan Nama Anda : ")
    password    = input("Masukkan Passwor Anda : ")
    keyword     = input("Masukkan Keyword Anda : ")    
    if keyword == "iam god":
        print("Selamat datang "  + nama + " anda berhasil login sebagai admin")
    else:
        print ("anda bukan admin")
    menu ()
 
#login data
def login():
    nama        = input("Masukkan Nama Anda : ")
    password    = input("Masukkan Passwor Anda : ")
    print ("selamat datang user")
    menu ()
menu ()   



   

