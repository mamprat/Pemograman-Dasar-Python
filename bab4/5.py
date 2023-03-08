nama = str(input("Masukkan Nama Anda : "))
asal = str(input("Masukkan Alamat Anda : "))
tinggi = str(input("Masukkan Tinggi Anda : "))
berat = str(input("Masukkan Berat Anda : "))

tinggi1 = int(tinggi)
bin_tinggi = bin(tinggi1)
berat1 = int(berat)
bin_berat = hex(berat1)

perkenalan = 'Halo, saya %s dari %s'
perkenalan1 = 'Halo, saya {nama} dari {asal}'
perkenalan2 = 'Tinggi saya {} dan berat saya {}'

print("")
print("================================")
print("Data Diri")
print("Nama     :",nama,"  ",'imam' in nama, nama[1])
print("Asal     :",asal,"",'subang' in asal, asal[0:7])
print("Tinggi   :",tinggi,"   ",'170' in tinggi, bin_tinggi)
print("Berat    :",berat,"    ",'60' in berat, bin_berat)
print("================================")
print("")

print(f'Perkenalkan saya {nama} dari {asal}')
print(perkenalan % (nama, asal))
print(perkenalan1.format(nama = 'Imam', asal = 'Subang'))
print(perkenalan2.format(tinggi, berat))
