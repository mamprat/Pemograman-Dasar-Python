kampus = 'FILKOM UNIVERSITAS BRAWIJAYA'
perkenalan = 'Halo, saya %s dari %s'
perkenalan1 = 'Halo, saya {nama} dari {asal}'
perkenalan2 = 'Saya suka makan {} dan minum {}'
nama = 'Imam Pratama'
asal = 'Subang'
jurusan = ['Teknik Komputer', 'Teknik Informatika', 'Magister Ilmu Komputer']
print('UNIVERSITAS' in kampus)
print('TEKNIK' in kampus)
print(kampus[9])
print(kampus[0:7])
print(kampus[: -5])
print(kampus[-3:])
print(len(kampus))
print(perkenalan % ('Imam Pratama', 'Subang'))
print(perkenalan1.format(nama = 'Imam Pratama', asal = 'Subang'))
print(perkenalan2.format('Sayur Asem', 'Air Putih'))
print(f'Perkenalkan saya {nama} dari {asal}')