# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 22:42
# @Author  : HardyYao
# @FileName: greeter.py
# @Software: PyCharm

# 获取用户名字
print("-----------------------获取用户名字-----------------------")
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# 使用int()来获取数值输入
print("-----------------------使用int()来获取数值输入-----------------------")
age = input("How old are you ? ")
age = int(age)
print(str(age) + "大于18，True or False: " + str(age >= 18))