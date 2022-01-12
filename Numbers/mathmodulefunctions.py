import math

# math.ceil()
#	Rounds a number up to the nearest integer
aa=104.4545
print(math.ceil(aa))

# math.fabs() returns the absolute value of the number  ie removes the sign of the number
dd=-49359
print(math.fabs(dd))
dd1=+34545
print(math.fabs(dd1))


# math.exp()
#Return 'E' raised to the power of different numbers:
# syntax  math.exp(x)
print(math.exp(345))


# math.pow(value,pow)  ie value^pow
# it reutrns the value of base to the power
# here value is the base and pow it the exponent(power)
# value is of float data type
print(math.pow(9,2))  # printing square of 9
print(math.pow(10,5)) # printing 10 to the power 5


#math.floor(value)
# The math.floor() method removes all the decimal digits
# it does not round the digits
print(math.floor(123.6778))
print(math.floor(99.99999))
print(math.floor(10.0))


#The math.log() method returns the natural logarithm of a number, or the logarithm of number to base.
# Syntax math.log(x, base)
# if the base is not specified, then the base is "e" by default
print(math.log(345,10))
print(math.log(345))
print(math.log(67,8))


#math.log10(x)
# it returns the log value of given number to base 10.
#Syntax  math.log10(x)
print(math.log10(99))  
print(math.log10(43))
print(math.log10(55),math.log(55,10))  # printing log of 55 to base 10 with different method


#math.sqrt(value)
# it returns square root of given number
#syntax math.sqrt(x)
print(math.sqrt(9))
print(math.sqrt(81))
print(math.sqrt(121))
print(math.sqrt(147))


#math.fmod(x,y)
# it gives the remainder of x/y
#syntax math.fmod(x,y)
print(math.fmod(45,9))
print(math.fmod(10,3))
print(math.fmod(937,177))


#cmp(x, y)	(-1 if x < y, 0 if x == y, or 1 if x > y)	 
# cmp() function is not used in python 3