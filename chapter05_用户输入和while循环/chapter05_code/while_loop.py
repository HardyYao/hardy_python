# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 23:07
# @Author  : HardyYao
# @FileName: while_loop.py
# @Software: PyCharm

# while循环从1数到5
print("-----------------------while循环从1数到5-----------------------")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# while循环让用户选择何时退出
print("-----------------------while循环让用户选择何时退出-----------------------")
prompt = "Tell me something, and I will repeat it back to you, enter 'quit' to end the program: "

active  = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False

    else:
        print(message)

# 使用break退出循环
print("-----------------------使用break退出循环-----------------------")
prompt = "Please enter the name of a city you have visited, enter 'quit' to end the program: "

while True:
    city = input(prompt)

    if city == 'quit':
        break

    else:
        print("I'd love to go to " + city.title() + "!")

# 在while循环中使用continue
print("-----------------------在while循环中使用continue-----------------------")
current_number = 0
while current_number < 16:
    current_number += 1
    if current_number%2 == 0:
        continue

    print(current_number)