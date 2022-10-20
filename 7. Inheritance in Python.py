#inheritance
class A:
    def feature1(self):
        print("Feature 1 Working")
    def feature2(self):
        print("Feature 2 Working")
class B(A): #imparting another class in parantheses during the declaration of a new class
    #makes the new class a daughter class // sub class of the (paranthesized) class.
    def feature3(self):
        print("Feature 3 Working")
    def feature4(self):
        print("Feature 4 Working")
    



a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature1(),b1.feature2(),b1.feature3(),b1.feature4()
class D:
    def feature6(self):
        print("Feature 6 Working")
    def feature7(self):
        print("Feature 7 Working")
        
# can be implemented through a multilevel hierarchy
class C(A,D):
    def feature6():
        print("feature6 working")
c1 = C()
#c1 has all features of D and A