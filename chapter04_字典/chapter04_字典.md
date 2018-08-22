# chapter04 字典

## 在本章中，你将学习：

> 如何使用和访问字典中的信息

> 如何增删改字典中的信息

> 如何遍历字典中的数据

> 字典的嵌套

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

### 4.4 字典的嵌套

有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。

新建一个名为nested_dict.py的文件，编写以下代码：

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

运行这个程序，会输出以下结果：

	---------------------在列表中嵌套字典---------------------
	{'color': 'green', 'points': 5, 'speed': 'slow'}
	{'color': 'green', 'points': 5, 'speed': 'slow'}
	{'color': 'green', 'points': 5, 'speed': 'slow'}
	{'color': 'green', 'points': 5, 'speed': 'slow'}
	{'color': 'green', 'points': 5, 'speed': 'slow'}
	...
	Total number of aliens: 30
	---------------------在字典中嵌套列表---------------------
	Jen's favorite languages are:
		Python
		Ruby
	Sarah's favorite languages are:
		C
	Edward's favorite languages are:
		Ruby
		Go
	Phil's favorite languages are:
		Python
		Haskell
	---------------------在字典中嵌套字典---------------------
	Username: aeinstein
		Full name: Albert Einstein
		Location: Princeton
	Username: mcurie
		Full name: Marie Curie
		Location: Paris

### 4.5 小结

在本章中，你学习了如何使用和访问字典中的信息、如何增删改字典中的信息、如何遍历字典中的数据以及存储字典的列表、存储列表的字典和存储字典的字典。

字典是一种可变容器模型，且可存储任意类型对象。它是Python中非常重要的一种数据结构，在网站开发中，可用字典存储各种各样的关联信息，例如上文中的外星人信息、用户信息以及编程语言信息等；在爬虫中，经常会爬取到大量的json格式的信息，在Python中，可以将json格式的信息转化为字典来进行处理。

总之，字典的用处多多，若能好好利用，可以发挥极大的用处。

### 4.6 题外话

仔细一想，专注于学习与工作，才是令人持续获得充实感的唯一路径。

前几周比较忙的时候，每周也会有两三天比较早回宿舍，可是我却把那些时间花在看视频上面，虽然有时也看会儿书敲会儿代码，但是效率很低，因为我当时觉得周末再认真学习就好了，工作日时间不多，还是算了。然后每次到快要睡觉的时候，心情都会有点失落，心里想着，一天又过去了，我该过多久才能重新找回状态？

就那样过了两三个星期，回顾一下，才发现自己浪费了那么多时间。

从上周六晚上开始，我每天晚上都是先把学习的任务完成了（效率高了很多），然后花半小时的时间学习吹口琴，再有时间，才看一集视频，睡觉前再看一小时的书，这样等到要睡觉的时候，就会觉得今天过得特充实，也没空胡思乱想了。

像前几周那种颓废的状态我大学期间也经历过几次，只不过当时没太在意，认真反思了一下，这样消耗时间，可真的是伤不起啊。

通过这段时间的思考，我想对自己（同时也对看到这篇文章的读者）说：任何时候都不要对自己说，过了这段时间或者做完某件事我再去执行某项计划，这样的想法往往到最后都无法落实。想做什么事，就立刻开始做，时间都是挤出来的，只要开始执行了，成绩就会一点点累积起来，过多一段时间，效果就体现出来了，有了正面反馈，就更加容易坚持下去，长此以往，绝对会有意想不到的进步。