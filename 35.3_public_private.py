class student:
    def __init__(self):
        self.name = "Mishuk"   # public 
        self.__age = "30"     # private (__name mangling)
    

obj = student()
print(obj.name)
# print(obj.__age) # cannot be accessed diretly

# private can be accessed indirectly
print(obj._student__age)
