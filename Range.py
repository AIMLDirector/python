for i in range(10):
    print(i, end=' ')

print("\n")
# for i in range(start, end, step)  -- ( 1, 10, 2)
    
for j in range(1,10,2):
    print(j, end=' ')

print("\n")

#python 2.6 or 2.7   range or Xrange 
# python 3.x  -- range

list = ['sam', 'paul', 'george']

for i in range(len(list)):
    print(list[i], end=' ')

print("\n")

import os
v1 = os.getcwd()
v2 = os.getlogin()
v3 = os.geteuid()
#print(v1, v2, v3)


for i in reversed(range(10,20)):
    print(i, end=' ')

print("\n")

#for x in range(20, 10 -2):
#  print(x)

for y in range(5, -1 -1):
    print(y)

