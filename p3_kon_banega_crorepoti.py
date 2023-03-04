questions_1 = [["What is the capital of Austria", "Vienna", "Innsbruck", "Salzburg", "Linz", 1],
            ["Which flower is red", "Gadha", "beli", "Rajanignadha","Rose", 4]]

questions_2 = [["WWhere is Austria", "Europe", "Asia", "Africa", "Australia", 1],
            ["Which flower is blue", "Gadha", "Nilkantha", "Rajanignadha","Beli", 2]]

questions_3 = [["What is the capital of Germany", "Vienna", "Innsbruck", "Berlin", "Salyburg",3 ],
            ["Which flower is yellow", "Gadha", "beli", "Rajanignadha","Nilkantha", 1]]


levels =[50000, 100000, 1000000]
total = 0
break_flag = False
for l in range(0, len(levels)):
    print (f"Questions for TK: {levels[l]}")
    for i in range(2):
        if l==0:
            q = questions_1
            
        elif l==1:
            q = questions_2
        else:
            q = questions_3
        print (q[i][0])
        print(f" 1) {q[i][1]}   2) {q[i][2]}")
        print(f" 3) {q[i][3]}   4) {q[i][4]}")
        enter = int(input("Enter your answer from 1 - 4: "))
        if (enter == int(q[i][-1])):
            print(f"your ans is correct. you won TK: {levels[l]}")
            total = total + levels[i]
        else:
            print(f"ooops!!!Wrong answer!!!")
            break_flag = True
            break
    print(f"Your total amount TK: {total}")
    if break_flag:
        break

    
   

