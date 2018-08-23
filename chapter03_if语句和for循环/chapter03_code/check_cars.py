# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 23:14
# @Author  : HardyYao
# @FileName: check_cars.py
# @Software: PyCharm

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    # 如果车名为audi，则以首字母大写的形式输出
    if car == 'audi':
        print('车名为audi，以首字母大写的形式输出:', car.title())
    # 否则，原样输出
    else:
        print('原样输出:', car)