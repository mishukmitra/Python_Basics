class Employee:
    name = "Mishuk"
    job = "umit"

    def __len__(self):
        return len(self.name)



ob = Employee()
print(ob.name)

print(len(ob))