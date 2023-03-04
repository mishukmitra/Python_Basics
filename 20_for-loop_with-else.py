# as far we know "else" is used for "if else" statement
# but "else" can be used with "for loop / while loop"

for i in range(5):
    print (i)

else:
    print("the loop is completed")
    # "else" will be executed once the "for" loop is completed


# if we use break  "for" loop it will not print "else" bcoz "for" loop is not completed

for i in range(5):
    print (i)
    if i==2:
        break
        

else:
    print("the loop is completed")