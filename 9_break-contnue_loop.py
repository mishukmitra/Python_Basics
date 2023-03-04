
# break = stop and go out from the Look
# continue = skip and continue looping(to check someehere between loop)





# example 1 using for

for i in range(15):
   print("5 x",(i+1),"=", 5*(i+1)) # i+1 for starting from 1

   if i == 9:
    break

print("\n")
# example 2 using for

for i in range(15):
    if i == 0:
        print("i =",i,  "we dont want starts from 0 so skip and continue loop")
        continue
    elif i == 5:
        print("5 x",i,"=", 5*i, "checking if I am in the middle ")
    elif i >= 11:
        break
    
    print("5 x",i,"=", 5*i)


print("\n")
# example 3 using while loop 
# do while loop


# while true is a infinty loop


i = 1
while True:
    print(i)
    i = i + 1
    if i % 10 == 0:
        break
