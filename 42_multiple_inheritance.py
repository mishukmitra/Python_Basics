class Student:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"I am {self.name}")

class Player:
    def __init__(self, sport):
        self.sport = sport
    
    def show(self):
        print(f"I am playing {self.sport}")


class Student_and_Player(Student, Player):
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport


o = Student_and_Player("John", "Football")
o.show()