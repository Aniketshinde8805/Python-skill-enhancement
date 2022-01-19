#functions
#block of statements that perform a specific task
#advantages:
#avoid repititions 
#reusability
#modularity 

#functions
#block of statements that perform a specific task
#advantages:
#avoid repititions 
#reusability
#modularity 

#syntax of creating function
#def fun_name(arguments/parameters):
#   statements
    
def message():       #function without arguments and return statements
    print("welcome all")
    print("to python session")
#call to function
message()

def add():
    a=int(input("enter first no"))
    b=int(input("enter second no"))
    c=a+b
    print(c)
#function call
add()

#factorial func
def fact():
    n=int(input("enter no"))
    f=1
    for i in range(1,n+1):
        f=f*i
        
    print(f)
fact() 

#function with args
#here a and b are formal arguments
def add(a,b):
    print("sum=",a+b)
    
#here 2 and 4 are actual args 
add(2,4) 
sum= 6
def oddeven(a):
    if(a%2==0):
        print("no is even")
    else:
        print(" no is odd")

n=int(input("enter no"))
oddeven(n)


#function with return type
def message():
    return "hello"
a=message()
print(a)


#function with argumetns and return type
def add(a,b):
    return(a+b)
n=int(input("enter first no"))    
m=int(input("enter second no")) 
c=add(n,m)
print(c)

print(add(5,5))

#rev a string
def rev(str):
    text=str[::-1]
    print(text)
    if(str==text):
        print("its palindrome")
    else:
        print("not a palindrome")
rev("hello")
rev("ili")


def square(a,b):
    return(a*a+b*b)
square(4,10)
116
def max():
    a=int(input("enter first no"))
    b=int(input("enter second no"))
    c=int(input("enter third no"))
    if(a>c and a>b):
        print("max=",a)
    elif(b>a and b>c):
        print("  max=",b)
    elif(c>a and c>b):
        print(" max=",c)
max()


def fun():
    x=10  #local variable
#print(x)  #here it gives error because it is not global variable


y=10  #global variabel
def my_fun():
    global y   #global keyword to modify global variable
    y=y+2
    print(y)
my_fun()
12
# arguments 
#default argument concept
def add(num1=0,num2=9): #always start providing default args from RHS
    print("num1",num1)
    print("num2",num2)
    print("sum=",num1+num2)
add(1,2)

sum= 3
add()

sum= 9
add(1)

sum= 10
def product(a,b,c=3,d=2):
    s=a*b*c*d
    print(s)
product(1,1)
6
#wa fun c
def emp(name,id,sal=10000):
    print("name",name)
    print("id",id)
    print("sal",sal)
emp("aniket",12)

#keyword arguments
def add(n1,n2):
    print("n1=",n1)
    print("n2=",n2)
    print(n1+n2)
add(n1=1,n2=8)
add(n2=6,n1=5)

#add(n2=6,7)#positional argument follows keyword argument 
# add(7,n1=6)    here it will give error because n1 will take 7 then again n1 will be given 6 
  

add(5,n2=6) #here positional args is given first and then keyword args
n1= 5
n2= 6
11
#arbitary arguments
def add(*num):   #it could take n number of arguments
    for i in num:
        print(i)
        
   
add(1)
add(1,3,4)
add(1,2,5,6,7,8)
1
1
3
4
1
2
5
6
7
8
def add(*num):
    s=0
    for i in num:
        s=s+i
    print(s)
add(1,2,3,4,4,5,)  