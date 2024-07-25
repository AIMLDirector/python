#!/opt/homebrew/bin/python3
from collections import Counter
v1 = "this is python list code "
list = [0,0,6,0,0,4,4,5]
listsort = list.sort()
#print(listsort)
print(list)
print(min(list))
print(max(list))
print(list.count(4))
listcount = Counter(list)
print("print the number of time the number repeats:", listcount[0])
print(listcount)
list1 = [1,"stri", 2.0, 3j]
print(list1[1])
list.append(7)
print(list)
list.insert(3, 9)
print(list)
set_num = set(list)
#print("The type of variables:", type(set_num))
#print([ [i,  list.count(i)] for i in set(list)])
#print(dict((i,  list.count(i)) for i in set(list)))
list.pop()
print(list)
list.remove(0) # - first time the value occurs 
#list.delete(0) # - multiple time the value occurs
for i in list:
    if i == 0:
        newlist = list.remove(0)

