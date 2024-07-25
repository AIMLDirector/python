class cubes:
    def __init__(self,max):
            self.max = max

    def __iter__(self):
          self.num = 0
          return self
    
    def __next__(self):
          if (self.num >= self.max):
                raise StopIteration
          return  3**self.num
          self.num+= 1
          return result


cub = cubes(4)
cub_iter = iter(cub)
print(list (cub_iter))

