# -*- coding: utf-8 -*-
# @Time    : 2018/8/18 23:38
# @Author  : HardyYao
# @FileName: judge_age.py
# @Software: PyCharm

age_0 = 18
age_1 = 23

# 为了增加可读性，可将每个条件测试都放在一堆括号中(当然，不这样做的话也不会出错)
flag = (age_0 >= 20) and (age_1 >= 20)

print('两个年龄值都大于20，flag为True，否则为False，结果为：')
if flag:
    print(flag)
else:
    print(flag)