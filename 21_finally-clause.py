list = [5,8,12,3]

def func1():
    try:
        i = int(input("Enter the index no: "))
        print(list[i])
        return 1
    except ValueError:
        print("value error")
        return 0
    except IndexError:
        print("list index out of range")
        return 0

    finally:
        print("I am always executed")


# finally is useful here when we use a function
# even after "return" it will continue to "finally"

n = func1()
print(n)