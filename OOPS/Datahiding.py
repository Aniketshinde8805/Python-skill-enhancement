#private data members
#syntax :  __varname
__num=10

#private methods
#Syntax :  __function_name(args...)
def __display(self,n1,n2):
    pass


#prodected members
#syntax : _varname
_count=45

#protected Methods
#syntax:  _fun_name(args)
def _details(self,name,age):
    pass

#Public data members
#syntax : varname
sum=99


class Test():
    __h=10
    _a=9
    g=345
    def add(self,n1):
        self.n1=n1
        print(self.n1)
        self.__h=self.__h+10
        print(self.__h)
        print("This is Public method of class Test")

    def __display(self):
        print("This is private method of class Test")

    def _display1(self):
        print("This is protected method of class Test")

class SubTest(Test):
    def sub(self):
        print("This is Public method of Clas SubTest")


obj1=SubTest()
obj1.sub()
obj1.add(11111)
# obj1.__display()
obj1._display1()

print(obj1.g)
print(obj1._a)
# print(obj1.__h)  #child class object cannot access private data members outside the class


obj2=Test()
# obj2.__display()
# print(obj2.__h)   cannot access outside the class
print(obj2._a)
print(obj2.g)



#Trick to access private data members outside the class
print(obj2._Test__h)