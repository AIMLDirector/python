import random

print(random.random())

print(random.randint(10, 30))

print(random.randrange(10, 40, 3))

print(random.sample([10,20,30,40,50,60,70,80], k=3))

print(random.choice([10,21,23,25,27,34]))

listx=[10,21,23,25,27,34]
random.shuffle(listx)
print(listx)

print(random.triangular(12.5, 40.7,  14.6))

import numpy as np

randarray=  np.random.rand(3,3)
randa2 = np.random.uniform(20.5,78.5, size=(4,2))
randint = np.random.random_integers(20, size=(3,3))
print(randarray)
print(randa2)
print(randint)

#ran

h, os, collection, datetime, sys, json, (systemtool module) --- inbuild module of python so no installation need
# external module -- u need to install that

# break  -- for  & while  loop
# exit()
#sys.exit()v
# error handling --
#sys.syserr()
# TypeError: