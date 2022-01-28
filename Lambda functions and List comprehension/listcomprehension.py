from ast import Expression


l1=[x**2 for x in range(1,11)]
print(l1)

l2=[(x,x**2) for x in range(1,11)]
print(l2)


#list comprehension with if clause
# Python List Comprehension If Clause Syntax :[expression for var in iterable if clause]
l3=[x for x in range(1,11) if x%2==0]
print(l3)
l4=[x for x in range(1,11) if x%2==1]
print(l4)


#nested list comprehension
# With list comprehension
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# L = [number for list in vector for number in list]
L=[number for l in vector for number in l]


print(L)
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

# equivalent to the following plain, old nested loop:
# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# L = []
# for list in vector:
#     for number in list:
#         L.append(number)
# print(L)
# Prints [1, 2, 3, 4, 5, 6, 7, 8, 9]