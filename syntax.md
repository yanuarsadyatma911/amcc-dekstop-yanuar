Perkenalan Basic Syntax PYTHON

Python adalah bahasa pemrograman multifungsi yang dibuat oleh Guido van Rossum dan dirilis pada tahun 1991. GvR, begitu ia biasa disebut di komunitas Python, menciptakan Python untuk menjadi interpreter yang memiliki kemampuan exception handling dan mengutamakan keterbacaan. Didesain untuk memudahkan dalam prototyping, Python menjadi bahasa yang sangat mudah dipahami dan fleksibel.
Saat ini, Python dikelola oleh Python Software Foundation (PSF). Namun sebelumnya, GvR dijuluki sebagai Benevolent dictator for life (BDFL) karena hampir semua keputusan pengembangan Python diambil oleh GvR, berbeda dengan bahasa lain yang misalnya menggunakan voting dan semacamnya. Pasca tahun 2000, dibentuklah beberapa sistem yang memungkinkan Python menjadi lebih sustain, misalnya Python Enhancement Proposals (PEP) untuk pengembangan Python dan tentunya Python Software Foundation (PSF). jika PSF menjadi lembaga yang mengelola dan mengadvokasi Python, PEP menjadi panduan dalam pengembangan Python. Beberapa PEP memuat misalnya bagaimana sintaksis dan bagaimana Bahasa Python akan berevolusi, bagaimana modul akan di-deprecate, dan sebagainya. Setelah kurang lebih 30 tahun dalam pengembangan Python, GvR memutuskan untuk tidak lagi menjabat BDFL pada 12 Juli 2018.
 
Mengapa Python?
Efektifitas Python cukup terbukti dengan banyaknya jumlah pengguna Bahasa ini. Berbagai survei memasukkan Python dalam top-3 sebagai bahasa dengan penggunaan terbanyak, bersaing dengan Java dan PHP. Python dapat digunakan dalam mengakomodasi berbagai gaya pemrograman, termasuk structured, prosedural, berorientasi-objek, maupun fungsional. Python juga dapat berjalan pada berbagai sistem operasi yang tersedia. Beberapa pemanfaatan bahasa Python di antaranya:
1.	Web development (server-side),
2.	Software development,
3.	Mathematics & data science,
4.	Machine learning,
5.	System scripting.
Style Guide pada Python Code
Indentasi
Gunakan 4 spasi pada setiap tingkatan indentasi.
Python menggunakan indentasi untuk menulis kode bertingkat. Bahasa lain mungkin menggunakan statement tertentu (Begin, end - pascal), perbedaan baris atau kurung kurawal. Statement yang memiliki indentasi yang sama dan diletakkan secara berurutan dikenali sebagai blok statement oleh Python dan akan dijalankan secara berurutan.
Panjang Baris Maksimum
Batasi panjang kode setiap baris hingga 79 karakter. Untuk komentar atau dokumentasi, usahakan untuk tidak melebihi 72 karakter.

Contoh:
 
Disarankan:
 





Reserved Words
Daftar berikut menunjukkan kata kunci Python. Ini adalah kata-kata yang dicadangkan dan Anda tidak dapat menggunakannya sebagai konstan atau variabel atau nama pengenal lainnya. Semua kata kunci Python hanya berisi huruf kecil.
 
and		exec		not
assert		finally		or
break		for		pass
class		from		print
continue	global		raise
def		if		return
del		import		try
elif		in		while
else		is		with
except		lambda		yield
 
5 Aturan Penulisan Sintaks Python yang Harus dipatuhi
1. Penulisan Statement Python
Statement adalah sebuah intruksi atau kalimat perintah yang akan dieksekusi oleh komputer.

	Contoh:
	 print("Hello World!")
	 print("Belajar Python dari Nol")
	 nama = “yanuar”
2. Penulisan String pada Python
String adalah teks atau kumpulan dari karakter. String dalam pemrograman biasanya ditulis dengan dibungkus menggunakan tanda petik. Bisa menggunakan tanda petik tunggal maupun ganda.
	Contoh:
	 judul = "Belajar Pemrograman Python sampai Bisa"
	 penulis = ‘yanuar yayan'
Atau kita juga bisa menggunakan triple tanda petik.
	Contoh:
	 judul = """Belajar Python dengan Cepat"""
	 penulis = '''Dekstop Programing'''
3. Penuilsan Case pada Python
Sintak Python bersifat case sensitive, artinya teksini dengna TeksIni dibedakan.
	Contoh:
	 judul = "Belajar Dasa-dasar Python"
	 Judul = "Belajar Membuat Program Python
Antara variabel judul dengan Judul itu dibedakan…
Case Style
Menurut rekomendasi style guide Google, berikut ini contoh penulisan case yang disarankan:


## Snake Case digunakan pada:
module_name, package_name, method_name, function_name, , global_var_name, instance_var_name, function_parameter_name, local_var_name.

## CamelCase digunakan Pada:
ClassName, ExceptionName

## ALL CAPS digunakan Pada:
GLOBAL_CONSTANT_NAME
Atau bias juga di lihat di https://www.petanikode.com/case-kode-program/
4. Penulisan Blok Program Python
Blok program adalah kumpulan dari beberpaa statement yang digabungkan dalam satu blok.Penulisan blok program harus ditambahkan indentasi (tab atau spasi 2x/4x).
# blok percabangan if
if username == 'Dekstoop Programing':
    print("Selamat Datang Member")
    print("Silahkan ambil tempat duduk")

# blok percabangan for
for i in range(10):
    print i

5. Cara Penulisan Komentar pada Python
Komentar merupakan baris kode yang tidak akan dieksekusi. Komentar digunakan untuk memberikan informasi tambahan dan untuk menonaktifkan kode. Ada beberapa cara menulis komentar pada pemrograman Python :

Menggunakan Tanda Pagar (#)
Cara pertama menggunakan tanda pagar (#)
Cara ini paling sering digunakan.
	Contohnya:
	 # ini adalah komentar
	 # Ini juga komentar

Menggunakan Tanda Petik
Selain untuk mengapit teks (string), tanda petik juga dapat digunakan untuk membuat komentar.
	Contoh:
	 "Ini adalah komentar dengan tanda petik ganda"
	 'Ini juga komentar, tapi dengan tanda petik tunggal'

Contoh penulisan coding python.

 


 
 








Operators and Expressions
Apa itu operator?
Operator merupakan simbol-simbol yang digunakan untuk melakukan operasi tertentu.
Ada enam jenis operator dalam pemrograman yang wajib diketahui:

1.	Operator Aritmatika
2.	Operator Pembanding/Relasi
3.	Operator Penugasan
4.	Opeartor Logika
5.	Operator Bitwise
6.	Operator Ternary

1. Operator Aritmatika
Opeartor aritmatika termasuk dalam operator yang paling sering digunakan dalam pemrograman.
Opeartor aritmatika terdiri dari:
Operator		Simbol
Penjumlahan		+
Pengurangan		-
Perkalian		*
Pembagian		/
Sisa Bagi		%
Pemangkatan		**

	Contoh programnya:
# file: operator_aritmatika.py

# Ambil input untuk mengisi nilai
a = input("masukan nilai a: ")
b = input("masukan nilai b: ")

# Menggunakan operator penjumlahan
c = a + b
print "Hasil %d + %d = %d" % (a,b,c)

# Operator Pengurangan
c = a - b
print "Hasil %d - %d = %d" % (a,b,c)

# Operator Perkalian
c = a * b
print "Hasil %d * %d = %d" % (a,b,c)

# Operator Pembagian
c = a / b
print "Hasil %d / %d = %d" % (a,b,c)

# Operator Sisa Bagi
c = a % b
print "Hasil %d %% %d = %d" % (a,b,c)

# Operator Pangkat
c = a ** b
print "Hasil %d ** %d = %d" % (a,b,c)

2. Operator Penugasan
Seperti namanya, operator ini digunakan untuk memberikan tugas pada variabel.
Misalnya:
umur = 18
Maka variabel umur telah kita berikan tugas untuk menyimpan angka 18.
Selain menyimpan atau pengisian nilai, ada juga menjumlahkan, mengurangi, perkalian, pembagian, dsb.
Selengkapnya bisa dilihat di tabel berikut.

Operator		Simbol
Pengisian		=
Penjumlahan		+=
Pengurangan		-=
Perkalian		*=
Pembagian		/=
Sisa Bagi		%=
Pemangkatan		**=

Contoh programnya.
# file: operator_penugasan.py

# Ambil input untuk mengisi nilai
a = input("masukan nilai a: ")
# ^ 
# | contoh operator penugasan untuk mengisi nilai

print "Nilai a = %d" % a

# Coba kita jumlahkan nilai a dengan opertor penugasan
a += 5
# ^
# |
# contoh operator penugasan untuk menjumlahkan

# Setelah nilai a ditambah 5, coba kita lihat isinya
print "Nilai setelah ditambah 5:"
print "a = %d" % a

3. Operator Pembanding
Operator ini digunakan untuk membandingkan dua buah nilai. Operator ini juga dikenal dengan operator relasi dan sering digunakan untuk membuat sebuah logika atau kondisi.
Opertor ini terdiri dari:

Operator			Simbol
Lebih Besar			>
Lebih Kecil			<
Sama Dengan			==
Tidak Sama dengan		!=
Lebih Besar Sama dengan		>=
Lebih Kecil Sama dengan		<=

Contohnya :
a = 4
b = 2
c = a < b
Apakah isi dari variabel c?
Isinya adalah False, karena nilai 4 lebih kecil dari 2 (4 < 2) adalah salah (False).

# file: operator_pembanding.py
a = input("masukan nilai a: ")
b = input("masukan nilai b: ")

# apakah a sama dengan b?
c = a == b
print "Apakah %d == %d: %r" % (a,b,c)

# apakah a < b?
c = a < b
print "Apakah %d < %d: %r" % (a,b,c)

# apakah a > b?
c = a > b
print "Apakah %d > %d: %r" % (a,b,c)

# apakah a <= b?
c = a <= b
print "Apakah %d <= %d: %r" % (a,b,c)

# apakah a >= b?
c = a >= b
print "Apakah %d >= %d: %r" % (a,b,c)

# apakah a != b?
c = a != b
print "Apakah %d != %d: %r" % (a,b,c)

4. Operator Logika
Operator logika digunakan untuk membuat operasi logika, seperti logika AND, OR, dan NOT.
Operator logika terdiri dari:

Nama			Simbol di Python
Logika AND			and
Logika OR			or
Negasi/kebalikan		not

Contoh:
a = True
b = False

# Logika AND
c = a and b
print "%r and %r = %r" % (a,b,c)

# Logika OR
c = a or b
print "%r or %r = %r" % (a,b,c)

# Logika Not
c = not a
print "not %r  = %r" % (a,c)

5. Operator Bitwise
Operator Bitwise adalah operator untuk melakukan operasi berdasarkan bit/biner.
Operator ini terdiri dari:

Nama			Simbol
AND			&
OR			|
XOR			^
Negasi/kebalikan	~
Left Shift		<<
Right Shift		>>

Hasil operasi dari operator ini agak sulit dipahami, kalau kita belum paham operasi bilangan biner.
Mari kita coba pahami dengan contoh sederhana:
Misalnya, kita punya variabel a = 60 dan b = 13.
Bila dibuat dalam bentuk biner, akan menjadi seperti ini:
a = 00111100
b = 00001101
Kemudian, dilakukan operasi bitwise
Operasi AND
a = 00111100
b = 00001101
a & b = 00001100
Operasi OR
a = 00111100
b = 00001101
a | b = 00111101
Operasi XOR
a = 00111100
b = 00001101
a ^ b = 00110001
Opearsi NOT (Negasi/kebalikan)
a = 00111100
~a  = 11000011

Konsepnya memang hampir sama dengan opeartor Logika. Namun, Bitwise digunakan untuk biner.




Contoh programnya: 
a = input("Masukan nilai a: ")
b = input("Masukan nilai b: ")

# Operasi AND
c = a & b
print "a & b = %s" % c

# Operasi OR
c = a | b
print "a | b = %s" % c

# Operasi XOR
c = a ^ b
print "a ^ b = %s" % c

# Operasi Not
c = ~a
print "~a = %s" % c

# Operasi shift left (tukar posisi biner)
c = a << b
print "a << b = %s" % c

# Operasi shift right (tukar posisi biner)
c = a >> b 
print "a >> b = %s" % c

6. Operator Ternary

Operator ternary juga dikenal dengan operator kondisi, karena digunakan untuk membuat sebuah ekspresi kondisi seperti percabgan IF/ELSE.
Operator ternary sebenarnya tidak ada dalam Python, tapi python punya cara lain untuk menggantikan operator ini.
Pada bahasa pemrograman lain operator ternary menggunakan tanda tanya (?) dan titik dua (:).
kondisi ? <nilai true> : <nilai false>

Contoh:

aku = (umur < 10) ? "bocah" : "dewasa"
Dalam Python bentuknya berbeda, yaitu menggunakann IF/ELSE dalam satu baris.
<Nilai True> if Kondisi else <Nilai False>

Contoh:

umur = input("berapa umur kamu? ")
aku = "bocah" if umur < 10 else "dewasa"
print aku

				Control Flow


1.IF

Seringkali, Anda perlu menjalankan beberapa pernyataan hanya jika suatu kondisi berlaku, atau memilih pernyataan untuk dieksekusi tergantung pada beberapa kondisi yang saling eksklusif. Python pernyataan majemuk if, yang menggunakan if, elif dan else klausa, memungkinkan Anda kondisional mengeksekusi blok pernyataan. if digunakan untuk menjalankan perintah jika dan hanya jika kondisi pada if bernilai benar. mari kita lihat seperti apa if :


if (1 > 2):
  print("1 lebih besar dari 2")

if (2 > 1):
  print("2 lebih besar dari 1")

kode diatas akan menghasilkan output “ 2 lebih besar dari 1”, karena kondisi yang bernilai benar adalah if yang kedua

2.ELSE

else digunakan untuk menjalankan perintah jika kondisi pada if bernilai salah, mari kita lihat seperti apa else :

if (2 < 1):
  print("2 lebih kecil dari 1")
else:
  print("2 lebih besar dari 1")
kode diatas akan menghasilkan output “2 lebih besar dari 1”, karena kondisi pada if bernilai salah, maka yang dijalankan adalah perintah pada else



3.IF-ELIF-ELSE

Pengambilan keputusan (kondisi if elif) merupakan lanjutan/percabangan logika dari “kondisi if”. Dengan elif kita bisa membuat kode program yang akan menyeleksi beberapa kemungkinan yang bisa terjadi. Hampir sama dengan kondisi “else”, bedanya kondisi “elif” bisa banyak dan tidak hanya satu. mari kita lihat bagaimana elif :

if (2 < 1):
  print("2 lebih kecil dari 1")
elif (2 > 1):
  print("2 lebih besar dari 1")
else:
  print("2 sama besar dengan 1")

contoh penggunaan if,else,dan elif :

hari_ini = "Minggu"

if(hari_ini == "Senin"):
    print("Saya akan kuliah")
elif(hari_ini == "Selasa"):
    print("Saya akan kuliah")
elif(hari_ini == "Rabu"):
    print("Saya akan kuliah")
elif(hari_ini == "Kamis"):
    print("Saya akan kuliah")
elif(hari_ini == "Jumat"):
    print("Saya akan kuliah")
elif(hari_ini == "Sabtu"):
    print("Saya akan kuliah")
elif(hari_ini == "Minggu"):
    print("Saya akan libur")




4. While

 Pernyataan while memungkinkan Anda untuk berulang kali menjalankan blok pernyataan selama kondisi benar. Sebuah while pernyataan adalah contoh dari apa yang disebut perulangan pernyataan. Sebuah whilepernyataan dapat memiliki opsional elseklausul.

Contoh (simpan sebagai while.py):

count = 0

while count < 5:
    print ('saya sedang belaljar python')

    count = count+1

angka = 23
running = True

while running:
    guess = int(input('masukan angka : '))

    if guess == angka:
        print('jawaban kamu benar')
        
        running = False
    elif guess < angka:
        print('tidak, jawaban kamu lebih dari itu')
    else:
        print('tidak, jawaban kamu kurang dari itu')
else:
    print('selamat anda benar')
    

print('SLESAI')



5.FOR

Perulangan for disebut counted loop (perulangan yang terhitung), perulangan for biasanya digunakan untuk mengulangi kode yang sudah diketahui banyak perulangannya.

for indek in range(banyak_perulangan):
    # jalankan kode ini
    # jalankan juga kode ini
    # kode ini tidak akan diulang karena berada di luar for

Contoh Program :
orang = ['saya','kamu','kita']

for nama in orang:
    print('nama namnya adalah', nama)



				ThankYOU

