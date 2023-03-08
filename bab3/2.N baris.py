n =int(input("tinggi kertas:"))
m =int(input("lebar kertas:"))
l =int(input("lebar huruf:"))

for i in range(n):
    for j in range(m):
        if i < l or j < l or i >= n-l:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print('\n')
