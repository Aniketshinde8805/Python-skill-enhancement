a=[1,2,3,4,5,6]
print(a)
b=a[:]
print(b)
a.pop()  # change in a will not reflect on b
print(a)
print(b) # change in a will not reflect on b


a=[1,2,3,4,5,6]
print(a)
b=a
print(b)
a.pop()  # change in a will  reflect on b
print(a)
print(b) # change in a will  reflect on b
print(id(a),id(b))  # a and b refer to same id   ie memory location


# unpackin a list
a,b,c=[1,2,3]
print(a,b,c) 
a,*b,c =1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16  # in this case a will get value 1 and c will get the last and rest will be assigned to c
print(a,b,c)
*a,b,c =1,2,3,4,5,6,7,8,9,10
print(a,b,c)

l1=[0,1,2,3,4,5,6,7,8,9,10]
print(l1[0])
print(l1[5])
print(l1[:])
print(l1[3:8])
print(l1[:5])
print(l1[4:])
print(l1[::-1])  # reverse list
print(l1[::3]) # print value on index interval of 34


# updating values of list
a=[1,2,3,4,5,6]
print(a)
a[1:3]="h","i"
print(a)
b=[1,2,3,4,5,6]
b=b+[9999]
print(b)


#deleting list elements
ll=['a','b','c','d','e','f']
print(ll)
del(ll[3:5])   #deleting elements in range
print(ll)
del(ll)   # del whole list

