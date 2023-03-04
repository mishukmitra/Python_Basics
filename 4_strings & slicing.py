name = "Mishuk"

length = len(name)
print("My name has", length, "letters")


print(name[0])
print(name[0:4])

print("\n")


for characters in name:
    print(characters)

print("\n")
for i in range(length):
    print(name[i])


print("\n")

# strings are immutable
# but we can create new strings and change






song = '''Twinkle, twinkle, little star, 
How I wonder what you are! 
Up above the world so high,
Like a diamond in the sky!!!!!'''

print(song.upper())
print(song.capitalize())
print(song.lower())
print(song.count("twinkle"))

print(song.startswith("Twinkle"))
print(song.endswith("is"))
print(song.endswith("sky."))
print(song.find('star'))


print(song.replace("diamond", "gold "))
print(song.split())

print(song.isalpha())

print(song.istitle())

print(song.rstrip("!"))
print(song.replace("!!!!!", "."))

song += "\n new added line by my"
print(song)