class Person:
    def __init__(self,NameSelf="Dev",AgeSelf=19): #setting default values for arguments
        self.Name = NameSelf
        self.Age = AgeSelf
    def update(self,AgeUpdated=20):
        self.Age=AgeUpdated
    def compare(self,other):
        if self.Age == other.Age and self.Name==other.Name:
            print("Same")
        else:
            print("Not Same")
c1=Person(NameSelf="Harry",AgeSelf=31)
c2=Person()
print(c1.Name, " || ",c2.Name) #callling value of declared variable
print(c1.Age, " || " ,c2.Age) #calling value of declared variable
c2.update(AgeUpdated=25) #works with and without a parameter. Can also be used like Person.update(c2,AgeUpdated=25)
c1.update() #works with and without a parameter. Can also be used like Person.update(c1,AgeUpdated)
print(c1.Age, " || " ,c2.Age) #calling value of declared variable

#comparing
c1=Person(NameSelf="Harry", AgeSelf=25)
c2=Person(NameSelf="Harry",AgeSelf=22)
c1.compare(c2)
c2.update(AgeUpdated=25)
c1.compare(c2)