# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 21:23
# @Author  : HardyYao
# @FileName: favorite_languages.py
# @Software: PyCharm

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 遍历字典中所有的键-值对
print('遍历字典favorite_languages中所有的键-值对：')
for key, value in favorite_languages.items():
    print('Key:' + key)
    print('Value:' + value)

print('-----------------------------------------------------')

# 遍历字典中所有的键
print('遍历字典favorite_languages中所有的键：')
for name in favorite_languages.keys():
    print('name:' + name.title())

print('-----------------------------------------------------')

# 按顺序遍历字典中所有的键
print('按顺序遍历字典favorite_languages中所有的键：')
for name in sorted(favorite_languages.keys()):
    print('name:' + name.title())

print('-----------------------------------------------------')

# 遍历字典中所有的值
print('遍历字典favorite_languages中所有的值：')
for language in favorite_languages.values():
    print('language:' + language.title())
