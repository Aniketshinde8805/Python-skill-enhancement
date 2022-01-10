# logical operators

#and
a=True
b=False
c=True

print(a and b)
print(a and c)

# or

a=True
b=False
c=True
print(a or b)
print(a or c)

#not
a=True
b=False
c=True
print(not a)
print(not b)
print(not c)

#▪ Membership Operators
# in
l1=[1,2,3,4,5,6,7]
print(3 in l1) 

# not in 
l1=[1,2,3,4,5,6,7]
print(100 not in l1) 

# Identity Operators
print("\nIdentity Operators ")
#  is
num=100
num2=num
bbb=100
print(num is bbb)
print(num is num2)

#  is not
num=100
num2=num
bbb=100
print(num is not bbb)
print(num is not num2)