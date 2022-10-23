#types of variables in python
#variables are of two types : instance variables and class/static variables
class Car:
    wheels = 4 #variables outside init are called class variables
    def __init__(self,mileage=10,company="BMW"):
        self.mileage = mileage #variables inside init are called init and are changeable from object to object
        self.company = company

CarA = Car(mileage=250,company="Mustang")
CarB = Car()
print(CarA.company)
print(CarB.company)
CarA.company = "Swift"
print(CarA.company)
print(CarA.wheels,CarB.wheels)
CarA.wheels = 5 #class variables are also changeable but are set to default and cannot be declared per object.
print(CarA.wheels)
CarC = Car(mileage=255,company="Maruti")
print(CarC.wheels)
Car.wheels = 5 #this permanently modifies class variable for all instances
print(CarC.wheels, CarB.wheels)