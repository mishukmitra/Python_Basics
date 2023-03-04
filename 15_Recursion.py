# Recursion is nothing just a function into a function
# that means we can call a function into this function


# Example 1: Factorial 
# 8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1
# n! = n * (n-1)!

# 1! = 1
# 0! = 1


def factorial(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(4))


# Fibonacci series 
# f0 f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 f11 f12
# 0  1  1  2  3  5  8  13 21 34 55  89  144
# f0 = 0
# f1 = 1
# f2 = f1 + f0
# fn = f(n-1) + f(n-2) 

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(8))




