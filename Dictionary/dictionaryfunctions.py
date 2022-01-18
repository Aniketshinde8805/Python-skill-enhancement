d1={"i":"hhhh","j":"kdjdkjf","g":"sjdk"}
d2={11:"eleven",22:"twenty two",33:"thirty three",44:"thirty four",55:"thirty five"}

#len()
print(len(d1))
print(len(d2))


# #str()
# Python dictionary method str() produces a printable string representation of a dictionary.
# Syntax str(dict)
# Return Value  This method returns string representation.

aa=str(d1)
print(aa)
print(str(d2))

 #dict.clear()
#clear(dict)
#this method is used to empty  the dictionary ie remove all the elemnts form the dictionary
d2.clear()
print(d2)


d1={"i":"hhhh","j":"kdjdkjf","g":"sjdk"}
d2={11:"eleven",22:"twenty two",33:"thirty three",44:"thirty four",55:"thirty five"}


# dict.items()
# it returns each key value pair in a list of tuples
print(d1.items())
print(d2.items())

# dict.copy()	
#Python dictionary method copy() returns a shallow copy of the dictionary.
aa=d1.copy()
bb=d2.copy()
print(aa)
print(bb)

# dict.keys()
# it returns list of keys in the dictionary
print(d1.keys())
print(d2.keys())


# dict.fromkeys(seq[, value])	
# Python dictionary method fromkeys() creates a new dictionary with keys from seq and values set to value.
# Syntax dict.fromkeys(seq[, value])
# Parameters
# seq − This is the list of values which would be used for dictionary keys preparation.
# value − This is optional, if provided then value would be set to this value
# Return Value   This method returns the list.
ll=[1,2,3,4]
tt=(1,2,3,4)
ss={1,2,3,4}
print(d1.fromkeys(ll,"list"))  #list
print(d2.fromkeys(tt,10))     #tuple
print(d2.fromkeys(ss,"set"))  #set
print(d1.fromkeys(ll))  # it no value is passed the it has None as value

# dict.values()
#it returns a list of values of the list
print(d1.values())
print(d2.values())

# dict.get(key, default=None)	
#The get() method returns the value of the item with the specified key.
#Syntax dictionary.get(keyname, value)
# Parameter	    Description
# keyname	        Required. The keyname of the item you want to return the value from
# value	        Optional. A value to return if the specified key does not exist.
print(d1.get('i'))
print(d1.get('j'))
print(d2.get(11))
print(d2.get(22))


# dict.update(dict2)(d = s , same; else update)


# # dict.has_key(key)		
# The get() method returns the value of the item with the specified key.
# Syntax  dictionary.get(keyname, value)
# Parameter	    Description
# keyname	        Required. The keyname of the item you want to return the value from
# value	        Optional. A value to return if the specified key does not exist.
# print(d1.has_key('i'))
# print(d1.has_key('j'))
# print(d2.has_key(11))
# print(d2.has_key(22))


# dict.setdefault(key, default=None)
# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value, see example below
# Syntax dictionary.setdefault(keyname, value)
# Parameter 	Description
# keyname	    Required. The keyname of the item you want to return the value from
# value	        Optional.
# If the key exist, this parameter has no effect.
# If the key does not exist, this value becomes the key's value
print(d1)
print(d1.setdefault('i'))
print(d1.setdefault('j'))
print(d1.setdefault('aa',1111))
print(d1)

print(d2)
print(d2.setdefault(11))
print(d2.setdefault(22))
print(d2.setdefault(99,9999))
print(d2)

