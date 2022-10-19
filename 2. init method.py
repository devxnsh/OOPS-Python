#init method and variables
class Computer:
    #attributs are variables and behaviour means method/function
    def __init__(self,CPU,RAM):
        #the idea behind init is, it gets called automatically whenever a constructor is called.
        self.CPU = CPU
        self.RAM = RAM    
    
    def config(self):
        print("Config is: ",self.CPU,",",self.RAM)

com1 = Computer("i5","16GB") #constructor
com1.config()
com2 = Computer("AMD Ryzen 6","8GB") #constructor
com2.config()