#----normally we write funtions like that-----
# def double(a):
#     return a*2

# we can do this with lamda function

double = lambda a : a*2
avg = lambda a,b : (a+b)/2

cube = lambda x : x*x*x

print(double(5))
print(avg(10,20))



# to make functions short 
# they coulz be further called into a function

def equ(fx, value):    #fx = cube, value =2
    return 6 + fx(value)

print(equ(cube, 2))