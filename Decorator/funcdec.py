def your_decorator(func):
  def wrapper():
    # Do stuff before func...
    print("Before func!")
    func()
    # Do stuff after func...
    print("After func!")
  return wrapper

@your_decorator
def foo():
  print("Hello World!")

foo()


def your_decorator(func):
  def wrapper(*args,**kwargs):
    # Do stuff before func...
    print("Before func!") 
    func(*args,**kwargs)
    # Do stuff after func...
    print("After func!")
  return wrapper

@your_decorator
def foo(bar):
  print("My name is " + bar)

foo("Jack")