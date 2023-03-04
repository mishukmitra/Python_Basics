
# dir function to view all funtions from a module
import math
print(dir(math)) 



print("\n")
# import module
import math
result_1 = math.floor(42.25666)
print(result_1)

result_2 = math.sqrt(9)
print(result_2)


#  import specific functions from a module 

from math import sqrt

result_3 = sqrt(9)
print(result_3)

# also import more than one funtions 

from math import sqrt, pi

result_4 = sqrt(9) * pi
print(result_4)


# shortcuts using "as"

import time as t 
wtitn_1 = t.strftime("%H:%M:%S %p")
print(wtitn_1)

from time import strftime as st
wtitn_2 = st("%H:%M:%S %p")
print(wtitn_2)


# self made function
# i made a function name 'mishuk_function'


from mishuk_func import welcome, mishuk
welcome()
print(mishuk)