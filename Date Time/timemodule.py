import time
import datetime

#time.time()
# The method time() returns the time as a floating point number expressed in seconds since the epoch, in UTC.
# Note − Even though the time is always returned as a floating point number, not all systems provide time with a better precision than 1 second. 
# While this function normally returns non-decreasing values, it can return a lower value than a previous call if the system clock has been set back between the two calls.
# Syntax time.time()
# Return Value This method returns the time as a floating point number expressed in seconds since the epoch, in UTC.
print(time.time() )



#time.localtime()
#this method of Time module is used to convert a time expressed in seconds since the epoch to a time.struct_time object in local time. 
#time.localtime() method of Time module is used to convert a time expressed in seconds since the epoch to a time.struct_time object in local time. 

print(time.localtime(time.time()))


#asctime()
# method asctime() converts a tuple or struct_time representing a time as returned by gmtime() or localtime() to a 24-character string of the following form: 'Tue Feb 17 23:21:05 2009'.
# Syntax  time.asctime([t]))
# Parameters
# t − This is a tuple of 9 elements or struct_time representing a time as returned by gmtime() or localtime() function.
# Return Value
# This method returns 24-character string of the following form: 'Tue Feb 17 23:21:05 2009'.
print(time.asctime())

#time.clock()
print(time.clock())

#time.sleep(sec)
# The method sleep() suspends execution for the given number of seconds. The argument may be a floating point number to indicate a more precise sleep time.
# The actual suspension time may be less than that requested because any caught signal will terminate the sleep() following execution of that signal's catching routine.
# Syntax  time.sleep(t)
# Parameters
# t − This is the number of seconds execution to be suspended.
# Return Value  This method does not return any value.
print ("Start : %s" % time.ctime())
time.sleep( 5 )
print ("End : %s" % time.ctime())


#time.gmtime()
# The method gmtime() converts a time expressed in seconds since the epoch to a struct_time in UTC in which the dst flag is always zero.
#  If secs is not provided or None, the current time as returned by time() is used.
# Syntax  time.gmtime([ sec ])
# Parameters
# sec − These are the number of seconds to be converted into structure struct_time representation.
# Return Value
# This method does not return any value.
print ("gmtime :", time.gmtime(1455508609.34375))


#mktime()
mytuple=(2022,9,9,16,45,30,0,0,0)
print(time.mktime(mytuple))
print(time.localtime(time.mktime(mytuple)))
print(time.asctime(mytuple))


#time.strptime(str,fmt='%a %b %d %H:%M:%S %Y') 
#convert str datetime to 9 tuple
str1=time.asctime(mytuple)
print(time.strptime(str1))

# #time.strftime(fmt[,tupletime])
# Pythom time method strftime() converts a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument.
# If t is not provided, the current time as returned by localtime() is used. format must be a string. An exception ValueError is raised if any field in t is outside of the allowed range.
# Syntax  time.strftime(format[, t])
# Parameters
# t − This is the time in number of seconds to be formatted.
# format − This is the directive which would be used to format given time. The following directives can be embedded in the format string −

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print (time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))
print(time.strftime('%a %b, %Y', time.localtime()))

	# time.tzset()
# time.altzone
print(time.altzone)



