# amcc-dekstop-yanuar
projek platihan python dan git hub amcc dekstop

cara ngeclone repository
1. buka profile anda, lalu klik your repositories
2. klik new (repository)
3. isi name repository dan kolom di bawahnya sesuai yang diinginkan
4. pilih public
5. jangan lupa centang (Initialize this repository with a README) 
6. klik Add,gitignore :None (pilih python)
7. lalu klik CREATE REPOSITORY
8. lalu copy SSH repository
9. buka git bush lslu paste SSHnya, 
10. stelah dicopy tambahkan (git clone) pada SSHnya
11. lalu enter.

#Bagaimana cara commit dan push
1. stelah melakukan perubahan, cek git anda dengan perintah 'git status'
2. lalu simpan perubahan dengan perintah 'git commit -am "pesan commit" '
3. pastikan dulu sudah tercommit , dengan perintah 'git status'
4. kirimkan perubahan dengan ngepush  dengan perintah 'git push'
5. lalu cek pada repository


##hello word dengan python
masuk ke direktroy folder repository ini dengan cara:
```bash
cd /path/nama direktory
```

catatan : path disini merupakan nama nama direktory diatas direktory repository null seperti misalnya Documen

1.buat sebuah file baru dengan nama file main.py varanya berikut ini
```
nano main.py
`

2.jalankan file tersebut dengan cara
`
python main.py
`

3.jalankan file tersebut dengan  cara
`
python main.py
`

4.hasil outputnya harusnya sesuia denganyang ada di isinya, 
`
hello word
`
	
## python interpreter
    1.python interpreter merupakan program yang dibaca & dieksekusi pada sebuah sesi pada command line. Untuk masuk ke pyhon interpreter, caranya sebagai berikut:
        -Buka CMD (window)/terminal (linux/OS) >> ketikan "python"


    ```python
       Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
       Type "help", "copyright", "credits" or "license" for more information.
    lalu untuk keluar cmd atau terminal ketikan "ctrl + D"

## menggunakan modul
    Modul merupakan set program yang sudah disediakan oleh python yang tingal dipakai 

```python

    >>> import datetime
    >>> datetime.datetime.now()
    datetime.datetime(2019, 12, 1, 20, 47, 4, 998304)
sebagai contoh,kode diatas yang digunakan untuk menampilkan tanggal (datetime) saat ini.
lalu selanjutya kita akan menampilkan karakter alfabet secara random, seperti contoh di bawa

```python
    >>> import random
    >>> import string
    >>> def randomword(length):
...     letters = string.ascii_lowercase
...     return ''.join(random.choice(letters) for i in range (length))
...
>>> randomword(5)
'klgzr'
bisa juga kita menggunakan kode tersebut untuk memilih nama secara random, dengan menginputkan nama nama yang ingin di random dengan list pada kodenya


```python
>>> import random
    >>> import string
    def randomname():
    ...     name = ('david','yanuar','sabil','peby','agung')
    ...     return ''.join(random.choice(name) for i in range(1))
    ...
    >>> randomname()
    'peby'

# menggunakan variabel
variabel adalh tempat menyimpan data pada kode program, lalu bagaimana menggunakan  variabel

```python 
>>> import datetime
>>> print ('waktu sekarang',datetime.datetime now ()
waktu sekarang 12-08-2019 21.13

"""menggabukan variabel string dan integer"""
number = 10
string = 'yanuar'
print(number,string)



# tipe data
dalam python ada berbagai macam type data sperti integer,string,float,
list,dictionary hingga float, list, dictionary hinga tupple.
di dalam file baasic.py sudah ada contoh bagaimana menggunakan berbagai macam file tersebut.

#function (fungsi)
