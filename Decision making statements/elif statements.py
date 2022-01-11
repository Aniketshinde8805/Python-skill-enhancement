# elif 

a=int(input("enter numbers"))
b=int(input("enter numbers"))
c=int(input("enter numbers"))
d=int(input("enter numbers"))
if a>b and a>c and a>d:
    print("a is greatest")
elif b>c and b>d and b>a:
    print("b is the greatest")
elif c>d and c>a and c>b:
    print("c is the greatest")
else:
    print("d is the greatest")


print("\npostitive, negative or zero")
num=int(input("enter a number"))

if num<0:
    print("number is Negative")
elif num>0:
    print("Number is positive")
elif num==0:
    print("number is zero")