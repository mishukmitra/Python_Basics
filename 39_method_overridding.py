class rec():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def area(self):
        return (self.x * self.y)
    

class circle(rec):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius) #  takes  return line operation
        
    def area(self):
        return 3.14 * super().area()
        
    

r = rec(5,3)
print(r.area())

c = circle(2)
print(c.area())