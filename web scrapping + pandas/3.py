import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(1998,6,13)
print(birthday)

date_since_birth = (today-birthday).days
print(date_since_birth)

tdelta = datetime.timedelta(days=10)
print(today+tdelta)

print(today.weekday()) #0 - Monday, 6-Sunday

hours_delta = datetime.timedelta(hours=12)
print(datetime.datetime.today()+hours_delta)

datetime_today = datetime.datetime.now(tz=pytz.utc)

datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_today)
print(datetime_pacific)
# jakie sa dostepne timezone
# for tz in pytz.all_timezones:
#    print(tz)
print(datetime_pacific.strftime('%B %d, %Y')) # %B <-- month, dunno why
#strftime from object to string
#strptime from string to object p-> parsing
print(datetime.datetime.strptime('March 24, 2019', '%B %d, %Y')) #output: 2019-03-24
