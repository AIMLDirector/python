try:
    x=int(input("Enter the value x:"))
    y=int(input("Enter the value y:"))
    res=x*y
except ValueError as err:
    raise ValueError(" Enter integer values only ") from err