#types of inheritance
#Single Inheritance
#Mulilevel Inheritance
#Multiple Inheritance
#Heirarchial Inheritance
#Hybrid Inheritance


#Single Inheritance
#one parent and one child class




class Parent:
    def add(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print("sum=",self.n1+self.n2)

class Child(Parent):
    def sub(self,x,y):
        self.x=x
        self.y=y
        print("sub=",self.x-self.y)

obj1=Child()
obj1.sub(11,5)
obj1.add(14,6)

print("----------------------------------")
#multilevel Inheritance
# A parent class has one child class and that child class has a child class

class Grandfather():
    def fun1(self,gname,surname):
        self.gname = gname
        self.surname = surname
        print("Name:",gname)
        print("Surname:",surname)

class Father(Grandfather):
    def fun2(self,fname):
        self.fname = fname
        print("Name:",fname)


class Child(Father):
    def fun3(self,name):
        self.name = name
        print("Name:",name)
        
cc=Child()
cc.fun3("Tom")
cc.fun2("Gary")
cc.fun1("Benjamin", "Howard")
print(cc.surname)
print(cc.name)
print(cc.fname)
print(cc.gname)

ff=Father()
ff.fun2("Harry")
ff.fun1("Rob","Owen")
print(ff.surname)
print(ff.fname)
print(ff.gname)
print(ff.fname)


gg=Grandfather()
gg.fun1("Tim","Lee")
print(gg.gname)
print(gg.surname)


print("----------------------------")
#Heiracheal Inheritance
#one parent multiple child class

class Parent:
    def parent_fun(self):
        print("This is parent function")
class Child1(Parent):
    def child1_fun(self):
        print("this is Child1 function")
class Child2(Parent):
    def child2_fun(self):
        print("this is Child2 function")

cc=Child2()
dd=Child1()
dd.child1_fun()
dd.parent_fun()
cc.child2_fun()
cc.parent_fun()

print("--------------------------------------")
#Multiple Inheritance
#Multiple Parent classes to single Child
class Parent1:
    def parent1_fun(self):
        print("This is Parent2 function")
class Parent2():
    def parent2_fun(self):
        print("this is Parent2 function")
class Child(Parent1,Parent2):
    def child_fun(self):
        print("this is Child function")

mm=Child()
mm.child_fun()
mm.parent1_fun()
mm.parent2_fun()