import datetime
import pytz

d = datetime.date(1996, 11, 3) # Выводит дату: год, месяц, день
print(d)

tday = datetime.date.today() # Выводит сегодняшний день
print(tday)
print(tday.weekday()) # Выводит день недели, индекс с 0 до 6
print(tday.isoweekday()) # Выводит день недели, индекс с 1 до 7

tdelta = datetime.timedelta(days=7) # Длительность, выражающая разницу между двумя экземплярами даты
print(tday - tdelta)

bday = datetime.date(2019, 11, 3)
till_day = bday - tday
print(till_day.total_seconds())

t = datetime.time(13, 13, 13)
dt = datetime.datetime(1996, 11, 3, 13, 13, 13)
print(dt)

dt_today = datetime.datetime.today() # Возвращает текущую локальную дату и время без tzinfo
dt_now = datetime.datetime.now() # Возвращает текущую местную дату, без tz похоже на today, с tz можно узнать более точно
dt_utcnow = datetime.datetime.utcnow() # Возвращает текущую дату и время UTC

print(dt_today)
print(dt_now)
print(dt_utcnow)
print()

dt_now1 = datetime.datetime.now(tz=pytz.UTC)
dt_utcnow1 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_now1)
print(dt_utcnow1)
print()

#dt_mtn = dt_utcnow1.astimezone(pytz.timezone('Europe/Prague'))
dt_mtn = dt_utcnow1.astimezone(pytz.timezone('Europe/Moscow')) # Возвращает объект с новым атрибутом tzinfo, скорректировав данные, чтобы результат был UTC, но по местному времени
print(dt_mtn)
print(dt_mtn.strftime('%B %d, %Y')) # strftime - возвращает дату в виде строки
dt_str = 'September 11, 2019'
aa = datetime.datetime.strptime(dt_str, '%B %d, %Y') # strptime - возвращает дату в виде даты
print(aa)
print()

#for tz in pytz.all_timezones:
#    print(tz)

mtn_tz = pytz.timezone('Europe/Moscow')
dt_now = mtn_tz.localize(dt_now)
dt_e = dt_now.astimezone(pytz.timezone('Europe/Prague'))
print(dt_e)