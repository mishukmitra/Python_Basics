marks = [70,46,56, "Mish", True]

print(marks)
print(type(marks))
print(marks[0])
print(marks[4])

if 46 in marks:
    print("yes")
else:
    print("no")

if "Mish" in marks:
    print(True)

print(marks[0:3])

# example 2
# Lists are mutable 

l = [32,44,2,3,34,64,80,10]

l.append(80)
print(l)
l.reverse()
print(l)
l.sort()
print(l)

print(l.count(80))

m = l.copy()

m[0] = 0
print(m)

m.insert(3,999)
print(m)

n = [40,50,60]
m.extend(n)
print(m)

new = m+n
print(new)
