a = list((input("Kata yang diinginkan : ")))
b = int(input("Jumlah manipulasi kata : "))

def swap(x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp

def rotate(x, y):
    z = int(y)
    for i in range (x, y+1):
        for j in range (x, z):
            swap(j, j+1)
        z-=1

for i in range (b):
    print("Manipulasi kata ", a)
    c = int(input("Angka 1 : "))
    d = int(input("Angka 2 : "))
    e = int(input("Metode : "))
    if e == 1:
        swap(c, d)
    elif e == 2:
        rotate(c, d)
    print(a)