# Module is a file consisting of Python code
# A module can define functions, classes and variables
#  The import Statement
import calendar,time,datetime

from mymodule import fun1,fun2
fun1()
fun2()


import mymodule
mymodule.fun1()
mymodule.fun2()


#  The from...import * Statement


# ▪ Locating Modules
# 	When you import a module, the Python interpreter searches for the module in 	the following sequences
# 		1. The current directory
# 		2. If the module isn't found, Python then searches
# 		    each directory in the shell variable PYTHONPATH.
# 		3. If all else fails, Python checks the default path.
# 		    default path is normally /usr/local/lib/python/

# ▪ The PYTHONPATH Variable
# 	set PYTHONPATH=/usr/local/lib/python

# ▪ The dir( ) 
# The dir() function returns all properties and methods of the specified object, without the values.
# This function will return all the properties and methods, even built-in properties which are default for all object.
# Syntax  dir(object)
# Parameter	Description
# object	    The object you want to see the valid attributes of
print(dir(1))
print(dir(mymodule))
l1=[1,2,3]
print(dir(l1))

# ▪ The reload() Function
# 	reload(module_name)
# 	When the module is imported into a script, the code in the top-level portion of a
# module is executed only once. if you want to re-execute the top-level code in a module, you can use the reload() function
# reload(time)


# ▪ Packages in Python
# 	A package is a hierarchical file directory structure that defines a single Python application environment that consists of modules and sub packages

