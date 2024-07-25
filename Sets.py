s1 = {2,4,6,8}
print(type(s1))
s1.add(9)
print(s1)
s1.remove(6)
print(s1)
s1.pop()
print(s1)
s1.clear()
print(s1)
s1.add(5)
print(s1)
s2 = {'a','b','c'}
s3 = {'test', 'sample',5,'a','b' }
s4 = s1.union(s2,s3)
print(s4)
s5 = s1|s2|s3
print(s5)
