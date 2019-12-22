# # dict = {'mangga':90,'manggis':100}
# # hasil = dict['mangga'] * dict['manggis']
# # print(hasil)

# nama ='yanuar'
# NIM ='18.11.2034'

# def data_diri ():
#     nama = 'sadyatma'
#     NIM = '18.11.2035'

#     print('Nama = %s' )  % nama
#     print('Nim = %s') % NIM

# # print('nama = ') % nama
# # print('NIM =  ') % NIM

# #data_dirip

# def hitung(x):
#     return x+x

# print (hitung(2))

# #menghitung luas segitiga
# def luassegitigs(alas, tinggi):
#     luas = alas * tinggi
#     return luas

# print (luassegitigs (6,8)) 

# my_password =[]

# def password(x):
#     if len(x) >= 8:
#         print('Password berhasil dibubat, jumlah karakter',len(x))
#     else:
#         print('Password gagal dibubat, jumlah karakter',len(x))


# def luas_lingkaran(r, phi = 3.14):
#     return phi * (r * r)
#     print (luas_lingkaran)

# luas_lingkaran(7)

# #rumus menghitung luas lingkaran
# #menggnakan default value pada parameter

# def luas_lingkaran(r,phi=3.14):
#     return phi * (r * r)

# def volume_balok(p,l,t):
#     print('panjang :',p,'lebar :',l,'tinggi :' ,t)
#     return p*l*t

# def total(*size,**nilai):
#     """fungsi yang menerima variabel argumen"""
#     for i in size:
#         print('ukuran sepatu :',i)
        
#     for key, value in nilai.items():
#         print(key.capitalize(),value)

# total(42,43,32,36, david=70 , yanuar=100, peby=80,sabil=89)


# count = 0

# while count < 5:
#     print ('saya sedang belaljar python')

#     count = count+1

# # #membuat fungsi menebak angka
# angka = 23
# running = True

# while running:
#     tebak = int(input('masukan angka : '))

#     if tebak == angka:
#         print('jawaban kamu benar')
        
#         running = False
#     elif tebak < angka:
#         print('tidak, angka lebih besar dari :')
#     else:
#         print('tidak, angka lebih kecil dari :')
# else:
#     print('selamat anda benar')
    

# print('SLESAI')

#
# running = True
# while True:


#     subjek = input('ketikan :')
#     if subjek == 'keluar':
#         break
#     print('panjag karakter :',len(subjek))
# print('selsai')

#
# while True:


#     subjek = input('ketikan :')
#     if subjek.lower() == 'keluar':
#         break
#     #menggunakan lower untuk menjadikan semua inputan menjadi huruf kecil
#     print('panjaga karakter :',len(subjek))
# print('selsai')

#continue
# running = True
# while True:


#     subjek = input('ketikan :')
#     if subjek.lower() == 'keluar':
#         break
#     elif len(subjek) < 3:
#         print('karakter terlau pendek')
#         continue
#print('karakter sudah cukup panjag')

# list_belanja =['TAS','buku','sepeda','telor goreng','indomie telor']
# print('jumlah list adalah:',len(list_belanja))
# for i in list_belanja:
#     print(i)

list_belanja =['TAS','buku','sepeda','telor goreng','indomie telor']
print('jumlah list adalah:',len(list_belanja))
for i in list_belanja:
    print(i, end=' ')
#memberikan huruf kapital pada awal kata
list_belanja =['TAS','buku','sepeda','telor goreng','indomie telor']
print('jumlah list adalah:',len(list_belanja))
for i in list_belanja:
    print(i,end=' ')
for i in list_belanja:
    print(i.capitalize(),end=' ')
#menampilkan urutan list
list_belanja =['TAS','buku','sepeda','telor goreng','indomie telor']
print('jumlah list adalah:',len(list_belanja))
for i in list_belanja:
    print(i,end=' ')
print('\n')
list_belanja.sort()
print('diurutkan dari A-Z:', end=' ')
print('\n')
list_belanja.append()
print('setelah ditambah :',end=' ')

list_belanja.remove('PC')
print('setelah ditambahkan', end=' ')
