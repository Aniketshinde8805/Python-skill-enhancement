class Double:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,q):
        return self.x+q.x,self.y+q.y

ob1=Double(2,3)
ob2=Double(3,2)
print(ob1+ob2)


class Point:
    def __init__(self,x):
        self.x = x
    def __add__(self,p):
        return self.x+p.x
    def __sub__(self,p):
        return self.x-p.x
    def __mul__(self,p):
        return self.x*p.x
    def __truediv__(self,p):
        return self.x/p.x
    def __floordiv__(self,p):
        return self.x//p.x
    def __mod__(self,p):
        return self.x%p.x
    def __pow__(self,p):
        return self.x**p.x
    def __rshift__(self,p):
        return self.x>>p.x
    def __lshift__(self,p):
        return self.x<<p.x
    def __and__(self,p):
        return self.x&p.x
    def __or__(self,p):
        return self.x|p.x
    def __xor__(self,p):
        return self.x ^ p.x



    
    

obj1=Point(3)
obj2=Point(7)
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)
print(obj1**obj2)
print(obj1/obj2)
print(obj1//obj2)
print(obj1%obj2)
print(obj1>>obj2)
print(obj1<<obj2)
print(obj1&obj2)
print(obj1 | obj2)
print(obj1 ^ obj2)