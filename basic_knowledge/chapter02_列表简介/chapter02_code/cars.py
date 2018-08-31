# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 0:57
# @Author  : HardyYao
# @FileName: cars.py
# @Software: PyCharm

# 使用方法sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
# 将汽车按字母排序
cars.sort()
print(cars)

# 使用方法sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)

print('Here is the sorted list:')
print(sorted(cars))

print('Here is the original list:')
print(cars)