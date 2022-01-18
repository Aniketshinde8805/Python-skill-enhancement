#dictionary
#ways of declaration of Dictionary
d1={"h":34,"i":"dfkj","j":456,"k":"ani"}
print(d1)

#accesin elements of a dictionary
print(d1["h"])
print(d1["i"])
print(d1["j"])
print(d1["k"])

#accesing element with a key which is not in the dictionary then it gives error
# print(d1["z"])

#updating a dictionary 
d2={"hello":'hello',344:344,"i":456,67:"world","l1":[1,2,3,4,5,6,7,8,9],"t1":(1,2,3,4,5),"s1":{1,5,7,9,45}}
print(d2)
d2["s1"]={1,44,66,77}
print(d2)
d2["dd"]={"q":"q"}  # here we added a new key value pair
print(d2)

#deleting specific dictionary elements from a dictionary
del(d2["i"])
print(d2)

#clear(dict)
#this method is used to empty  the dictionary ie remove all the elemnts form the dictionary
d2.clear()
print(d2)

#del()
#del() method is used to delete objects
del(d2) #here we are deleting dictionary d2


#properties of key in a dictionary
# every key in a dictionary must be unique
#key must be of immutable ie  string, number and tuple data types can be used as key
# a dictionary cannot contain duplicate keys
# if you give duplicate key then the dictionary will store the latest entered key value pair
dc={"h":"hi","i":"hello","j":456,"h":"welcome","k":45,"l":23,"h":999} 
#here we have entered "h" key 3 times ,so then it will take the last entered key value pair ie "h":999
print(dc)


#key must be of immutable ie  string, number and tuple data types can be used as key

# dk={[1,2,3]:"list"}  #here it gives error because list is mutable
# ds={{1,2,3}:"set"}   # set are also mutable so it gives error
#da={dc:"dictionary"}   #dictionary is mutable so it gives error
dt={(1,2,3):"tuple"}   #tuple is immutable so it tuple as key and we have no error
