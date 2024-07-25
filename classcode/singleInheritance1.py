class paul():
    def student1(self):
        print('I am a student with roll Number: 101')


class Daniel(paul):   # constructor -- java/c++/python 
    def student2(self):   # method
        print('I am a student with roll Number: 102')

s=Daniel()   # object assignment to variable 

#s.student1()
#s.student2()

class paul1():
    def student1(self):
        print('I am a student with roll Number: 101')


class Daniel1(paul1):
    def student1(self):
        print('I am a student with roll Number: 102')




s1=Daniel1()
s1.student1()
print(Daniel.mro())


def student3():   # method
        print('I am a student with roll Number: 102')

student3()