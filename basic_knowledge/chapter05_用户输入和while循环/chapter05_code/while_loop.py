# -*- coding: utf-8 -*-
# @Time    : 2018/8/29 23:07
# @Author  : HardyYao
# @FileName: while_loop.py
# @Software: PyCharm

# while循环从1数到5
print("-----------------------while循环从1数到5-----------------------")
number = 1
while number <= 5:
    print(number)
    number += 1


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


# 使用while循环来处理列表
print("-----------------------使用while循环来处理列表-----------------------")

# 首先，创建一个待验证用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证用户为止，将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# 使用while循环来处理字典
print("-----------------------使用while循环来处理字典-----------------------")

responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nwhat is your name? ")
    response = input("which mountain would you like to climb someday? ")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")