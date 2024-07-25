for i in range(-1, -11, -1):
    print(i)


for i in range(10):
    if i  == 5:
        pass
#print(i)
    

for i in range(1,10):
    if i > 5:
        break
    print("Multiplication table", i)
    for j in range(1,11):
        print(i* j, end=' ')
    print('')

    

for i in range(1,10):
   
    print("Multiplication table", i)
    for j in range(1,11):
         if j == 5:
            continue
         print(i* j, end=' ')
    print('')


import os
v2 = os.getlogin()
if 'root' in os.getlogin():
    print("user login is root")
else:
    print("not a root user")






