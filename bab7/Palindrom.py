def check(original, edited):
    print(original)
    if edited[::-1] == edited:
        print ('Palindrom')
    else :
        print ('Bukan Palindrom')

def reversed(word):   
    original = word
    edited = word
    check(original, edited)
    
n = int(input("Jumlah Pemerikasaan kata: "))
    
for i in range(n):
    word = input("Tuliskan sebuah kata : ")     
    reversed(word)