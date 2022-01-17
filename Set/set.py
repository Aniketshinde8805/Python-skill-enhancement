s1={1,2,3,4,5,6,6,6,6} # set does not allow duplicate values
print(s1)

s2=set()
s2.add(33)
s2.add(44)
print(s2)


#add()
#this method is used to add element to set 
ss={"dfgkl","jy5",345}
ss.add(0)
ss.add(457345)
t1=1,2,3,4,5,6  #set can contain tuple data 
ss.add(t1)
print(ss)

#remove()
sg={4,6,989,34,76,45,345}
print(sg)
sg.remove(989)
print(sg)
sg.remove(4)
print(sg)


#union() or  A+B
s1={1,2,3,4,5,6,7}
s2={6,7,8,9,10,11,12}
su=s1.union(s2)
print(su)
A={1,2,3,4,5,6,7}
B={6,7,8,9,10,11,12}
C=A|B
print(C)


#intersection() or A&B
si=s1.intersection(s2)
print(si)
A={1,2,3,4,5,6,7}
B={6,7,8,9,10,11,12}
C=A&B
print(C)

#difference()  or A-B
sd=s1.difference(s2)
print(sd)
A={1,2,3,4,5,6,7}
B={6,7,8,9,10,11,12}
C=A-B
print(C)

#symmetric_difference()  or A^B
sid=s1.symmetric_difference(s2)
print(sid)
A={1,2,3,4,5,6,7}
B={6,7,8,9,10,11,12}
C=A^B
print(C)


#subset  <=   
# in <= it returns true if the LHS is subset of RHS and  both must be of type set
l1=[3,4,5,6]
se={1,2,3,4,5,6,7,8,9,10}
su={3,4,5,6}
sf={1,2,3,4,5,6,7,8,9,10}
print(su<=se)
print(se<=sf)  # here se and sf contain same elements and are equal , it returns true
# print(su<=l1)   this gives error because of different datatype


#issubset()
# the difference between issubset and <= is that in issubset() either LHS and RHS can be of different datatype
l1=[3,4,5,6]
l2=[1,2,3,4,5,6,7,8,9,10]
se={1,2,3,4,5,6,7,8,9,10}
su={3,4,5,6}
sf={1,2,3,4,5,6,7,8,9,10}
print(su.issubset(se))
print(su.issubset(l1))
print(se.issubset(l2))
print(sf.issubset(se))# here se and sf contain same elements and are equal , it returns true


#proper subset <
print("proper subset")
l1=[3,4,5,6]
l2=[1,2,3,4,5,6,7,8,9,10]
se={1,2,3,4,5,6,7,8,9,10}
su={3,4,5,6}
sf={1,2,3,4,5,6,7,8,9,10}
print(su<se)
print(se<sf)# here se and sf contain same elements and are equal , it returns False because its not proper subset


#super set >=
# in >= it returns true if the LHS is subset of RHS and  both must be of type set
l1=[3,4,5,6]
se={1,2,3,4,5,6,7,8,9,10}
su={3,4,5,6}
sf={1,2,3,4,5,6,7,8,9,10}
print(se>=su)
print(se>=sf) # here se and sf contain same elements and are equal , it returns true
#print(su>=l1)   this gives error because of different datatype


#issuperset()
# the difference between issubset and >= is that in issuperset() either LHS and RHS can be of different datatype
l1=[3,4,5,6]
l2=[1,2,3,4,5,6,7,8,9,10]
se={1,2,3,4,5,6,7,8,9,10}
su={3,4,5,6}
sf={1,2,3,4,5,6,7,8,9,10}
print(se.issuperset(su))
print(se.issuperset(l2))
print(se.issuperset(se))
print(sf.issuperset(se))# here se and sf contain same elements and are equal , it returns true



#proper superset >
print("proper superset")
l1=[3,4,5,6]
l2=[1,2,3,4,5,6,7,8,9,10]
se={1,2,3,4,5,6,7,8,9,10}
su={3,4,5,6}
sf={1,2,3,4,5,6,7,8,9,10}
print(se>su)
print(se>sf)# here se and sf contain same elements and are equal , it returns False because its not proper superset

#membership
ss={1,2,3,4,5,6,7,8,9,10}
for i in ss:
    print(i)





# #enumerate()
# The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
# The enumerate() function adds a counter as the key of the enumerate object.
# Syntax  enumerate(iterable, start)
# Parameter	Description
# iterable	An iterable object
# start	    A Number. Defining the start number of the enumerate object. Default 0
t1=(1,2,3,4,5,6)
y=enumerate(t1)
print(list(y))
print(tuple(y))

for i,element in enumerate(t1):
    print(i,element)


# #zip()
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together,
#  and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
# Syntax  zip(iterator1, iterator2, iterator3 ...)
# Parameter Values
# Parameter	Description
# iterator1, iterator2, iterator3 ...	Iterator objects that will be joined together

l1=[1,2,3,4]
l2=[1,1,2,4,5,6,9]
print(list(zip(l1,l2)))
for i in zip(l1,l2):
    print(i)
for i,j in zip(l1,l2):
    if i==j:
        print("Same ")
    else:
        print("Not Same")

ll=['a','b', 'c', 'd', 'e', 'f']
lk=[1,2,3,4,5,6,7,8,9,10]
ls=["one","two","three","four","five","six","seven","eight"]
print(list(zip(ll,lk,ls)))
for i in zip(ll,lk,ls):
    print(i)