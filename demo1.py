from datetime import *

# print(datetime.now())
# dt = datetime(2020, 8, 13, 12, 00)
# print(dt)

# # 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# print(dt.timestamp())

# t = 1597291200.0
# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t))

# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(type(cday))

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M:%S'))