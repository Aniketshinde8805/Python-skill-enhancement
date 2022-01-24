#meta characters
#[]^.$+*?{}()\/

# ^----------matches the beginning
# $----------matches the end
# []---------sequence of characters
# ()---------encloses group of regular expressions
# +----------one or more occurrences
# ?----------zero or one occurrence
# |----------or
# {}---------indicate the no of occurences
# *----------any no of occurrences including 0
# \----------drops the special meaning of characters
# \d--------- matches any decimal digit
# \D---------matches any non-digit character
# \s---------matches any whitespace
# \S---------matches any non-whitespace character
# \w---------matches any alphanumeric character
# \W---------matches any non-alphanumeric character
# '\A'-------Returns a match if the specified characters are at the beginning of the string
# '\b'-------Returns a match where the specified characters are at the beginning or at the end of a word



# re.findall(pattern, string, flags=0)
# In this syntax:
# pattern is a regular expression that you want to match.
# string is the input string
# flags is one or more regular expression flags that modify the standard behavior of the pattern.

# The findall() function scans the string from left to right and finds all the matches of the pattern in the string.
# The result of the findall() function depends on the pattern:
# If the pattern has no capturing groups, the findall() function returns a list of strings that match the whole pattern.
# If the pattern has one capturing group, the findall() function returns a list of strings that match the group.
# If the pattern has multiple capturing groups, the findall() function returns the tuples of strings that match the groups.

import re

pattern='[abc]'
s="hi abc how are you."
print(re.findall(pattern, s))
# output =  ['a', 'b', 'c', 'a']

pattern2='[a-c]'  #here a-c means all characters form a to c
print(re.findall(pattern2, s))
# output =  ['a', 'b', 'c', 'a']

print(re.findall('(abc)',"abc abc"),type(re.findall('(abc)',"abc abc")))
# output = ['abc', 'abc'] <class 'list'>


# \d--------- matches any decimal digit
p1='\d'
s="good evening 123 hi 890"
print(re.findall(p1,s))
# output =  ['1', '2', '3', '8', '9', '0']

s2="everyone wake up at 7 am on 3rd Jan 2022"
print(re.findall(p1,s2))
# output =  ['7', '3', '2', '0', '2', '2']



# ^----------matches the beginning
p1='^s'
s1='Say hello'  # here it returns empty list  because of different case as it is case sensitive
print(re.findall(p1,s1))
# output =  []

s2='say hello'
print(re.findall(p1,s2))
#output = ['s']

p2='^the'
s3='the world is awesome'
print(re.findall(p2,s3))
# output = ['the']


p3='[xy]'
s4="x abc yz df xyz"
print(re.findall(p3,s4))
# output =  ['x', 'y', 'x', 'y']

p3='[^xy]'   # when you use  ^ in [] then it acts like a complement
s4="x abc yz df xyz"
print(re.findall(p3,s4))
# output =  [' ', 'a', 'b', 'c', ' ', 'z', ' ', 'd', 'f', ' ', 'z']

p4='^xy'
s="xyz"
print(re.findall(p4,s))
#output=  ['xy']

p4='^xy'
s="xzy"
print(re.findall(p4,s))
# output = []


# $----------matches the end
p='x$'
s='asdx'
print(re.findall(p,s))
# output =  ['x']

p='x$'
s='asdp'
print(re.findall(p,s))
# output = []


# +----------one or more occurrences
p1='\d+'
s="abc 345 7 x yu t"
print(re.findall(p1,s))
#output = ['345', '7']

p1='\d'
s="abc 345 7 x yu t"
print(re.findall(p1,s))
#output = ['3', '4', '5', '7']





# *----------any no of occurrences including 0
p='pi*n'
s='pin'
print(re.findall(p,s))
#output = ['pin']

p='pi*n'
s='pan'
print(re.findall(p,s))
# output = []

p='pi*n'
s='piiiiiin'
print(re.findall(p,s))
# output =  ['piiiiiin']

p='pi*n'
s='piiiiii'
print(re.findall(p,s))
# output =  []


p='pi+n'
s='pin'
print(re.findall(p,s))
# output = ['pin']

p='pi+n'
s='piiiiiin'
print(re.findall(p,s))
# output =  ['piiiiiin']


# ?----------zero or one occurrence
p='pi?n'
s='pin'
print(re.findall(p,s))
# output = ['pin']

p='pi?n'
s='pn'
print(re.findall(p,s))
# output = ['pn']


p='pi?n'
s='piiiiin'
print(re.findall(p,s))
# output =  []


# {}---------indicate the no of occurences
p='s{2,4}'   #here first no is the minimum and second no is maximum no of occurences to find
s='ss assd sa ssssd sssss'
print(re.findall(p,s))
# output =  ['ss', 'ss', 'ssss', 'ssss']

p='\d0{3,5}'
s='1000 iiii 100000 010000000'
print(re.findall(p,s))
#output = 

p='0{3,5}'
s='1000 hiiiii 100000 010000000'
print(re.findall(p,s))
# output =  ['000', '00000']


# |----------or
p='x|y'
s='xabcy'
print(re.findall(p,s))
# output = ['x', 'y']

p='(x|y)ab'  
s="hi hello xab xyab xy yab"
print(re.findall(p,s))
# output =  ['x', 'y', 'y']



# \----------drops the special meaning of characters
p='\^a'  #here the meaning of ^ is taken off and it is considered as normal character
s="^abc b ^a"
print(re.findall(p,s))
# output = ['^a', '^a']

p='a\$'
s="^abc b a$"
print(re.findall(p,s))
# output =  ['a$']


p='\^a\$'  #we have to use \ for each meta character 
s="^abc b ^a$"
print(re.findall(p,s))
#output = ['^a$']


#'\A'---------Returns a match if the specified characters are at the beginning of the string
p='\Ahi'
s="hello hi all"
print(re.findall(p,s))
#output = []

p='\Ahi'
s="hi hello all"
print(re.findall(p,s))
# output =  ['hi']


# '\b'-------Returns a match where the specified characters are at the beginning or at the end of a word
p=r'\bhi'   #(the "r" in the beginning is making sure that the string is being treated as a "raw string")
s='hi thi'
print(re.findall(p,s))
# output =  ['hi']

#for word ending with
p=r'\bis'
s=" is simple"
print(re.findall(p,s))
# output =  ['is']


# \s---------matches any whitespace
# p='\s'
# s=input("enter a string ")
# m=re.findall(p,s)
# if m:
#     print("white space")
# else:
#     print("no white space")



# #re.search()
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
#If no matches are found, the value None is returned:
txt = "The rain in Spain"
x = re.search("\s", txt)
print(x.start())


txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


#re.split()
#The split() function returns a list where the string has been split at each match:
#You can control the number of occurrences by specifying the maxsplit parameter:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


#The sub() function replaces the matches with the text of your choice:
#You can control the number of replacements by specifying the count parameter:
txt = "The rain in Spain"
x = re.sub("\s", "#", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "#", txt, 2)
print(x)


#match object
#A Match Object is an object containing information about the search and the result.

# The Match object has properties and methods used to retrieve information about the search, and the result:
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


#re.match()
#it searches for a match at the start of the string
#If zero or more characters at the beginning of string match this regular expression, return a corresponding match object.

txt="dogs are my favorite pets"
print(re.match('dogs',txt))
#output =  <_sre.SRE_Match object; span=(0, 4), match='dogs'>

txt="dogs are my favorite pets"
print(re.match('pets$',txt))
#output= None
print(re.findall('pets$',txt))
#output = ['pets']