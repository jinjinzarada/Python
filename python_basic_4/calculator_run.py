# 모듈 
# import calculator as c
from calculator import add, sub 

# calculator.add(10,20)
# calculator.sub(20,10)
# calculator.times(10,20)
# calculator.dev(10,5)

# c.add(10,20)
# c.sub(20,10)
# c.times(10,20)
# c.dev(10,5)

add(10,20)
sub(10,5)

from datetime import date # 날짜

today = date.today()
print(today)
new_date =date(1999,12,31)
print(new_date)

from datetime import time # 시간

print(time(9))
print(time(9,2))
print(time(9,2,2))
print(time(9,2,2,2222))

from datetime import datetime

dt = datetime(2002,10,20,14,5,2)
print(dt)

from datetime import datetime, timedelta

today = datetime.now()
print(today)
print(today - timedelta(days = 20)) # , hours=, weeks=,minutes=


from time import strftime

now = strftime("%Y-%m-%d %H:%M")
now = strftime("%Y년 %m월 %d일 %H시%M분")

print(now)