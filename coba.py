# Membuat Fungsi
def salam():
    print ('Hello, Selamat Pagi')

## Pemanggilan Fungsi
salam()
salam()
salam()
salam()

def yanuar(panjang, lebar):
    luas = panjang * lebar
    print ('luas semua %f' % luas)

yanuar(10 , 12)

# rumus: sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

luas_persegi(12)

# membuat variabel global
nama = "DEKSTOP"
versi = ""

def help():
    # ini variabel lokal
    nama = "Programku"
    versi = "1.0.2"
    # mengakses variabel lokal
    print "Nama: %s" % nama
    print "Versi: %s" % versi


# mengakses variabel global
print "Nama: %s" % nama
print "Versi: %s" % versi

# memanggil fungsi help()
help()