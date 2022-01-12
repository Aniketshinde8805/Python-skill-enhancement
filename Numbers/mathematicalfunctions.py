# abs() function
# it returns the absolute value  ie it removes the sign of the value
a=12.5
print(abs(a))

b=-45
print(abs(b))

#round() function
# it rounds the value to the given number of digits
#syntax :  round(value,n) here "n" is an integer which tells upto how many decimal places to round
aa=3445.34534857394593485
print(round(aa,5)) # rounding upto 5 decimal places
print(round(aa,0))  #rounding upto 0 decimal places
print(round(aa))   # if we don't specify "n" then it rounds upto 0 decimal places and makes it integer
print(type(round(aa)))


#max(x1, x2, x3,.....)
#it returns the max value of the given inputs
print(max(45,67,2,567,22234))
l1=[345,677,54,778,3,4453,4]
print(max(l1))
t1=(454,33,72,34,789,45769,293)
print(max(t1))
d1={"1":345,"4":5646,"56":567567}  # here it returns the key with max value
print(max(d1))
s1={34,66,88,2346,787.78}
print(max(s1))


# min(x1,x2,x3,x4,...)
# it returns the min value of the given inputs
print(min(45,67,2,567,22234))
l1=[345,677,54,778,3,4453,4]
print(min(l1))
t1=(454,33,72,34,789,45769,293)
print(min(t1))
d1={"1":345,"4":5646,"56":567567}  # here it returns the key with min value
print(min(d1))
s1={34,66,88,2346,787.78}
print(min(s1))