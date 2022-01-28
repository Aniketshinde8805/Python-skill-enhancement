#lambda functions are short functions which can take single expressions only 
#lambda functions must be assigned to a variable


y=lambda x:x**2 
print(y(3))
print(y(5))
print(y(9))


y1= lambda x,y:x+y
print(y1(4,5))
print(y1(5,6))


y2=lambda x,y,z:x+y+z
print(y2(10,7,3))

y3= lambda p,q:p**q
print(y3(10,3))
print(y3(10,4))

