# A day is the day of the year.py
# Author: Zhang Yiyuan
# Data: 2023_01_27
# Age: 9
# A registration game for you! Go ahead and give it a try!
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
res = 0
year = int(input('year: '))
month = int(input('month: '))
day = int(input('day: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: # 闰年二月 29 天
    months[2] += 1

for i in range(month):
    res += months[i]

print(res+day)
