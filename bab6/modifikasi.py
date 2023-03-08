from collections import Counter

def remov_duplicates(nama):
    nama = nama.split(" ")
    for i in range(0, len(nama)):
        nama[i] = "".join(nama[i])
    UniqW = Counter(nama)
    s = " ".join(UniqW.keys())
    print (s)

if __name__ == "__main__":
    nama = input("Masukkan Nama Anda : ")
    remov_duplicates(nama)