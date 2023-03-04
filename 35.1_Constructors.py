#---------------class--------------------------------------
#-----class with constructiors----------------------------
class umit:

    def __init__(self, name, pos, id, dept):
        self.name = name
        self.position = pos
        self.id = id
        self.department = dept
        print("Welcome to University of UMIT-Tirol.")
    
    def info(self):
        print(f"Employee name is {self.name}, {self.position} and {self.id}, department of {self.department}")

#-----------------object------------------------------------
#-----dont need to define every time----just put into class just like in function--------

a = umit("Mishuk", "Junior scientist", "20221073", "IEBE")
a.info()

b = umit("Mike", "Associate professor", "20151020", "IEBE")
b.info()