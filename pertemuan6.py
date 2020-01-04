import os
def main():
    Pilihan = input('Masukkan Pilihan (B) Konversi Binner to Decimal, (S) Konversi Suhu. (B/S)? ')
    if Pilihan.title() == 'S':
        C = int(input('Masukkan Suhu dalam Celcius: '))
        X = input('Konversi ke K/R/F: ')
        konversi(C,X)
    elif Pilihan.title() == 'B':
        nilai_bin = int(input('Masukkan Angka Binner: '))
        bin_to_dec()
    else:
        print('Error!')

def konversi(C,X):
    if X.title() == 'K':
        K = C + 273
        print('%d Celcius itu %d Kelvin'%(C,K))
    elif X.title() == 'R':
        R = (4/5)*C
        print('%d Celcius itu %d Reamur'%(C,R))
    elif X.title() == 'F':
        F = ((9/5)*C) + 32
        print('%d Celcius itu %d Fahrenheit'%(C,F))
    else:
        print('ERROR!')
    konfirmasi()

def bin_to_dec():
    konfirmasi()

def konfirmasi():
    while True:
        ulang = input('Apakah anda ingin mengulangi?(y/t): ')
        if ulang.title() == 'Y':
            cls()
            main()
        elif ulang.title() == 'T':
            break
        break
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
if __name__ == '__main__':
    main()
