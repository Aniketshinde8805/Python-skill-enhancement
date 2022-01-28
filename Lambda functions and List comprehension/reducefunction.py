from functools import reduce

l1=[2,4,6,8,10]
m=lambda x,y:x+y
r1=reduce(m,l1)
print(r1)

l2=[1,2,3,4,5]
n=lambda x,y:x*y
r2=reduce(n,l2)
print(r2)



