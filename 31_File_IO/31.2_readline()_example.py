# -------Real example, when we will do machine learning--------

student = 0
with open("marks.txt", "r") as f:
    while True:
        line = f.readline()
        # print(line)
        student = student + 1
        if not line:
            break

        
        # split: put line row in a list separately, and makes matrix
        l1 = line.split() # select index 1 from the matrix
        
        print(f"Student {student}: Math result: {l1[0]} ")
        print(f"Student {student}: physics result: {l1[1]} ")
        print(f"Student {student}: chemistry result: {l1[2]} \n")

        
        
        