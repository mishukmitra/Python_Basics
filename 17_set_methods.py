n1 = {7,9,20,10,15,10}
n2 = {3,4,6,7,9}

## -----------Intersection--------------
print(n1.intersection(n2))
#n1.intersection_update(n2) # intersenction but updated the new value to n1
print(n1)

# n1.update(n2) # it includes all value from n2 and update n1
print(n1)


## ------------Union---------------
print(n1.union(n2)) # take evrything and common values once

###----------------difference------------------

n3 = n1.symmetric_difference(n2) # takes uncommom items from both
print(n3)

n4 = n1.difference(n2) # takes uncommon item from n1 
print(n4)


# to check n1 and ne have totally different values, if false then must have some common values
print(n1.isdisjoint(n2)) 

##--------- superset and sbset-----------
# to check all values of n2 contain in n1
print(n2.issubset(n1))

n6 = {7,9,20,10,15,10}
n7 = {7,9}
print(n7.issubset(n6))

#
print(n1.issuperset(n2))
print(n6.issuperset(n7))

##------------add and remove new items----------------------
n7.add(100)
print(n7)

n7.remove(100)
print(n7)

n7.discard(7)
print(n7)

pop_item = n6.pop() # pop random values from n6
print(n6)
print(pop_item)

## -----------clear abd delete--------------
# it i want to clear all items from n6
print(n6.clear())

# if i want to delete n7
del n7
