# map() is similar to filter()
# but the only difference is that in map the function  given as argument
# is not used as a condition

l=[1,2,3]
m=lambda x:x**2
res=list(map(m,l))
print(res)

res2=list(filter(m,l))
print(res2)
#here it does not return list of squares , it just returns the list

l2=[3,4,7,8,44]
n=lambda x: x*1000
res4=list(map(n,l2))
print(res4)