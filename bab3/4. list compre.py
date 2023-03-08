# angka = [1,2,3,4,5,6,7,8,9,10]
# angkakuadrat = []

# for x in angka:
#     if x % 2 == 0:
#         angkakuadrat.append(x*x) 

# print (angkakuadrat)


# angka = [1,2,3,4,5,6,7,8,9,10]
# angkakuadrat = [x*x for x in angka]
# print (angkakuadrat)

angka = [1,2,3,4,5,6,7,8,9,10]
angkakuadrat = [x*x for x in angka if x % 2 == 0]
print (angkakuadrat)