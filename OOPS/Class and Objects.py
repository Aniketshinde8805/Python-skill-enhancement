class One:
    num=100  # class variable
    def fun1(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(f"value of n1 is {self.n1}") #instance variable
        print(f"value of n2 is {self.n2}") #instance variable
    

aa=One()  #creating class Object
print(aa.num)
aa.fun1(11,12)



print("-------------------------------------------------------------------------")
class Phone:
    def set_color(self,color):
        self.color=color
        print(f"color is {color}")
    
    def set_price(self,price):
        self.price=price
        print(f"price is {price}")

    def display(self):
        print(f"color: {self.color}")
        print(f"price: {self.price}")

p=Phone()
p.set_color("RED")
p.set_price(10000)
p.display()


print("-------------------------------------------------------------------------")
class Number:
    def set_num(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def cal_sum(self):
        print("sum=",self.n1,self.n2)

s=Number()
s.set_num(1,2)
s.cal_sum()

print("-------------------------------------------------------------------------")
class Student:
    'This is a class that contains Student details and marks'
    def student_details(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    def student_marks(self,maths,physics,chem):
        self.maths=maths
        self.physics=physics
        self.chem=chem
    def display_stud_details(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Id:",self.id)

    def display_stud_marks(self):
        print("Maths:",self.maths)
        print("Physics:",self.physics)
        print("Chem:",self.chem)

s1=Student()
s1.student_details("Aniket",23,1103)
s1.student_marks(40,34,34)
s1.display_stud_details()
s1.display_stud_marks()

#Built in class Attributes
# __dict__: Dictionary containing the class's namespace
print(Student.__dict__)
#__doc__: Class documentation string or none, if undefined.
print(Student.__doc__)
#__name__: Class name.
print(Student.__name__)
#__bases__: A possibly empty tuple containing the base classes,
print(Student.__bases__)
#__module__:Module name in which the clas is defined
print(Student.__module__)


