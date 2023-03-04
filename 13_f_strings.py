name = "Mishuk"
country = "Bangladesh"
address = {"street" : "Leopoldstraßse",
            "house" : "42a",
            "plz" : "6020",
            "city" : "Innsbruck",
            "country" : "Austria"}

me = "My name is {}, I am from {}, I live in {}."

p = me.format(name, country, address["country"])
print(p)

c = address["country"]
print(f"My name is {name}, I am from {country}, I live in {c}.")
print(f"My name is {{name}}, I am from {{country}}, I live in {{c}}.")


price = 55.345345

print(f"The price of the flower is {price}")
print(f"The price of the flower is {price: .3f}")