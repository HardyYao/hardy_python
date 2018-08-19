# -*- coding: utf-8 -*-
# @Time    : 2018/8/19 0:00
# @Author  : HardyYao
# @FileName: judge_age2.py
# @Software: PyCharm

age_0 = 18
age_1 = 23

print('两个年龄值有一个大于20，结果为True；若两个年龄值都小于20，则为False，结果为：')

# 为了增加可读性，可将每个条件测试都放在一对括号中(当然，不这样做的话也不会出错)
if (age_0 >= 20) or (age_1 >= 20):
    print(True)
else:
    print(False)