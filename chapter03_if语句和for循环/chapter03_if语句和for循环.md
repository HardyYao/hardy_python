# chapter03 if语句和for循环

## 在本章中，你将学习：

> 如何使用if语句和for循环检查条件

> 如何编写简单的if-else语句

> 如何编写简单的if-elif-else语句

### 3.1 条件测试：检查一个条件

在编程中，经常需要检查一系列条件，并以此决定执行哪些操作，在Python中，检查条件使用的是if语句。

假设你有一个列表，列表中存储着几辆车的名称，每辆车的名称都是小写的，但是对于其中某辆车，你想以首字母大写的形式输出它，可以结合if语句和for循环做到这件事。

新建一个名为check_cars.py的文件，编写以下代码：

	cars = ['audi', 'bmw', 'subaru', 'toyota']
	
	for car in cars:
	    # 如果车名为audi，则以首字母大写的形式输出
	    if car == 'audi':
	        print('车名为audi，以首字母大写的形式输出:', car.title())
	    # 否则，原样输出
	    else:
	        print('原样输出:', car)

运行这个程序，会输出以下结果：

	车名为audi，以首字母大写的形式输出: Audi
	原样输出: bmw
	原样输出: subaru
	原样输出: toyota

### 3.2 条件测试：检查多个条件

有时，仅仅检查一个条件可能无法获取你想要的数据，这种时候，你可以使用and和or来检查多个条件。

#### 3.2.1 使用and检查多个条件

若要检查多个条件都为True，可使用关键字and将多个条件测试合而为一；如果每个测试都通过了，整个表达式就为True；如果至少有一个测试没有通过，整个表达式就为False。

新建一个名为judge_age.py的文件，编写以下代码：

	age_0 = 18
	age_1 = 23
	
	# 为了增加可读性，可将每个条件测试都放在一堆括号中(当然，不这样做的话也不会出错)
	flag = (age_0 >= 20) and (age_1 >= 20)
	
	print('两个年龄值都大于20，flag为True，否则为False，结果为：')
	if flag:
	    print(flag)
	else:
	    print(flag)

运行这个程序，会输出以下结果：

	两个年龄值都大于20，flag为True，否则为False，结果为：
	False

#### 3.2.2 使用or检查多个条件

若检查的多个条件只需要有一个为True，可使用关键字or将多个条件测试合而为一；只要有一个测试都通过了，整个表达式就为True；如果所有测试都没有通过，整个表达式才为False。

新建一个名为judge_age2.py的文件，编写以下代码：

	age_0 = 18
	age_1 = 23
	
	# 为了增加可读性，可将每个条件测试都放在一堆括号中(当然，不这样做的话也不会出错)
	flag = (age_0 >= 20) or (age_1 >= 20)
	
	print('两个年龄值有一个大于20，flag为True；若两个年龄值都小于20，则为False，结果为：')
	if flag:
	    print(flag)
	else:
	    print(flag)

运行这个程序，会输出以下结果：

	两个年龄值有一个大于20，flag为True；若两个年龄值都小于20，则为False，结果为：
	True

### 3.3 检查特定值是否包含在列表中

有时候，你需要获取列表中某个特定的值，要判断某个值是否存在列表中，可使用关键字in。

新建一个名为judge_specific_value.py的文件，编写以下代码：

	requested_toppings = ['mushrooms', 'onions', 'pineapple']
	
	print('特定的值若在列表中，flag为True；否则为False，结果为：')
	
	flag1 = 'mushrooms' in requested_toppings
	if flag1:
	    print(flag1)
	else:
	    print(flag1)
	
	print('--------------------------------------------------------')
	
	print('特定的值若在列表中，flag为True；否则为False，结果为：')
	flag2 = 'pepperoni' in requested_toppings
	if flag2:
	    print(flag2)
	else:
	    print(flag2)

运行这个程序，会输出以下结果：

	特定的值若在列表中，flag为True；否则为False，结果为：
	True
	--------------------------------------------------------
	特定的值若在列表中，flag为True；否则为False，结果为：
	False
