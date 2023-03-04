# working with list 
l = [1,2,3,4,5,6,7,8,9]

# square every value of the list
def squ(a):
    return a*a

new_l = []
for i in l:
    new_l.append(squ(i))

print(new_l)

###--------------map--------------------
squ = lambda a : a*a

l_1 = list(map(squ,l))
print(l_1)

##-------------Filter-------------------
filt = lambda a : 5<a
l_2 = list(filter(filt, l))
print(l_2)

##-------------Reduce-------------------
#reduce the list to a single value 
from functools import reduce
sum = lambda a,b : a+b

l_3 = reduce(sum, l)
print(l_3)



