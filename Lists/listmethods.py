#cmp(list1,list2)    cmp() is not in python3
# l1=[1,2,3,4];l2=[1,2,3,4]
# print(cmp(l1,l2))

#len(list)
#it gives the length of the list
from tkinter import N


ll=[1,2,3,4,5,6,7,8,999,100]
la=['a', 'b', 'c', 'd', 'e', 'f']
print(len(ll))
print(len(la))

#max(list)
# max() in list  returns the element having the maximum value
print(max(ll))
print(max(la))


#min(list)
#min() in list returns the element having the minimum value
print(min(ll))
print(min(la))


#append()
ll=[1,2,3]
print(ll)
ll.append(33)
print(ll)
ll.append(676)
print(ll)

#extend()
l1=['x', 'y', 'z']
print(l1)
l2=['p', 'q', 'r', 's']
print(l2)
l1.extend(l2)
print(l1)


#count()
# The count() method returns the number of elements with the specified value.
# Syntax  list.count(value)
# Parameter	    Description
# value	     Required. Any type (string, number, list, tuple, etc.). The value to search for.
l1=[45,567,345,56,45,567,78,45,5567,345,45]
print(l1.count(45))


#index()
#syntax  list.index(obj)
# this method gives the index of the given object in the  list 
lk=['asdf','dgds','dfg','dfkgj','sddd']
print(lk.index("sddd"))
print(lk.index("dfg"))


#insert(index,obj)
#insert() method is used to insert an object at specific index 
lj=['m','n','o','p']
lj.insert(2,'zzz')
print(lj)
lj.insert(0,'aaaa')
print(lj)


#pop(index)
#pop(index) method is used to delete elements at specific index
# if the index is not give the last element of the list is deleted
pp=['a', 'b', 'c', 'd', 'e', 'f','g', 'h']
pp.pop()
print(pp)
pp.pop(0)
print(pp)
pp.pop(-1)  # this will delete the last element
print(pp)


#remove(obj)
#remove() method is used to delete the object from the list
#here obj is passed as a parameter
mm=['g','h','i','j','k','l','m']
print(mm)
mm.remove('g')
print(mm)
mm.remove('m')
print(mm)


#sort()
# #The sort() method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).
# Syntax list.sort(reverse=True|False, key=myFunc)
# Parameter	Description
# reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
# key	Optional. A function to specify the sorting criteria(s)
n1=[1,2,3,4,5,6,7,8,9]
n1.sort()
print(n1)
aa = ["Math","History","Geometry","Geography","Science"]
aa.sort(reverse=True)
print(aa)

#reverse()
#this method is used to reverse the list 
lx=[1,2,3,4]
ly=['a', 'b', 'c', 'd', 'e', 'f']
lx.reverse()
print(lx)
ly.reverse()
print(ly)
