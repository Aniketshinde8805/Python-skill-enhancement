import random

# random.choice(sequence)
# it returns a random element from a sequence
l1=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(l1))


#random.shuffle(sequence) 
# method is used to shuffle a sequence (list). 
# Shuffling means changing the position of the elements of the sequence. 
l2=[10,20,30,40,50,60,70,80,90,100]
random.shuffle(l2)
print(l2)
random.shuffle(l2)
print(l2)
random.shuffle(l2)
print(l2)


#random.seed(value)
for i in range(5):
    random.seed(0)
    print(random.randint(1,1000))


# random.radians(start,end,setout)
# it generates random values in given range 
# setout is the value which we want to omate form the range

print(random.randrange(1,100,44))
print(random.randrange(11,40,4))
print(random.randrange(80,100,67))


#random.randint(start,end)
#A random integer in range [start, end] including the end points.
print(random.randint(1,2))
print(random.randint(1,2))
print(random.randint(30,35))


# random.random() function generate random floating numbers between 0 and 1.
# Syntax : random.random()
# Parameters : This method does not accept any parameter.
# Returns : This method returns a random floating number between 0 and 1.
print (random.random())
print (random.random())
print (random.random())


# Syntax : uniform(int x, int y)
# Parameters :
# x Specifies the lower limit of the random number required to generate.
# y Specifies the upper limit of the random number required to generate.
# Returns : Returns the generated floating point random number between lower limit and upper limit
print(random.uniform(10,20))