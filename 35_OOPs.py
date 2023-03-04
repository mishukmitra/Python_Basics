# Object Oritented Programming's
    # Class # Object
    
# --------------------Class--------------------------------------
class form:
    name = ""
    train = ""
    ticket= ""

    def info(self):
        print(f"Hi {self.name}! Welcome to {self.train}. your  ticket no. is: {self.ticket}.")


# --------------------Object----------1-------
a = form()

a.name = "Manashi"
a.train = "Rajanigandha Express"
a.ticket = "2344"
a.info()

a.name = "Bose"
a.info()
# --------------------Object----------2--------
b = form()

b.name = "Mishuk"
b.train = "DB"
b.ticket = "930456"
b.info()



