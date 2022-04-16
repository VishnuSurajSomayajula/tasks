class Calcus:
    def Square(self,a,b):
        return a**b
class Calcus1:
    def Mult(self, a,b):
        return a*b
class Derived (Calcus,Calcus1):
    def fDivide(self,a, b):
        return a//b
d = Derived ()
print(d.Square(10,20))
print(d.Mult(10,20))
print(d.fDivide(10,20))
