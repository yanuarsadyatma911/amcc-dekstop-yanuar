
"""LIST"""

print (list(range(1,20,3)))

temperature = [12.5 , 10, 'yanuar']
print (temperature)

#""" calculating list"""
students_grades = [2.5,5.4,7.5,8.5,9.5]
mysum = sum(students_grades)
print (mysum)
length = len(students_grades)
print (length)
mean = mysum / length
print(mean)

#"""cara mencari nilai dalam list"""
students_grades = [10.0,10.5,11.5,10.0,12.0]
print(students_grades.count(10.0))

students = {'sabil': 7.9,'yanuar':8.0,'agung':8.5}
print(students.values())
print(students.keys())

#"""cara membuat tampilan huruf menjadi huruf kecil"""
username = 'Python'
print(username.lower())

#"""Panjang nilai dalam List"""
length = len(students_grades)
print (length)
mean = mysum / length
print(mean)

list1 = ['kimia', 'fisika', 1993, 2017]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
