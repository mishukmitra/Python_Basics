#---------------class: parent--------------------------------------
class umit:

    def __init__(self, name, pos, id, dept):
        self.name = name
        self.position = pos
        self.id = id
        self.department = dept
        print("Welcome to University of UMIT-Tirol.")
    
    def info(self):
        print(f"Employee name is {self.name}, {self.position} and {self.id}, department of {self.department}")

#--------------------class: child---------------------------------------
class dept(umit):
    def details(self):
        print("I a IT department")



#-----------------object------------------------------------
#note: tcc is a son of umit
# child will get everything from parent 
# but parent will get nothing from child

a = umit("Mishuk", "Junior scientist", "20221073", "IEBE")
a.info()

c = dept("Bose", " Prof", "44", "IEBE")
c.details()

c.info() # child know about his father