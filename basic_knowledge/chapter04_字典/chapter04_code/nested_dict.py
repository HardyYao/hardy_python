# -*- coding: utf-8 -*-
# @Time    : 2018/8/22 20:09
# @Author  : HardyYao
# @FileName: nested_dict.py
# @Software: PyCharm

'''
在列表中嵌套字典
'''
print('---------------------在列表中嵌套字典---------------------')

# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# 显示前五个外星人
for alien in  aliens[:5]:
    print(alien)
print('...')

# 显示创建了多少个外星人
print('Total number of aliens: ' + str(len(aliens)))

'''
在字典中嵌套列表
'''
print('---------------------在字典中嵌套列表---------------------')

# 存储喜欢的编程语言的信息
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

'''
在字典中嵌套字典
'''
print('---------------------在字典中嵌套字典---------------------')

# 存储两个用户的个人信息：名、姓和居住地
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}

for username, user_info in users.items():
    print("Username: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())