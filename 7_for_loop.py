
# example 1
name_1 = "Mishuk"
for i in name_1:
    print(i)
    

print("\n")
# Example 2:
name_2 = "Mishuk"
for i in name_2:

    if i == "M":
        print(i, ": This is the first letter of my name")

    elif i == "k":

        print(i, ": This is the last letter of my name")

    else:
        print(i)


print("\n")

# Example 3:
flowers = ["Rose", "Gadha", "Jui","Jasmine"]

for flower in flowers:
    print(flower)
    for charaacter in flower:
        print(charaacter)

print("\n")

# Example 4: range function
for i in range(5): # 0:5
    print(i)

print("\n")
for i in range(1,5):
    print(i)

print("\n")
for i in range(1,10,2):
    print(i)

