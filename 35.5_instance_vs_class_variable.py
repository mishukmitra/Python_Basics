# at first search for instance variable
# if no instance variable then take class variable

class employee:
    
    country = "Austria"    # class variable

    def __init__(self, name):
        self.name = name
        self.company = "Google" # class variable
        self.basic = 2000
        
    
    def details(self):
        print(f"Employess in {self.country}")
        print(f"Employee name is {self.name} and works in {self.company} and salary is {self.basic}" ) 



ob1 = employee("Mishuk")
ob1.details()

ob2 = employee("Manashi")
ob2.company = "BRB" # instance variable
ob2.country = "BD"  # instance variable
ob2.details()