import datetime
import calendar
month, day, year = map( int, input().split())
print((calendar.day_name[datetime.datetime(month=month, day=day, year=year).weekday()]).upper())