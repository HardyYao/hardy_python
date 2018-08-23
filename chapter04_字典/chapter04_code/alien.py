# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 20:47
# @Author  : HardyYao
# @FileName: alien.py
# @Software: PyCharm

alien = {'color': 'green', 'points': 5}
print('初始字典为：', alien)

# 增加键-值对
alien['x_position'] = 0
alien['y_position'] = 10
print('添加两个键-值对后的字典为：', alien)

# 删除键-值对
alien = {'color': 'green', 'points': 5}
del alien['points']
print('删除掉一个键以后的字典为：', alien)

# 修改键-值对
alien = {'color': 'green', 'points': 5}
alien['color'] = 'red'
print('修改后的字典为：', alien)