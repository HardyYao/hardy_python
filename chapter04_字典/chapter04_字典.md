# chapter04 字典

## 在本章中，你将学习：

> 如何使用和访问字典中的信息

> 如何增删改字典中的信息

> 如何遍历字典中的数据

> 如何存储字典的列表、存储列表的字典和存储字典的字典

### 4.1 如何使用和访问字典中的信息

在Python中，字典是一系列键-值对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。

在Python中，字典用放在花括号{}中的一系列键-值对表示，如下所示：

	dict = {'key1': 'value1', 'key2': 'value2'}

键-值对是两个相关联的值。指定键时，Python将返回与之相关联的值。键和值之间用冒号分隔，而键-值对之间用逗号分隔。在字典中，你想存储多少个键-值对都可以。

要访问字典中的信息，即获取与键相关联的值，可依次指定字典名和放在括号内的键。

新建一个名为dict.py的文件，编写以下代码：

	dict = {'key1': 'value1', 'key2': 'value2'}
	print(dict['key1'])

运行这个程序，会输出以下结果：

	value1

### 4.2 如何增删改字典中的信息

字典是一种动态结构，可随时在其中增删改键-值对。要想增删改键-值对，可依次指定字典名、用方括号括起来的键和相关联的值。

下面举个具体的例子，字典alien存储了有关特定外星人的信息，通过增删改alien的键-值对，可修改外星人的相关信息。

新建一个名为alien.py的文件，编写以下代码：

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

运行这个程序，会输出以下结果：

	初始字典为： {'color': 'green', 'points': 5}
	添加两个键-值对后的字典为： {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 10}
	删除掉一个键以后的字典为： {'color': 'green'}
	修改后的字典为： {'color': 'red', 'points': 5}

### 4.3 如何遍历字典中的数据

一个Python字典可能只包含几个键-值对，也可能包含数百万个键-值对。鉴于字典可能包含大量的数据，Python支持对字典遍历。字典可用于以各种方式存储信息，因此有多种遍历字典的方式：可遍历字典所有键-值对、键或值。

下面来遍历一个新字典，它用于存储不同程序员最喜欢的编程语言。

新建一个名为favorite_languages.py的文件，编写以下代码：

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

运行这个程序，会输出以下结果：

	遍历字典favorite_languages中所有的键-值对：
	Key:jen
	Value:python
	Key:sarah
	Value:c
	Key:edward
	Value:ruby
	Key:phil
	Value:python
	-----------------------------------------------------
	遍历字典favorite_languages中所有的键：
	name:Jen
	name:Sarah
	name:Edward
	name:Phil
	-----------------------------------------------------
	按顺序遍历字典favorite_languages中所有的键：
	name:Edward
	name:Jen
	name:Phil
	name:Sarah
	-----------------------------------------------------
	遍历字典favorite_languages中所有的值：
	language:Python
	language:C
	language:Ruby
	language:Python

### 4.4 如何存储字典的列表、存储列表的字典和存储字典的字典