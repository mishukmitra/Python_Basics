with open("myfile_4.txt", "w") as f:
    f.write("This is a python learning class. \n")

with open("myfile_4.txt", "a") as f:
    f.write("this is a append line \n")


with open("myfile_4.txt", "a") as f:
    f.write("this is also a append line huhhahh")

##----readline is used to read line by line--------
with open("myfile_4.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)

