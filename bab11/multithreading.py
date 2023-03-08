from threading import*

def persegi(sisi):
	print("Luas persegi :", sisi * sisi)

def kubus(sisi):
	print("Luas kubus :", sisi * sisi * sisi)

t1 = Thread(target=persegi, args=(10, ))
t2 = Thread(target=kubus, args=(10, ))

t1.start()
t2.start()

t1.join()
t2.join()

print("tau apaan")