# #exceptions
# x=10
# y=2
# print("sum=",x+z)


try:
    pass  # code which might raise error 
except:
    pass  # catch error and displays to user


# x=10
# y=0
# print("quotient=",x/y)
# print(x)
# print(y)


try:
    x=10
    y=0
    z=x/y
    print("quotient=",z)
except:
    print("cant divide by zero")


try:
    x=int(input("enter a number"))
    y=int(input("enter a number"))
    z=x/y
    print("quotient=",z)
except ValueError:
    print(" value is wrong")
except ZeroDivisionError:
    print("can't divide by zero")


try:
    x=int(input("enter a number"))
    y=int(input("enter a number"))
    z=x/y
    print("quotient=",z)
except (ValueError, ZeroDivisionError):
    print("try with valid inputs")
    

# try:
#     x=int(input("enter a number"))
#     y=int(input("enter a number"))
#     z=x/y
#     print("quotient=",c)
# except ValueError:
#     print(" value is wrong")
# except ZeroDivisionError:
#     print("can't divide by zero")
# except NameError:
#     print("name not definde")


sums=11
try:
    print(sums)
# except:
#     print("error 1")
except:
    print('valiable not defined')
else:
    print("successfully executed")


# finally block
q=0
try:
    print(q)
except:
    print(" variable not defined")
finally:
    print("exception is handled")


try:
    f = open('filez.txt','r')
    f.write("he")
except:
    print("open the file in write mode to write to the file")
finally:
    f.close()


# raise Exception
a=-10
if a <0:
    raise Exception("value of a should be greater than 0")


c="aniket"
if type(c) is not int:
    raise TypeError('please enter valid data type input')



# custom exceptions
# there is exception class
class Value(Exception):
    pass
    


try:
    x=-1
    if x<0:
        "hh"
        raise Value
except Value:
    print("value is less than 0")


c=-22
if c<0:
    raise Value


class divisionnotpossible(Exception):
    pass
try:
    x=int(input("enter no"))
    y=int(input("enter no"))
    if y==0:
        raise divisionnotpossible
    z=x/y
except divisionnotpossible:
    print(" y cannot be zero")
