# Author: Zhang Yiyuan
# Data: 2023_01_27
# Age: 9
# A registration game for you! Go ahead and gibe it a try!
year = int(input('year of entry: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leap)
