number = int(input('Masukkan angka : '))
total = 0
for i in range(number+1):
    if i%3 == 0:
        total = total + i
    elif i%5 == 0:
        total = total + i
    print(total, i)
print('Totalnya sebanyak ', total)
