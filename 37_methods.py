class info:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    

ob1 = info("John", 20, 10000)

print("\n")
print(dir(ob1)) # print all attributes

print("\n")
print(ob1.__dict__) # dictionary attribute

print("\n")
print(help(ob1)) # print help


    