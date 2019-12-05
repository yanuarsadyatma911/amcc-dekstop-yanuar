# penjumlahan 
# Program Penjumlahan Dua Bilangan 
# Meminta inputan dari user 

bil1 = input('Masukkan bilangan pertama: ') 
bil2 = input('Masukkan bilangan kedua:  ') 

# Menjumlahkan bilangan 
jumlah = float (bil1) + float (bil2) 
# Menampilkan jumlah 
print('Jumlah {0} + {1} adalah {2}'.format(bil1, bil2, jumlah))

# Program python untuk menentukan bilangan prima atau tidak

# Meminta input bilangan dari user
num = int (input("Masukkan bilangan: "))

# bilangan prima harus lebih besar dari 1

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "bukan bilangan prima")
            print(i, "kali", num//i, "=", num)
            break
    else:
        print(num,"adalah bilangan prima")

# bila bilangan kurang atau sama dengan satu

else:
    print(num, "bukan bilangan prima")