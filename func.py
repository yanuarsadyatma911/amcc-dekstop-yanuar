def square(x):
    """calculate Square Value"""
    return x*x
square(5)

#niali_murid = ['yannuar': 9.5]

#password controller

def foo(x):
    if len(x) >= 8:
        return True
    else:
        return False


def foo(x):
    if x > 7:
        return 'Warm'
    else:
        return 'Cold'


#Summary: Functions and Conditionals In this section you learned to:

#Define a function:

def cube_volume(a):
    return a * a * a
#Write a conditional block:

message = "hello there"
 
if "hello" in message:
    print("hi")
else:
    print("I don't understand")
#Write a conditional block of multiple conditions

message = "hello there"
 
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")
#Use the and operator to check if both conditions are True at the same time:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
#Output is Yes since both x and y are 1.

#Use the or operator to check if at least one condition is True:

x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
#Output is Yes since x is 1.

#Check if a value is of a certain type with:

isinstance("abc", str)
isinstance([1, 2, 3], list) 

or

type("abc") == str
type([1, 2, 3]) == lst