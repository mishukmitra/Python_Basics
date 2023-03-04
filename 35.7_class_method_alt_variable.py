# #  class method have access to the class itself via cls 
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def from_string(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    
    
    
string = "Mishuk-2300"

# ob1 = Employee(string.split("-")[0], string.split("-")[1])
# print(ob1.name)
# print(ob1.salary)

ob2 = Employee.from_string(string)
print(ob2.name)
print(ob2.salary)