import os


# if the folder not exist then make
if (not os.path.exists("29_os_module")):
    os.mkdir("29_os_module")


# if subfolders not exist then make some
for i in range(1,11):
    if (not os.path.exists(f"29_os_module/Tutorial_{i}")):
        os.mkdir(f"29_os_module/Tutorial_{i}")

# verify a file exist
print(os.path.isfile('Tutorial_3/sales.txt'))




print("\n")
# # list files from a working director
folders = os.listdir("29_os_module")



for folder in folders:
    print(folder)
    print(os.listdir(f"29_os_module/{folder}"))


# os.rmdir("data")

print(os.getcwd()) # directory
# os.chdir("\Users") # change directorry


#-----------------------------------------------------------------

if not os.path.exists("31_File_IO"):
    os.mkdir("31_File_IO")


if not os.path.exists(""):
    os.mkdir("32_readline()")