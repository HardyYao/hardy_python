# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 20:04
# @Author  : HardyYao
# @FileName: practice.py
# @Software: PyCharm

# 个性化消息
name = 'Hardy'
message = 'Hello ' + name + ', would you like to learn some Python today?'
print('------------------------个性化消息------------------------')
print(message + '\n')

# 调整名字的大小写
print('------------------调整名字的大小写------------------------')
print('小写：', name.lower())
print('大写：', name.upper())
print('首字母大写：', name.title() + '\n')

# 编写4个表达式，输出数字6
print('-----------------编写4个表达式，输出数字6-----------------')
print(1 + 5)
print(7 - 1)
print(2 * 3)
print(int(12/2))
print()

# 最喜欢的数字
print('-----------------------最喜欢的数字-----------------------')
num = 6
print('My favorite number is', num)
print()

# 将字符串转换为数字
print('--------------------将字符串转换为数字--------------------')
strNum = '123'
print('原来strNum的类型为：', type(strNum))
strNum = int(strNum)
print('转换后strNum的类型为：', type(strNum))