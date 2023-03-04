##-------------------- {:} --------------
##-------------------- {key : value} --------------
d = {"name" :" Mishuk",
    "address" : "Innsbruck",
    "zip" : 6020,
    "eligible" : True} 


print(d)
print(d.keys())
print(d.values())

# both are same but first one shows error if name is not in the dict where d.get shows none
print(d["name"])    
print(d.get("name"))


print("\n")
#-----
for key in d.keys():
    print (key)
    print (d[key])
    print("\n")


print("\n")

for key, value in d.items():
    print(key)
    print(value)