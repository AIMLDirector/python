s = 1
while(s <=10):
    print(f"Square root of {s}:", s**2)
    s +=1

#output = 10,20,30,40 .. 100
       
i = 0
list1 = []
while(i <=100):
   i+=10
   list1.append(i)

print(list1) 

       
j = 0

while(j <=100):
   j+=10
   print(j, end=",")
print("")


np = 0
user_number = int(input("Enter your number:"))

if user_number == 0 or user_number == 1:
   print(" 0 & 1 are not prime number")
else:
   n = 2
   while(n < user_number):
      if(user_number % n) == 0:
         np = np + 1
      n = n+ 1
if np == 0:
    print ( user_number, " This is prime number")
else:
   print ( user_number, " This is not  prime number")

''' n = 9494
   rnum = 0
   r = n%10      r = 4
   rnum = rnum*10 '''


usr_list = []
user_input = input("Enter your number (type 'done' to finish the loop)")

while user_input.lower() != 'done':
    usr_list.append(int(user_input))
    user_input = input("Enter your next number (type 'done' to finish the loop)")

print("user list", usr_list)

'''while False:
      --- infinite loop 
   security team tester
   hacker '''


