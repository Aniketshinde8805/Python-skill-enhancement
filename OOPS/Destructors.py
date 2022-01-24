#Destructors in python 
print("----------------------Destructors------------------------------------")
class One:
    def __init__(self):
        print("Constructor invoked")
    def __del__(self):
        print("Destructor invoked ")
v1=One()
del v1