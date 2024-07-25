from importmod import *  

class Circle:
    def __init__(self, rad):
        self.radius = rad

    def calculat_area(self):
        return round(math.pi * self.radius ** 2, 4)
    

#c1 = Circle(3)
#print(c1.calculat_area())

    
