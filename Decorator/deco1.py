def Deco_Fun(func):
    def Inner():
        print("This is before calling the function loop")

        func()
        print("This is after calling the function loop")
    return Inner

@Deco_Fun
def testfunc():
    print("This is a first dummy function")


@Deco_Fun
def testfunc1():
    print("This is second dummy function")

#f1 = Deco_Fun(testfunc)
#f1()
#f2 = Deco_Fun(testfunc1)
#f2()
testfunc()
testfunc1()