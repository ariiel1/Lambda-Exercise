import datetime
time = datetime.datetime.now()
year = lambda x:x.year
month = lambda x:x.month
date = lambda x:x.day
print("Year: ",year(time))
print("Month: ",month(time))
print("Date: ",date(time))