# == , compare values 
# == , compares identity/ location

a = 2 
b = 3

print(a == b) # compare value
print(a is b) # compare location

print("\n")

# only for the list it changes location even same value assign
c = [1,2,3,4,5]
d = [1,2,3,4,5]

print(c == d)
print(c is d)

print("\n")
#.-----------
c = (1,2,3,4,5)
d = (1,2,3,4,5)

print(c == d)
print(c is d)

#------
f = None

print(f is None)
