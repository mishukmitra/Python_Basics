#--------static method: dont need "self" in class----------
class math:
    def __init__(self, a, b):
        self.num = a
        self.num2 = b
    
    def mul(self):
        print(self.num *self.num2)

    @staticmethod  
    def add(x,y):
        print(x+y)


ob = math(5,5)

ob.mul()


#---------advantages of static metod---------
ob.add(2,7)
math.add(2,7)
