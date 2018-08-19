# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 10:13
# @Author  : HardyYao
# @FileName: amusement_park.py
# @Software: PyCharm

age = 15

if age < 4:
    print('四岁一下的儿童可免费入场！')
elif age < 15:
    print('4岁以上，15岁以下的门票费为5元！')
elif age < 18:
    print('15岁以上，18岁以下的门票费为10元！')
else:
    print('18岁以上的成人门票费为20！')
