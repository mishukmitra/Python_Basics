# seek and tell in "read" mode
with open("myfile_6.txt", "r") as f:

    f.seek(4) # start after 4 bytes,  skip first 4 bytes 

    
    data = f.read(5) # read 5 bytes
    print(data)

    print(f.tell()) # bytes executed so far

