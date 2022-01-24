#constructors in python3
# def __init__(self,arg1,arg2)
#types of constructor
#Parameterized constructor
#Non Parameterized constructor

#Non Parameterized constructor
class Name:
    def __init__(self):
        print("Constructor of class Name is invoked")

n1=Name()
print("---------------------------------------------------------------------------")
#Parameterized constructor
class Car:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        print("Constructor of class Car is invoked")
c1=Car("BMW","Black") 





