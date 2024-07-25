# equal  "word" == "word"  or 1 == 2
# Not Equal  "word" != "word" or 1 != 2
 # a < b ,  a <= b, a > b, a >= b

a = 5
b = 6
c = 7 

if a > b:
    print( "a is greater than b")
else:
    print("b is greater than a")


if a > b:
    print( "a is greater than b")
elif a > c:
    print("a is greater than c")
elif b > c:
    print (" b is greater than c")
else:
    print ( "b is the smallest number")

if (a > b) and ( a > c):
    print ( "a is the greatest number")
elif( b > c) and ( b > a):
    print ( "b is the greatest number")
else:
    print ( "c is the smallest number ")


# number from 1 to 40 
# if it is divisible by 2 collect that in one list
# if it is divisble by 3 collect that in second list 
# print first list
# print second list
    
list = [1, 3, 4.0, 35, 'str', "sample", 5,"in", 9.45,  0.4]

list1 = [1,3,35,5]
list2 = [4.0, 9.45, 0,4 ]
list3 = ['str', "sample", "in"]


