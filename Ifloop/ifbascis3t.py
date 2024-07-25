res = "";
for i in range(0,7):
    for j in range(0,7):
        if ( j == 3 or (i ==0 and j> 0 and j < 6)):
           res = res+"*"
           
        else:
            res = res+""
    res = res+"\n"

print(res)

for x in range(1, 8):
    print("*", end="")
    print("")
for x in range (1,7):
    for y in range (1,4):
        print(" ", end="")
    print("*", end="")
    for z in range (1,3):
        print(" ", end="", )
        print("")
        