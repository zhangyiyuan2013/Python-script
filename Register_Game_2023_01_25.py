# Inspired by the bilibili registration effect.
# Register_Game_2023_01_25.py
# Author: Zhang Yiyuan
# Data: 2023_01_25
# Age: 9
# A registration game for you! Go ahead and give it a try!
import easygui,time
name = easygui.enterbox("Enter your name: ")
code = easygui.enterbox("Enter your code:")
easygui.msgbox("Register successfully!")
easygui.msgbox("Loading......")
time.sleep(1)
easygui.msgbox("Name: " + name + "\nCode: ······")
