x =''
if x == 0:
    print("The error in the code")

def zeroerr(i):
    return 1/i



try:
    i = zeroerr(2)
    print(i)
except ZeroDivisionError as err :
    #print("some error happen on executing the code:  %s" % err)
    raise ZeroDivisionError("Some Error happen while parsing the input value") from err
except ValueError as err :
    raise ValueError("Some Error happen while parsing the input value") from err
else:
    print("No error happen during execution ")
finally:
    print("Execution is successful ")

class XyzError(Exception): pass

n = -3

if n < 0:
    raise XyzError("Input valuse is less than 0  provide positive number")



