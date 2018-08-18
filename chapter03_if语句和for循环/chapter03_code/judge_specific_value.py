# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 0:26
# @Author  : HardyYao
# @FileName: judge_specific_value.py
# @Software: PyCharm

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('特定的值若在列表中，flag为True；否则为False，结果为：')

flag1 = 'mushrooms' in requested_toppings
if flag1:
    print(flag1)
else:
    print(flag1)

print('--------------------------------------------------------')

print('特定的值若在列表中，flag为True；否则为False，结果为：')
flag2 = 'pepperoni' in requested_toppings
if flag2:
    print(flag2)
else:
    print(flag2)