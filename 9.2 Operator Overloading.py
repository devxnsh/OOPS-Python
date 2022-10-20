
## __add__(a,b) is the behind the scene function when a+b is called. (in class int)
#methods like __add__, __sub__,__mul__ etc have abbreviations like + , - , * so as to make code more readable
class Mathematicians:
    def __init__(self,number) :
        self.number = number
    def __add__(self,other):
        return self.number + other.number 

Ram = Mathematicians(5)
Shyam = Mathematicians(35)
print(Ram+Shyam) #will not work if __add__ is not defined