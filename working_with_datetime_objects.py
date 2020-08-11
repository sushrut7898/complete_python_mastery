from datetime import datetime
import time

dt1 = datetime(2018, 1, 1)
print(dt1)
dt2 = datetime.now()
print(dt2)
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")    #String to DateTime
print(dt)
dt = datetime.fromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))  #DateTime to String
print(dt1 > dt2)