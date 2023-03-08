n = int(input("Jumlah angka genap yang ingin disimpan: "))
i = 0
while i < n:
    nilai = int(input("Masukan angka: "))
    if nilai % 2 ==0:
        print (nilai)
        i += 1
    else:
        print("Bukan Angka Genap!")