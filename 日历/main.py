import calendar
import time
print(calendar.month(time.localtime().tm_year,time.localtime().tm_mon))
i=1
while(i<=12):
    print(calendar.month(time.localtime().tm_year, i))
    i+=1