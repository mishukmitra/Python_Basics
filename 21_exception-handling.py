

try:
    a = int(input("Please enter a number for multipilcation table: "))
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")
except:
    print("Number entered is not an integer, Value error")

print("I am always executed")