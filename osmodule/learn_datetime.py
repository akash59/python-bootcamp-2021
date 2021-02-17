from datetime import date
from datetime import datetime
from datetime import time

# if only time is needed
my_time = time(2, 20)
print(my_time)

print(my_time.minute)

print(my_time.hour)

print(type(my_time))

# if only date is needed
today = date.today()
print(today)

print(today.year, today.month, today.day)

print(today.ctime())

# if both date and time is needed
my_date_time = datetime(2021, 10, 3, 14, 20, 1)
print(my_date_time)

my_date_time = my_date_time.replace(year=2020)
print(my_date_time)

date1 = date(2021, 11, 3)
date2 = date(2020, 11, 3)
result = date1 - date2
print(result.days)
print(type(result))

datetime1 = datetime(2021, 11, 3, 22, 0)
datetime2 = datetime(2020, 11, 3, 12, 0)
result = datetime1 - datetime2
print(result)
print(type(result))
print(result.seconds)
print(result.total_seconds())
