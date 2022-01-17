s1="ecolibriumenergy"
s2="abcde"
# capitalize() 
# it capitalize the first letter of the string
print(s1.capitalize())

#isalpha() 
#it returns true if the string contains only alphabests and it has atleast one character
s3="anike1334"
print(s3.isalpha()) 
s4=""
print(s4.isalpha())   
s5="aniket"
print(s5.isalpha()) 


#isalnum()
# it returns true if the string contains alphanumeric characters  or characters only or numbers only
#  and is has atleast one character
print(s5.isalnum())  # hers s5 has only characters
print(s3.isalnum())  # here s3 has char and numbers
print(s4.isalnum())  # hers s4 is empty


#title()
# it makes the first letter in each word of string capital
ss="this is my string"
print(ss.title())

sa="anii d kd d d d d d"
print(sa.title())


#isdigit()
# this method returns True if the string contains only digits and atleast one caharacter
sn="3984894894"
ss="thsif9994"
sv="2²"
sf="½"
print(ss.isdigit())
print(sn.isdigit())
print(sv.isdigit())  # isdigit() returns True for exponents
print(sf.isdigit())  # isdigit() returns False for fractions



# isnumeric()
#isnumeric method checks if the character is a unicode representation of a numeric value.
# it returns True for integer , exponents and fractions values
sa="2.3" 
si="54656"
sv="2²"
sd="94559"
sf="½"
print(sa.isnumeric())   # here it will be false because floating points are not considered numeric in str 
print(sv.isnumeric())
print(sd.isnumeric())
print(si.isnumeric())
print(sf.isnumeric())  


# isdecimal()
#The isdecimal() method returns True if all the characters are decimals (0-9).
#This method is used on unicode objects.
aa="56768"
print(aa.isdecimal())
bb="89.99"
print(bb.isdecimal())
ss="\u0033" #unicode for 3
print(ss.isdecimal())
sv="2²"
sd="94559"
sf="½"
print(sv.isdecimal())
print(sd.isdecimal())
print(sf.isdecimal())


#isspace()
#method is used to check space in the string. It returna true if there are only whitespace characters in the string.
s1="    "
s2=""
s3="df"
s4="df  DF"
print(s1.isspace()) #true
print(s2.isspace()) # false
print(s3.isspace()) #false
print(s4.isspace()) #false


#istitle()
# istitle() method returns true if the string in title format ie each word has first letter a capital letter
aa="this is my string1"
sf="This Is My String2"
print(aa.istitle())
print(sf.istitle()) 


#islower()
# it returns true if all characters in the string are lowercase
aa="this is my string"
ad="thi is my String"
dd="dfddfA"
print(aa.islower())
print(ad.islower())
print(dd.islower())


#isupper()
# it returns true if all characters in the string are in upper case
aa="THIS IS MY STRING 334"
df="THIS IS MY strng3"
print(aa.isupper())
print(df.isupper())


#The join() method takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.
# Syntax string.join(iterable)
# here string vaue is put in between each list object in the string.
l1=["45645","45655","7877","fgh","fhfgh"]  # all list element must be of type str
aa=" ".join(l1)
print(aa)
l2=["this","is","my","string"]
bb="#".join(l2)
print(bb)

#len(string)
# this method gives the count of characters in the string including the space
s1="Tom Mandy"
print(len(s1))
s2="    "
print(len(s2))
s3="the the the"
print(len(s3))


#lstrip()
# this method is used to removes leading whitespace from the string
aa="  thank you"
print(aa.lstrip())
bb="    thank for the      "
print(bb.lstrip())


#rstrip()
# this method is used to removes trailing whitespace from the string
s2="Thankyou           "
s3="Tom            "
print("%s %s" % (s2,s3))
print("%s %s" % (s2.rstrip(), s3.rstrip()))

#strip()
# it removes leading and trailing whitespace from the string
s2="              Thankyou   very much     "
s3="        Tom            "
print(s2.strip())
print(s3.strip())
print("%s %s" % (s2,s3))
print("%s %s" % (s2.strip(), s3.strip()))


#max(string)
#Python string method max() returns the max alphabetical character from the string str.
s1="string1"
print(max(s1))
s2="zebra is  zerbra"
print(max(s2))


#min(string)
#Python string method min() returns the min alphabetical character from the string str.
s1="string1"
print(min(s1))   # here 1 is the smallest character in the string
s2="zebra is  zerbra"  # here whitespace is the smallest character in the string
print(min(s2))


#maketrans()
#Python string method maketrans() returns a translation table that maps each character in the intabstring into the character at the same position in the outtab string.
#  Then this table is passed to the translate() function.
# Note − Both intab and outtab must have the same length.
# Syntax  str.maketrans(intab, outtab)

s1="The quick brown fox jumps over the lazy dog"
trans1= s1.maketrans("aeiou","vwxyz")
print(trans1)   # type dictionary

s2="Pack my box with five dozen liquor jugs"
trans2=s2.maketrans("abcde","pqrst")
print(trans2)   # of type dictionary

#translate()
#The translate() method returns a copy of the string in which all characters have been translated using table (constructed with the maketrans() function in the string module), optionally deleting all characters found in the string deletechars.
# Syntax
# str.translate(table[, deletechars]);
# Parameters
# table − You can use the maketrans() helper function in the string module to create a translation table.
# Return Value
# This method returns a translated copy of the string.

str1=s1.translate(trans1)
print(str1)
str2=s2.translate(trans2)
print(str2)


#zfill()
# The zfill() method pads string on the left with zeros to fill width.
# Syntax str.zfill(width)
# Parameters:-width − This is final width of the string. This is the width which we would get after filling zeros.
# Return Value:- This method returns padded string.

s1="Happy Birthday"
print(s1.zfill(40))
s2="Good Morning"
print(s2.zfill(40))


#The expandtabs() method sets the tab size to the specified number of whitespaces.

# Syntax:string.expandtabs(tabsize)
# Parameter = tabsize
# Description=Optional. A number specifying the tabsize. Default tabsize is 8

ss = "H\te\tl\tl\to"

print(ss)
print(ss.expandtabs())
print(ss.expandtabs(2))
print(ss.expandtabs(4))
print(ss.expandtabs(10))


#count()
# The count() method returns the number of occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

# Syntax
# str.count(sub, start = 0,end = len(string))
# Parameters
# sub − This is the substring to be searched.
# start − Search starts from this index. First character starts from 0 index. By default search starts from 0 index.
# end − Search ends from this index. First character starts from 0 index. By default search ends at the last index.
# Return Value
# Centered in a string of length width.

str = "this is string example....wow!!!"
sub = 'i'
print ("str.count('i') : ", str.count(sub))
sub = 'exam'
print ("str.count('exam', 10, 40) : ", str.count(sub,10,40))


#codecs.decode()
# With the help of codecs.decode() method, we can decode the binary string into normal form by using codecs.decode() method.

# Syntax : codecs.decode(b_string)

# Return : Return the decoded string.
# s1 = "this is string example....wow!!!";
# s1 = codecs.encode('base64');

# print ("Encoded String: " + s1)
# print ("Decoded String: " + s1.codecs.decode('base64','strict'))


#startswith()
# Python string method startswith() checks whether string starts with str, optionally restricting the matching with the given indices start and end.
# Syntax
# Following is the syntax for startswith() method −
# str.startswith(str, beg=0,end=len(string));
# Parameters
# str − This is the string to be checked.
# beg − This is the optional parameter to set start index of the matching boundary.
# end − This is the optional parameter to end start index of the matching boundary.
# Return Value
# This method returns true if found matching string otherwise false.
s1="this is my string"
print(s1.startswith("this",0,10))
print(s1.startswith("is",5,10))
print(s1.startswith("this",5,10))


#endswith()
# The endswith() method returns True if the string ends with the specified value, otherwise False.
# Syntax
# string.endswith(value, start, end)
# Parameter Values
# Parameter	Description
# value	Required. The value to check if the string ends with
# start	Optional. An Integer specifying at which position to start the search
# end	Optional. An Integer specifying at which position to end the search
ss = "Hello, welcome to my world."
print(ss.endswith("my world."))
print(ss.endswith("hello"))


#find()
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
# Syntax
# string.find(value, start, end)
# Parameter Values
# Parameter	Description
# value	Required. The value to search for
# start	Optional. Where to start the search. Default is 0
# end	Optional. Where to end the search. Default is to the end of the string
sf="today is a very good day to go on a vacation"
print(sf.find("is"))
print(sf.find("a",4))
print(sf.find("is",9,12))
print(sf.find("is",7,12))


#rfind()
#The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
# The rfind() method is almost the same as the rindex() method. See example below.
# Sy
# string.rfind(value, start, end)
# Parameter Values
# Parameter	Description
# value	Required. The value to search for
# start	Optional. Where to start the search. Default is 0
# end	Optional. Where to end the search. Default is to the end of the string
txt = "Hello, welcome to my world."
print(txt.rfind("e"))
print(txt.rfind("e",5,10))


#index()
# Python list method index() returns the lowest index in list that obj appears.
# Syntax
# Following is the syntax for index() method −
# list.index(obj)
# Parameters
# obj − This is the object to be find out.
# Return Value
# This method returns index of the found object otherwise raise an exception indicating that value does not find.
aList = [123, 'xyz', 'zara', 'abc']
print ("Index for xyz : ", aList.index( 'xyz' )) 
print ("Index for zara : ", aList.index( 'zara' ) )


#rindex()
# Python string method rindex() returns the last index where the substring str is found, or raises an exception if no such index exists, optionally restricting the search to string[beg:end].
# Syntax
# Following is the syntax for rindex() method −
# str.rindex(str, beg=0 end=len(string))
# Parameters
# str − This specifies the string to be searched.
# beg − This is the starting index, by default its 0
# len − This is ending index, by default its equal to the length of the string.
# Return Value
# This method returns last index if found otherwise raises an exception if str is not found.
str1 = "this is string example....wow!!!"
str2 = "is"
print (str1.rindex(str2))
print (str1.index(str2))


#replace()
# The replace() method replaces a specified phrase with another specified phrase.
# Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.
# Syntax
# string.replace(oldvalue, newvalue, count)
# Parameter Values
# Parameter	Description
# oldvalue	Required. The string to search for
# newvalue	Required. The string to replace the old value with
# count	Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences
txt = "one one was a race horse, two two was one too."
print( txt.replace("one", "three"))
txt = "one one was a race horse, two two was one too."
print(txt.replace("one", "three", 2))


#split()
# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
# Note: When maxsplit is specified, the list will contain the specified number of elements plus one.
# Syntax
# string.split(separator, maxsplit)
# Parameter Values
# Parameter	Description
# separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
# maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"
s1 = "hello, my name is Peter, I am 26 years old"
x = s1.split(", ")
print(x)
s2 = "apple#banana#cherry#orange"
x = s2.split("#")
print(x)
s3="this is my string"
x=s3.split()
print(x)


#splitlines()
# Python String splitlines() method is used to split the lines at line boundaries. 
# The function returns a list of lines in the string, including the line break(optional).
# Syntax: string.splitlines([keepends])
# Parameters:keepends (optional): When set to True line breaks are included in the resulting list. 
# This can be a number, specifying the position of line break or, can be any Unicode characters, like “\n”, “\r”, “\r\n”, etc as boundaries for strings.
#The splitlines() method splits a string into a list. The splitting is done at line breaks.

# Representation  Description

# \n	            Line Feed
# \r	            Carriage Return
# \r\n	        Carriage Return + Line Feed
# \x1c	        File Separator
# \x1d	        Group Separator
# \x1e        	Record Separator
# \x85        	Next Line (C1 Control Code)
# \v or \x0b  	Line Tabulation
# \f or \x0c  	Form Feed
# \u2028	    Line Separator
# \u2029	    Paragraph Separator

s1="hello\n welcome to \n my website"
x=s1.splitlines()
print(x)


# #replace()
# The replace() method replaces a specified phrase with another specified phrase.
# Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.
# Syntax
# string.replace(oldvalue, newvalue, count)
# Parameter Values
# Parameter	Description
# oldvalue	Required. The string to search for
# newvalue	Required. The string to replace the old value with
# count	Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences

s1="Today is the day. A day of the month, a day of the week, the best day"
print(s1.replace("day","bestday"))
print(s1.replace("day","Sunday",3))


#swapcase()
# swapcase() Function in python swaps the case of the every single character of the string from upper case to lower case and from lower case to upper case.
# If the input string is in small case it swaps the result to upper case.
# If the input string is in upper case it swaps the result to small case.
# If input string is in mix of small case and upper case then it swaps all the upper case character to small case and all the small case character to upper case.
# Syntax: str.swapcase();
s1="tooidf ddfdfdfdf"
s2="JDFLJFJ  DFOIDO  IDF DO F"
s3="kdfERT DFGfgdFGFG dfgfDF"
print(s1.swapcase())
print(s2.swapcase())
print(s3.swapcase())


#center()
# The center() method will center align the string, using a specified character (space is default) as the fill character.
# Syntax string.center(length, character)

# Parameter	    Description
# length      	Required. The length of the returned string
# character   	Optional. The character to fill the missing space on each side. Default is " " (space)
s1="this is one string"
s2="this is another string to be centered"
print(s1.center(100,"-"))
print(s2.center(100,"-"))



# #ljust()
# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
# Syntax  string.ljust(length, character)
# Parameter	    Description
# length      	Required. The length of the returned string
# character	    Optional. A character to fill the missing space (to the right of the string). Default is " " (space).
s1="this is one string"
s2="this is another string to be ljusted"
print(s1.ljust(100,"-"))
print(s2.ljust(100,"-"))


# #rjust()
# The rjust() method will right align the string, using a specified character (space is default) as the fill character.
# Syntax string.rjust(length, character)
# Parameter	Description
# length	Required. The length of the returned string
# character	Optional. A character to fill the missing space (to the left of the string). Default is " " (space).
s1="this is one string"
s2="this is another string to be rjusted"
print(s1.rjust(100,"-"))
print(s2.rjust(100,"-"))