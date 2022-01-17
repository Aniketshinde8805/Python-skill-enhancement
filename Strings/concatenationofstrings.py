# concatenation of strings with different methods

# concatenating string variables with strings
fname=input("enter First Name")
lname=input("Enter Last Name")
print("Welcome" + " " + fname + " " + lname + " to my website")


# concatenating Number variables with strings
str1=" Your roll no is " 
roll=4546566
print(str1 + str(roll)) # you have to convert roll  to srt type


# Concatenate strings with "%" operator
name="Atul"
age=7
year=2001
print('%s is %i years old as he was born in year %i' % (name,age,year))


# concatenating string Using .format() without index 
# here the variable values will be replaced with {} in given order
print("{} is {} years old as he was born in year {}".format(name,age,year))


# concatenating string  Using .format() with index
print("{0} is {1} years old as he was born in year {2}".format(name,age,year))


#Concatenating strings using Python f-strings
# F-strings, also called "formatted string literals", are string literals with a leading "f" and curly braces in the string pattern that will be replaced with the values of the variables. Internally, f-strings are Python expressions that will be evaluated at runtime, not a constant value.
# F-strings are less verbose, more readable, and less error-prone when refactoring your code than other ways to concatenate strings. Whenever possible, prefer f-strings to any concatenation method.
print(f"{name} is {age} years old as he was born in year {year}")