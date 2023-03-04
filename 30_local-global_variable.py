x = 5 
y = 100


def hello():
    x = 8
    global y
    y = 300
    print(f"The local variable x is: {x}")




hello() # x=8
print(f"The global variable x is: {x}") # x = 5



print("\n")
print(f"The global variable y is: {y}") # 300