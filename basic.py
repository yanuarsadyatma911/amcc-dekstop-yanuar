"""DATE TIME"""
import datetime
mynow = datetime.datetime.now()
print ('tanggal hari ini', mynow)

"""menggabukan variabel string dan integer"""
number = 10
string = 'yanuar'
print(number,string)

""" simpe type """

x = 10
y = 10
z = 15.1

hasil1 = x+x
hasil2 = y+y
hasil3 = z+z

print (hasil1,hasil2,hasil3)
print (type(x),type(y),type(z))

#"""LIST"""

print (list(range(1,20,3)))

temperature = [12.5 , 10, 'yanuar']
print (temperature)

""" calculating list"""
students_grades = [2.5,5.4,7.5,8.5,9.5]
mysum = sum(students_grades)
print (mysum)
length = len(students_grades)
print (length)
mean = mysum / length
print(mean)

"""cara mencari nilai dalam list"""
students_grades = [10.0,10.5,11.5,10.0,12.0]
print(students_grades.count(10.0))

students = {'sabil': 7.9,'yanuar':8.0,'agung':8.5}
print(students.values())
print(students.keys())

"""cara membuat tampilan huruf menjadi huruf kecil"""
username = 'Python'
print(username.lower())

"""Panjang nilai dalam List"""
length = len(students_grades)
print (length)
mean = mysum / length
print(mean)

"""Tuple"""


"""more with list"""
nilai_murid = [9.5,9.6,7.8,9.4,7.8,9.0]
nilai_murid.append(7.7) #menambahkan nilai dalam list
print (nilai_murid)

nilai_murid.index(9.5) #mencari index pada list
nilai_murid.clear() #menghaapus isi pada list
print(nilai_murid)

