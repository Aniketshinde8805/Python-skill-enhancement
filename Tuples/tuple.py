#tuple with single element
t1=(45,)
print(t1)
#tuple
t2=(3,4,5,6,7,84,5,63,535,345,7,7)
print(t2)

t3=2,4,5,67,8,78
print(t3)
print(type(t3))


# convert tuple into list
l1=list(t2)
print(l1)

#accesing elements of tuple
tt=(88,55,3,4,445,76,345,223,45)
print(tt[0])
print(tt[1])
print(tt[2])
print(tt[3])
print(tt[4])

#slicing of tuples
print(tt[3:7])
print(tt[:])
print(tt[:6])
print(tt[4:])
print(tt[::-1])


#concatenation of tuples
t1=(1,2,3,4,5,6)
t2=(7,8,9,10,11,12,13)
t3=t1+t2
print(t3)
print(t1+t2)


#Tuples are immutable ie you cannot change,modify,update,delete elemets of tuples


#delete whole tuple
a=(45,6,34,67,7)
del(a)

#len()
print(len(t1))
print(len(t2))

#max()
print(max(t1))
print(max(t2))

#min()
print(min(t1))
print(min(t2))