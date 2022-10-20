class A:
    def __init__(self):
        print("This is A function")
    
    def Feature1(self):
        print("Feature1")

    def Feature2(self):
        print("Feature2")


class B(A):
    def __init__(self): #if removed, B function will automatically call the init of A-class.
        super().__init__() #calls init of first class
        print("This is B Function")
    def Feature3(self):
        print("Feature3")

    def Feature4(self):
        print("Feature4")

#in cases of multiple inheritance, the parent class declared first in parantheses is considered primary superclass
a1=A()
b1=B()
