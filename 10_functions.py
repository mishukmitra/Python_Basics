# Exmaple 1: 

def average(a,b):
    return (a+b)/2

a = 6
b = 7
print(average(a,b))
print(average(12,9))

# Exmaple 2:
def isgreater(a,b):
    if a < b:
        print("a is less than b")
    else:
        print("a is greater than b")

isgreater(a,b) 

# Exmaple 3:
def your_name(fname, mname, lname = "kumar"):

    print(f"Hello {fname} {mname} {lname}")

your_name("Mishuk", "Mitra")
your_name("Bose", "Manashi")



def avg(a,b,c=4):
    return (a+b+c)/3
print(avg(1,4))

# Exmaple 4:
def avg2(*numbers):
    print(type(numbers))
    return sum(numbers)/len(numbers)
    

print(avg2(10,2,3,4,5))


# Exmaple 5:
def avg3(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
    
print(avg3(10,2,3,4,5))

# Exmaple 6:
def flowers(**flower):
    print(type(flower))
    print(flower["fname"], flower["sname"], flower["tname"])


flowers(sname="rose", tname="gadha", fname="rajanigandha")


