#---------------class: parent--------------------------------------
class parent_class:

    def info(self):
        print("I am parent.")
    

#--------------------class: child---------------------------------------
class child_class(parent_class):
    def info2(self):
        print("I am a child class but know my parent university.")
        super().info() # call from parent class and parent method



#-----------------object------------------------------------


ob = child_class()
ob.info()