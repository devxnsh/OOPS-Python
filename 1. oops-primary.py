class Computer:
    #attributes are variables and behaviour means method/function
    
    def config(self):
        print("i3,16GB,1TB")

com1 = Computer() #constructor
com2 = Computer() #constructor
print(type(com1))
#accessing a function//behavior out of the class:
Computer.config(com1) #will work
#config() won't
com1.config() #will also work