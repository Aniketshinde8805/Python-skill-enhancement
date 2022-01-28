#filter(fun,iter) is a inbuilt function 
#it takes two arguments
#it take function and iterable as arguments
#the function acts as a condition

#syntax:  filter(fun,iterable_value)
#the filter function returns an iterable value 

l=[1,2,45,67,8,10,11]
y=lambda x:x>10

res=filter(y,l)
for i in res :
    print(i)

print('-------------------------------------')
l1=[34,657,8,4,345,74,3,65,7,43,78,5643,7877]
y1=lambda x:x%2==0

r1=filter(y1,l1)
for i in r1 :
    print(i)

print("--------------------------------------------------")

def fun(x):
    if x<=10:
        print(x)
   
l3=[5,7,8,9,11,21,154,556]
r4=list(filter(fun,l3))
print(r4)

for i in r4:
    print(i)

print('--------------------------------')
ll=[3,56,37,78,44,87,3]
r4=list(filter(lambda x:x%2==0,ll))
print(r4)


