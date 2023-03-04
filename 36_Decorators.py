# This is a decorator function who will decorate other funtion
def greet(d):
    def md(*args, **kwargs):
        print("Good Morning!")
        d(*args, **kwargs)
        print("Thank you for using decorator.")
    return md




#----------------------------------------------------------

@greet
def add(a,b):
    return a+b

add(1,2)
