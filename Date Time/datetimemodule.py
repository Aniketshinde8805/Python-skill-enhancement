import datetime
import time
print(datetime.MINYEAR)
print(datetime.MAXYEAR)

#datetime.date(year,month,hour)
#To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
#The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
x=datetime.datetime(2020,2,19)
print(x)
y=datetime.datetime(2023,5,12)
print(y)

# print(datetime.time())
aa=datetime.date(2023,5,12)
print(aa)


tday=datetime.date.today()  #today's date 
print(tday)
print(tday.weekday())   #display which day is today  #here Monday is 0  and Sunday is 6
print(tday.isoweekday()) #display which day is       #here Monday is 1 and  Sunday is 7


tdelta=datetime.timedelta(days=7)
print(tday +tdelta)   #prints date 7 days from tday
print(tday -tdelta) #prints   date 7 previous from tday


#calculating how many days remaining for my birthday
bday=datetime.date(2022,9,9)
till_bday = bday-tday
print(till_bday.days)  # days remaining for  bday
print(till_bday.total_seconds()) # seconds remaining for bday





#datetime.time

t=datetime.time(9,20,45,111110)
print(t.hour)
dt=datetime.datetime(2022,2,19,20,45,13,100000)
print(dt.year)

#print date form 7 days form dt 
tdelta=datetime.timedelta(days=7)  #t
print(dt +tdelta)

#printing date from 10 hours from dt
tdeltah=datetime.timedelta(hours=12)
print(dt+tdeltah)

print("____________________________________________________")
dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
date_utcnow=datetime.datetime.utcnow()
print(dt_today )
print(dt_now )
print(date_utcnow)

print("---------------------------------------------")

tdelta=datetime.timedelta(days=100)
print(tdelta.min)
print(tdelta.max)

print("date objects---------------------------------------------")
dati=datetime.datetime(2005, 7, 14, 12, 30)
print(datetime.date.today())
print(datetime.date.min)
print(datetime.date.max)
print(dati.year)
print(dati.month)
print(dati.day)

dt=datetime.date.today()
print(datetime.date.timetuple(dt))
print(datetime.date.isoformat(dt))		#Return a string date in format, ‘YYYY-MM-DD’
print(datetime.date.strftime(dt,"%d/%m/%y"))		#d.strftime("%d/%m/%y")
print(datetime.date.weekday(dt))		#0-6
print(datetime.date.isoweekday(dt))	#	1-7
print(datetime.date.ctime(dt))



print("time objects-------------------------------------------------------")
 #return datetime.time([hour[,minute[, second[, microsecond[, tzinfo]]]]])
dt=datetime.time(9,20,45,111110)
print(dt)
print(dt.min)
print(dt.max)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

print(dt.isoformat())
        #Return a string time in format HH:MM:SS.mmmmmm
print(dt.strftime("%H:%M:%S"))


print("date time objects--------------------------------------------")
ttt=datetime.time(12,45,30,100000)
ddd=datetime.date(2020,2,19)
dt=datetime.datetime(2020,2,19,12,30,20,100000)
print("time=",ttt)
print("date=",ddd)
print(datetime.date.today())
print(ttt)
# print(datetime.now())
print(dt.utcnow())
# print(datetime.combine(ddd, ttt))
# print(datetime.strptime(date_string,format))
print(ddd.weekday())
print(ddd.isoweekday())
print(ttt.isoformat())
print(ttt.strftime("%H:%M:%S"))
print(dt.ctime())