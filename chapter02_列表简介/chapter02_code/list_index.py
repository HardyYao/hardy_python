# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 1:18
# @Author  : HardyYao
# @FileName: list_index.py
# @Software: PyCharm

# 每当需要访问最后一个列表元素时，都可使用索引-1.这在除列表为空以外的任何情况都有效，即便你最后一次访问列表后，其长度发生了变化
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])

# 当列表为空时，这种访问最后一个最后一个元素的方式也会引发索引错误
motorcycles = []
print(motorcycles[-1])

# 以下程序将引发索引错误，原因是索引号超出列表长度
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])