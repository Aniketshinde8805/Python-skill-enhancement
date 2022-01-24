


class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print("Name:",self.name)
        print("Id:",self.id)

class Employee(Person):
    def __init__(self,salary,dept,name,id):
        self.salary = salary
        self.dept = dept
        #invoke the constructor of parent class
        Person.__init__(self,name,id)
    def displayall(self):
        print("salary:",self.salary)
        print("dept:",self.dept)
        super().display()   #super() method call Parent method in Child class method
 
emp1=Employee(id=245345,name="Mohan",salary=30000,dept="Sales")
emp1.displayall()
obj=12

print(issubclass(Employee,Person))   #True
print(issubclass(Person,Employee))  #False
print(isinstance(emp1,Employee)) #True
print(isinstance(emp1,Person))  #True
print(isinstance(obj,Person)) #True
