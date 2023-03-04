# time module 
# check which loop  faster

#-------while loop-------#
def using_while_loop():
    i = 0
    while i < 4000:
        print(i)
        i = i +1

# -------for loop-------#
def using_for_loop():
    for i in range(4000):
        print(i)
        

#----------------------------------------------------------------
import time

#-------
init = time.time()
using_while_loop()
t1 = time.time() - init
#--------


#-------
int = time.time()
using_for_loop()
t2 = time.time() - int
#--------

print(t1)
print(t2)