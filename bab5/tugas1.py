menu = input ("Masukkan keperluan anda (regis/login): ")

if menu == "regis":
    nama        = input("Masukkan Nama Anda : ")
    password    = input("Masukkan Passwor Anda : ")
    keyword     = input("Masukkan Keyword Anda : ")
    
    if keyword == "iam god":
        print("Selamat datang "  + nama + " anda berhasil login sebagai admin")
    else:
        print ("anda bukan admin")
   
elif menu == "login":
    nama        = input("Masukkan Nama Anda : ")
    password    = input("Masukkan Passwor Anda : ")
    print ("selamat datang user")

#nyambungin antara data base sama login
