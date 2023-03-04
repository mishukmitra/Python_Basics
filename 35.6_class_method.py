# Class methods don't need a class instance. They can't access the instance ( self ) 
# but they have access to the class itself via cls 
# class method changes the class variable forever

class employee:
    
    country = "Austria"    # class variable
        
    
    def details(self):
        print(f"Employess name is {self.name} and country is {self.country}")
    
    @classmethod  
    def change_country(cls, newcountry):
        cls.country = newcountry

        


ob1 = employee()
ob1.name = "Mishuk"


ob1.change_country("Germany") 
ob1.details()
print(ob1.country)
