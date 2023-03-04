import time

# from time import gmtime, strftime
# print(strftime("%H:%M:%S"))

t = time.strftime("%H:%M:%S %p")
print(t)


t_hour = time.strftime("%H")
t_min = time.strftime("%M")
t_sec = time.strftime("%S")


if 6 < int(t_hour) < 12:
    print("Good Morning! Mishuk.")
elif 12 < int (t_hour) < 5:
    print("Good Afternoon! Mishuk.")
elif 5 < int (t_hour) < 24:
    print("Good Evening! Mishuk.")
else:
    print("Good Night! Mishuk.")





