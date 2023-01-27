# Guess grades.py
# Author: Zhang Yiyuan
# Data: 2023_01_27
# Age: 9
# A registration game for you! Go ahead and give it a try!
score = float(input('Please enter the score: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('The grade is:', grade)
