a = int(input("Please enter a number to match: "))

match a:
    case 0:
        print("you entered", a,", matches with case 0")

    case 1:
        print("you entered", a,", matches with case 1")
    
    case 2:
        print("you entered", a,", matches with case 2")
        
    case 3:
        print("you entered", a,", matches with case 3")
        
    case 4:
        print("you entered", a,", matches with case 4")

    case _:
            print("You entered something else")