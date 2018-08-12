# chapter02 列表简介

## 在本章中，你将学习：

> 如何使用列表

> 如何访问、增删列表中的元素

> 如何对列表进行永久性排序

> 使用列表时如何避免索引错误

### 2.1 列表是什么

列表是由一系列特定顺序排列的元素组成。你可以创建包含字母表的字母、数字0~9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素可以没有任何关系。鉴于列表通常包含多个元素，给列表指定一个表示复数的名称（如letters、digits或names）是一个不错的注意。

在Python中，用方括号（[]）来表示列表，并用逗号来分隔其中的元素。下面是一个简单的列表示例，这个列表包含几种自行车：

新建一个名为bicycles.py的文件，编写以下代码：

    bicycles = ['trek', 'cannondale', 'redline', 'speciallized']
    print(bicycles)

运行这个程序，会输出以下结果：

    ['trek', 'cannondale', 'redline', 'speciallized']

当然，这并不是用户希望看到的输出，下面来学习如何访问列表元素

### 2.2 如何访问、增删改列表中的元素

#### 2.2.1 如何访问列表中的元素

列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。

例如，下面的代码从列表bicycles中提取出第一款自行车：

    bicycles = ['trek', 'cannondale', 'redline', 'speciallized']
    print(bicycles[0])

运行这个程序，会输出以下结果：

    trek

这里演示了访问列表元素的语法，在Python中，第一个列表元素的索引为0，而不是1。当你请求获取列表元素时，Python只返回该元素，而不包括方括号和引号。这正是用户想看到的结果————整洁、干净的输出。

#### 2.2.2 如何增删改列表中的元素

你创建的大多数列表都将是动态的，这意味着列表创建后，将随着程序的运行增删元素。例如，你创建一个游戏，要求玩家射杀从天而降的外星人；为此，可在开始时将一些外星人存储在列表中，然后每当有外星人被射杀时，都将其从列表中删除，而每次有新的外星人出现在屏幕上时，都将其添加到列表中。在整个游戏运行期间，外星人列表的长度将不断变化。

修改列表元素的语法与访问列表元素的语法类似。要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。

例如，假设有一个摩托车列表，其中的第一个元素为'honda'，如何修改它的值呢？

新建一个名为motorcycles.py的文件，编写以下代码：

	motorcycles = ['honda', 'yamaha', 'suzuki']
	print('初始列表为：',motorcycles)

	# 修改列表中索引为0的元素值
	motorcycles[0] = 'ducati'
	print('修改列表中索引为0的元素,修改后的列表为：', motorcycles)
	
	# 在列表末尾添加元素
	motorcycles = ['honda', 'yamaha', 'suzuki']
	motorcycles.append('ducati')
	print('在列表末尾添加元素,修改后的列表为：', motorcycles)
	
	# 在列表中插入元素
	motorcycles = ['honda', 'yamaha', 'suzuki']
	motorcycles.insert(1, 'ducati')
	print('在列表中插入元素,修改后的列表为：', motorcycles)
	
	# 使用del语句删除元素
	motorcycles = ['honda', 'yamaha', 'suzuki']
	del motorcycles[0]
	print('使用del语句删除元素,修改后的列表为：', motorcycles)
	
	# 使用方法pop()删除元素
	motorcycles = ['honda', 'yamaha', 'suzuki']
	pop_motocycle = motorcycles.pop()
	print('使用方法pop()删除元素,删除的元素值为：', pop_motocycle)
	print('使用方法pop()删除元素,修改后的列表为：', motorcycles)
	
	# 弹出列表中任何位置处的元素
	motorcycles = ['honda', 'yamaha', 'suzuki']
	first_owned = motorcycles.pop(0)
	print('The first motorcycle I owned was a ', first_owned)
	
	# 根据值删除元素
	motorcycles = ['honda', 'yamaha', 'suzuki']
	motorcycles.remove('honda')
	print(motorcycles)

运行这个程序，会输出以下结果：

	初始列表为： ['honda', 'yamaha', 'suzuki']
	修改列表中索引为0的元素,修改后的列表为： ['ducati', 'yamaha', 'suzuki']
	在列表末尾添加元素,修改后的列表为： ['honda', 'yamaha', 'suzuki', 'ducati']
	在列表中插入元素,修改后的列表为： ['honda', 'ducati', 'yamaha', 'suzuki']
	使用del语句删除元素,修改后的列表为： ['yamaha', 'suzuki']
	使用方法pop()删除元素,删除的元素值为： suzuki
	使用方法pop()删除元素,修改后的列表为： ['honda', 'yamaha']
	The first motorcycle I owned was a  honda
	['yamaha', 'suzuki']

### 2.3 组织列表

在你创建的列表中，元素的排列顺序常常是无法预测的，因为你并非总能控制用户提供数据的顺序。这虽然在大多数情况下都是不可避免的，但你经常需要以特定的顺序呈现信息。有时候，你希望保留列表元素最初的排列顺序，而有时候又需要调整排列顺序。Python提供了很多组织列表的方式，可根据具体情况选用。

#### 2.3.1 使用方法sort()和sorted()对列表进行排序

新建一个名为cars.py的文件，编写以下代码：

    # 使用方法sort()对列表进行永久性排序
	cars = ['bmw', 'audi', 'toyota', 'subaru']
	# 将汽车按字母排序
	cars.sort()
	print(cars)
	
	# 使用方法sorted()对列表进行临时排序
	cars = ['bmw', 'audi', 'toyota', 'subaru']
	print('Here is the original list:')
	print(cars)
	
	print('Here is the sorted list:')
	print(sorted(cars))
	
	print('Here is the original list:')
	print(cars)

运行这个程序，会输出以下结果：

	['audi', 'bmw', 'subaru', 'toyota']
	Here is the original list:
	['bmw', 'audi', 'toyota', 'subaru']
	Here is the sorted list:
	['audi', 'bmw', 'subaru', 'toyota']
	Here is the original list:
	['bmw', 'audi', 'toyota', 'subaru']

#### 2.3.2 反转列表顺序以及确定列表的长度

新建一个名为cars2.py的文件，编写以下代码：

	# 反转列表的排列顺序
	cars = ['bmw', 'audi', 'toyota', 'subaru']
	# 将汽车按字母排序倒着排列
	cars.reverse()
	print(cars)
	
	# 求出列表的长度
	cars = ['bmw', 'audi', 'toyota', 'subaru']
	print('列表的长度：', len(cars))

运行这个程序，会输出以下结果：

	['subaru', 'toyota', 'audi', 'bmw']
	列表的长度： 4

### 2.4 使用列表时避免索引错误

刚开始使用列表时，经常会碰到一种错误：索引错误，索引错误意味着Python无法理解你指定的索引。程序发生索引错误时，请尝试将你指定的索引减1，然后再次运行程序，看看结果是否正确。

下面举几个例子进行讲解，新建一个名为list_index.py的列表，编写以下代码：

	# 每当需要访问最后一个列表元素时，都可使用索引-1.这在除列表为空以外的任何情况都有效，即便你最后一次访问列表后，其长度发生了变化
	motorcycles = ['honda', 'yamaha', 'suzuki']
	print(motorcycles[-1])
	
	# 当列表为空时，这种访问最后一个最后一个元素的方式也会引发索引错误
	motorcycles = []
	print(motorcycles[-1])
	
	# 以下程序将引发索引错误，原因是索引号超出列表长度
	motorcycles = ['honda', 'yamaha', 'suzuki']
	print(motorcycles[3])

### 2.5 小结

在本章中，我们学习了：列表是什么以及如何使用其中的元素；如何定义列表以及如何增删改元素；如何对列表进行永久性排序，以及如何为展示列表而进行临时排序；如何确定列表的长度，以及在使用列表时如何避免索引错误。

通过本章的学习，你应该知道了列表的简单使用方法。