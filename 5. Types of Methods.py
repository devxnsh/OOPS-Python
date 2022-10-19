#types of methods:
# >Instance methods   >Class Methods    >Static Methods
class Student:
    school = "Telusko"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        avg = (self.m1+self.m2+self.m3)/3
        return avg 
    def get_m1(self): #getter
        return self.m1
    def get_m2(self): #getter
        return self.m2
    def get_m3(self):  #getter
        return self.m3
    def alter_value_m1(self,value): #setter
        self.m1 = value
    def alter_value_m3(self,value): #setter
        self.m3 = value
    def alter_value_m2(self,value): #setter
        self.m2 = value
    @classmethod #if this is not defined, it will remain an instance method. If this is declared we don't have to call it per object but only per class.
    def info(cls): #class method. Fetches class variables
        print(cls.school)
    @staticmethod #is not linked to any class or object. Comes when called upon. True Sigma, Some might conclude.
    def getclassName():
        print("This is the Student Class")


s1 = Student(14,67,32)
s2 = Student(100,100,100)
print(s1.avg())
# Types of instance methods >> Accessors (getters) >> Mutators (Setters)
#Avg method is a getter
Student.info() #had @classmethod not been declared it would be s1.info() or otherobject.info()
Student.getclassName()