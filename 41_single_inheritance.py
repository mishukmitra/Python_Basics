class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def make_sound(self):
        print(f"I'm {self.name} and I can make sound like {self.sound}.")


class Dog(Animal):
    def __init__(self, breed):
        self.breed = breed
        Animal.__init__(self,name = "MICHE", sound="Bark!!!" )
    
    def make_sound(self):
        super().make_sound()
        



u = Dog("Shepard")
u.make_sound()

        
    