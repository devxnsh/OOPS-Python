#duck typing
#if it looks like a duck,swims like a duck and quacks like a duck, it is a duck. Probably.
class PyCharm:

    def execute(self):
        print("Compiling...")
        print("Running...")

class MyEditor:
    
    def execute(self):
        print("Spell Check...")
        print("Convention Check...")

class Laptop:
    
    def code(self,ide):
        ide.execute()

ide1 = PyCharm()

lap1 = Laptop()
lap1.code(ide=ide1)

ide1 = MyEditor() 
lap1.code(ide=ide1)
#same variable can be assigned to a different class if their construction is identical.
#thats all duck typing is. If it has the function execute, it doesnt matter to code(function) which class its from.
#Personally, I was expecting some swimming.
