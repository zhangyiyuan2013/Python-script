# Inspired by the Exercises after the lesson.
# Restaurant reservations.py
# Author: Zhang Yiyuan
# Data: 2023_01_26
# Age: 9
# A registration game for you! Go ahead and give it a try!
import random
table = int(input('\nWaiter:How many people dined?\nUser: '))
if table > 8:
    print('Waiter:Sorry, there are no empty tables.')
else:
    print('Waiter:Please go to table 18.')
    Foods = input('Waiter:What did you come up with?\nUser: ')
    print('Your',Foods,'.')
    yuan = random.randint(1,20)
    print("Here's your bill:",yuan,"$")
    Rating = input('How does it feel?(Enter1-5integer): ')
    if Rating == '1':
        print("Emmmmmmmmmmmm...@_@")
    elif Rating == '2':
        print(":(")
    elif Rating == '3':
        print(":)")
    elif Rating == '4':
        print("Good!!")
    elif Rating == '5':
        print("Yes!Great!!YYDS!:)")
    else:
        print("Enter illegal!")

    # if Rating == '1':
    #     print("Emmmmmmmmmmmm...@_@")
    # elif Rating == '2':
    #     print(":(")
    # elif Rating == '3':
    #     print(":)")
    # elif Rating == '4':
    #     print("Good!!")
    # elif Rating == '5':
    #     print("Yes!Great!!YYDS!:)")
    # else:
    #     print("Enter illegal!")
    # Note: Here '1', '2', '3', '4'', '5' should be put in quotation marks!!!

        


