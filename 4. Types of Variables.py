#types of variables in python
#variables are of two types : instance variables and class/static variables
class Car:
    wheels = 4 #variables outside init are called class variables
    def __init__(self,mileage=10,company="BMW"):
        self.mileage = mileage #variables inside init are called init and are changeable from object to object
        self.company = company

Lola = Car(mileage=250,company="Mustang")
Bhola = Car()
print(Lola.company)
print(Bhola.company)
Lola.company = "Swift"
print(Lola.company)
print(Lola.wheels,Bhola.wheels)
Lola.wheels = 5 #class variables are also changeable but are set to default and cannot be declared per object.
print(Lola.wheels)
Dora = Car(mileage=255,company="Maruti")
print(Dora.wheels)
Car.wheels = 5 #this permanently modifies class variable for all instances
print(Dora.wheels, Bhola.wheels)