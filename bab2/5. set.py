s1 = {1,1,3,2,3,2,1}
s1a = s1.discard(1)
# s1b = s1[2]
# s1c = s1(2)

s2 = set('filkom universitas brawijaya')
s2a = s1.union(s2)

s3 = {4,5,4,7,7,6,5}
s3a = s3.add(8)
s3b = s1.intersection(s3)
s3c = s1.difference(s3)

print(s1)
print(s2)
print(s3)
print(s3a)
print(s1a)
print(s2a)
print(s3b)
print(s3c)
# print(s1b)
# # print(s1c)