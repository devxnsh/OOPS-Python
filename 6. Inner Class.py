class Student:
    def __init__(self,name,rollno,brand="HP",cpu="i5",ram=8):
        self.name=name
        self.rollno=rollno
        self.lap = self.Laptop(brand,cpu,ram)
    def show(self):
        print(self.name, self.rollno)
    

    class Laptop:

        def __init__(self,brand="DELL",cpu="i3",ram=16): #these default values will be called only when this class is utilized directly
            self.brand,self.cpu,self.ram = brand,cpu,ram
        def show(self):
            print(self.brand, self.cpu,self.ram)
S1 = Student("Navin",25525,"HP","AMD RYZEN",8)
S2 = Student("Pravin",26252)
print(S2.lap.ram)

lap1 = Student.Laptop()
print(lap1.brand)
Stud1 = Student("Nitin",22525,lap1.brand,lap1.cpu,lap1.ram)
print(Stud1.lap.ram)
Student.Laptop.show(lap1) 