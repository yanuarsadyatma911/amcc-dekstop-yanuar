# def say_hi():
#     print('hi, ini merupakan module')


# __version__= '0.1'
import os
def mulai():
    pilihan = input('masukan pilihan anda')
    suhuawal = int (input('masukan suhu:'))
    pilihan = str(input('tentukan konfersi anda F,K,R:'))
    konversi(suhuawal,pilihan)

def konversi(suhuawal,pilihan):
    if pilihan.title() == 'F':
        f = (1.8*suhuawal)+ 32
        print('%d celcius itu %d farennheit ' % (f,suhuawal))
    elif pilihan.title() == 'K':
        k = suhuawal + 273
        print('%d celcius itu %d kelvin'% (k,suhuawal))
    elif pilihan.title() == 'R':
        r = 0.8 * suhuawal
        print('%d celcius itu %d reamur' % (r, suhuawal))
    else:
        print('EROR')
    konversi()

def konfirmasi():
    while True :
        ulang = (input('apakah anda ingin mengulang?, (y/t)')) 
        if ulang.title() == 'Y':
            cls()
            mulai()
        elif ulang.title() =='T':
            break   

def cls():
    os.system('cls'  if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    mulai()


    
