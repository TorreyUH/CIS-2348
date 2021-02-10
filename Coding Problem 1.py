# Torrey Brett PSID: 1498427

from datetime import datetime

year = int(input('What year were you born? ex: 1990 '))
month = int(input('What is the number of the month you were born? ex: 1 - 12 '))
day = int(input('What is the day you were born? ex: 25'))

DOB = datetime(year, month, day)
Age = (datetime.now() - DOB)

convert_days = int(Age.days)

AgeYears = convert_days/365

print('Birthday Calculator')
print('Current day:', datetime.today())
print('Month: ', datetime.now().month)
print('Day: ', datetime.now().day)
print('Year: ', datetime.now().year)
print('You are', int(AgeYears), 'years old.')
