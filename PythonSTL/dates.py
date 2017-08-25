from datetime import date

now = date.today()
print(now.isoweekday())
print(now.isocalendar())
print(now.timetuple())

print(now)

birthday = date(1997, 6, 22)

print(birthday)

print((now - birthday))
