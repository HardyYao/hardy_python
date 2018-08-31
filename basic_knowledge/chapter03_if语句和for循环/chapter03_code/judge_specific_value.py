# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 0:26
# @Author  : HardyYao
# @FileName: judge_specific_value.py
# @Software: PyCharm

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('特定的值若在列表中，结果为True；否则为False，此处的结果为：')

if 'mushrooms' in requested_toppings:
    print(True)
else:
    print(False)

print('--------------------------------------------------------')

print('特定的值若在列表中，结果为True；否则为False，此处的结果为：')

if 'pepperoni' in requested_toppings:
    print(True)
else:
    print(False)