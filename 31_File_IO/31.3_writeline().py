lines= ["line1 \n", "line2 \n", "line3  \n", "line4 \n"]

with open("myfile_5.txt", "w") as f:
    f.writelines(lines)