# -----------read mode............

f1 = open("myfile.txt", "r")
print(f1.read())
f1.close


#-----------write mode--------
f2 = open("myfile_2.txt","w")
f2.write("I am Mishuk")
f2.close

#shortcut
with open("myfile_3.txt","w") as f3:
    f3.write("I am a good boy. ")



#-----------append mode--------for editing-------
with open("myfile_3.txt", "a") as f4:
    f4.write("I am also Innocent")