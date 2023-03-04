# generator doesnt store, it generate when call
# check loop one by one

def my_generator():
    for i in range(100):
        # complex operation
        yield i
        
        

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))