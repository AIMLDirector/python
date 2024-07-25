# f = open(filename, permission or mode  - r, w, a, r+ ,  w+ , rb, wb)
import os
import shutil

shutil.copyfile("test.txt", "test1.txt")

file1 = open('test.txt', 'r')
print(file1.read())
file1.close()

'''for each in file1:
    print(each)'''



with open("test.txt") as file:
    data = file.read()
print(data)
file.close()

with open("test.txt", 'r') as file:
    data = file.readlines()

    for lines in data:
        wordsplit = lines.split()
        print(wordsplit)
file.close()

with open("tt.txt", 'w') as file:
    file.write("new line appended \n ")
file.close()

with open("test.txt", 'a') as file:
    file.write("new line appended11")
file.close()
# open -- processname (test.txt) -- 2003 -- copied to memory -- 3 lines space memory and store the data in memory   -- read -- it read from memory .
# write  4 line added....  --  it is write in the memory   ( 4 )
# close  --  save the file with line 4 and then it kill the process 2003 -- close the file by release the space in the memory  - permanent store
