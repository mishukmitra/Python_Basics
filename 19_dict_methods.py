d_empty = {} # empty dict
print(d_empty)

d = {"name" :" Mishuk",
    "address" : "Innsbruck",
    "zip" : 6020,
    "eligible" : True} 

d1 = {"employer" : "umit",
    "ID" : 20221073}

d.update(d1)
print(d)

#---------------------pop----------
d.pop("eligible") # pop out value you want
print(d)

d.popitem() # pop out the last value
print(d)

del d["address"]
print(d)

d1.clear()
print(d1)

