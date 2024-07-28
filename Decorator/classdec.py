class CountCallNumber:

  def __init__(self, func):
    self.func = func
    self.call_number = 0

  def __call__(self, *args, **kwargs):
    self.call_number += 1
    print("This is execution number " + str(self.call_number))
    return self.func(*args, **kwargs)

@CountCallNumber
def say_hi(name):
  print("Hi! My name is " + name)

say_hi("Jack")

say_hi("James")
say_hi("sam")


@CountCallNumber
def Hellofunc(name):
  print("Hi! My name is " + name)

Hellofunc("kumar")