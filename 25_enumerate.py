fruits = ["apple", "orange", "mango", "jack", "banana", "kiwi", "guava"]

# we can print fruits as well as their index togather called enumerate


# ----------- normally we do --------------

index = 0

for f in fruits:
    print(f)
    if index == 3:
        print(f, ": please add 'fruit' on the end of amy name" )
    index += 1


print("\n")
# ----------using enumerate------------

for index, f in enumerate(fruits):
    print(f)
    if index ==3:
        print(f, ": please add 'fruit' on the end of amy name" )