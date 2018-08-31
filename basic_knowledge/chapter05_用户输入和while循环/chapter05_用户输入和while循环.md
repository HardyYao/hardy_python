# chapter05 用户输入和while循环

## 在本章中，你将学习：

> 如何接受用户输入的数据

> 如何使用while循环

### 4.1 如何接受用户输入的数据

大多数程序都旨在解决最终用户的问题，为此通常需要从用户那里获取一些信息。在程序需要一个名字时，你需要提示用户输入改名字；程序需要一个名单时，你需要提示用户输入一系列名字。为此，你需要使用函数input()。

新建一个名为greeter.py的文件，编写以下代码：

	# 获取用户名字
	print("-----------------------获取用户名字-----------------------")
	name = input("Please enter your name: ")
	print("Hello, " + name + "!")
	
	# 使用int()来获取数值输入
	print("-----------------------使用int()来获取数值输入-----------------------")
	age = input("How old are you ? ")
	age = int(age)
	print(str(age) + "大于18，True or False: " + str(age >= 18))

运行这个程序，会输出以下结果：

	-----------------------获取用户名字-----------------------
	Please enter your name: Hardy
	Hello, Hardy!
	-----------------------使用int()来获取数值输入-----------------------
	How old are you ? 23
	23大于18，True or False: True

### 4.2 如何使用while循环

for循环用于针对集合中的每个元素的一个代码块，而while循环则会不断地运行，直到指定的条件不满足为止。

新建一个名为while_loop.py的文件，编写以下代码：
	
	# while循环从1数到5
	print("-----------------------while循环从1数到5-----------------------")
	number = 1
	while number <= 5:
	    print(number)
	    number += 1
	
	
	# while循环让用户选择何时退出
	print("-----------------------while循环让用户选择何时退出-----------------------")
	prompt = "Tell me something, and I will repeat it back to you, enter 'quit' to end the program: "
	
	active  = True
	while active:
	    message = input(prompt)
	
	    if message == 'quit':
	        active = False
	
	    else:
	        print(message)
	
	
	# 使用break退出循环
	print("-----------------------使用break退出循环-----------------------")
	prompt = "Please enter the name of a city you have visited, enter 'quit' to end the program: "
	
	while True:
	    city = input(prompt)
	
	    if city == 'quit':
	        break
	
	    else:
	        print("I'd love to go to " + city.title() + "!")
	
	
	# 在while循环中使用continue
	print("-----------------------在while循环中使用continue-----------------------")
	current_number = 0
	while current_number < 16:
	    current_number += 1
	    if current_number%2 == 0:
	        continue
	
	    print(current_number)
	
	
	# 使用while循环来处理列表
	print("-----------------------使用while循环来处理列表-----------------------")
	
	# 首先，创建一个待验证用户列表和一个用于存储已验证用户的空列表
	unconfirmed_users = ['alice', 'brian', 'candace']
	confirmed_users = []
	
	# 验证每个用户，直到没有未验证用户为止，将每个经过验证的列表都移到已验证用户列表中
	while unconfirmed_users:
	    current_user = unconfirmed_users.pop()
	
	    print("Verifying user: " + current_user.title())
	    confirmed_users.append(current_user)
	
	# 显示所有已验证的用户
	print("\nThe following users have been confirmed: ")
	for confirmed_user in confirmed_users:
	    print(confirmed_user.title())
	
	
	# 使用while循环来处理字典
	print("-----------------------使用while循环来处理字典-----------------------")
	
	responses = {}
	
	# 设置一个标志，指出调查是否继续
	polling_active = True
	
	while polling_active:
	    # 提示输入被调查者的名字和回答
	    name = input("\nwhat is your name? ")
	    response = input("which mountain would you like to climb someday? ")
	
	    # 将答卷存储在字典中
	    responses[name] = response
	
	    # 看看是否还有人要参与调查
	    repeat = input("Would you like to let another person respond? (yes / no) ")
	    if repeat == 'no':
	        polling_active = False
	
	# 调查结束，显示结果
	print("\n--- Poll Results ---")
	for name, response in responses.items():
	    print(name + " would like to climb " + response + ".")

运行这个程序，会输出以下结果：

	-----------------------while循环从1数到5-----------------------
	1
	2
	3
	4
	5
	-----------------------while循环让用户选择何时退出-----------------------
	Tell me something, and I will repeat it back to you, enter 'quit' to end the program: Hello
	Hello
	Tell me something, and I will repeat it back to you, enter 'quit' to end the program: quit
	-----------------------使用break退出循环-----------------------
	Please enter the name of a city you have visited, enter 'quit' to end the program: HangZhou
	I'd love to go to Hangzhou!
	Please enter the name of a city you have visited, enter 'quit' to end the program: quit
	-----------------------在while循环中使用continue-----------------------
	1
	3
	5
	7
	9
	11
	13
	15
	-----------------------使用while循环来处理列表-----------------------
	Verifying user: Candace
	Verifying user: Brian
	Verifying user: Alice
	
	The following users have been confirmed: 
	Candace
	Brian
	Alice
	-----------------------使用while循环来处理字典-----------------------
	
	what is your name? Hardy
	which mountain would you like to climb someday? TaiShan
	Would you like to let another person respond? (yes / no) yes
	
	what is your name? HardyYao
	which mountain would you like to climb someday? HengShan
	Would you like to let another person respond? (yes / no) no
	
	--- Poll Results ---
	Hardy would like to climb TaiShan.
	HardyYao would like to climb HengShan.

### 4.3 小结

在本章中，你学习了使用input()函数来接受用户输入的数据，同时结合了input()函数和while循环，从而可以输出各种各样的交互信息。

### 4.4 题外话

写到这里，基础篇还差函数、类、文件处理和异常处理等知识点没讲，后面打算换种方式写了，尽量结合一些小项目来讲解，这样更能锻炼自己，在别人看来，文章也会更有趣些。

距离上一篇文章发布，已经过去一个多星期了，我更新得还是太慢了，写作效率还有待提升，

最近到天津出差，要将近一个月以后才能回去。虽然才8月份，现在总结还早了些，不过，2018，于我而言，真的是四处奔波的一年。我经历过两家公司，出过两次差，所以在半年多的时间里去过了四个城市：惠州->广州->茂名(出差)->广州->惠州->天津(出差)。每到一个新的地方，都得学会适应那里的环境，挺耗费时间与精力。

虽然长辈们都说：趁着年轻，多出去走走，这是好事。可我真的不喜欢这样四处奔波，因为我目标很明确，我知道自己要干嘛，我想做的事情还有很多，我希望能有一个固定的、舒适的住处，专心学习自己感兴趣的东西，外面的世界，等我想见识了，我再出去走走就是了。可是，工作上的安排，也没办法呀，不想去也得去，权当锻炼自己的毅力和意志力了。

很想过得潇洒一些，可是现在的自己，不管是性格还是能力，都不足以支撑起那样的生活方式。

再给自己几年时间吧，未来充满着变数，要始终坚信自己会有个十分有趣的未来，不然，活着可就太痛苦了哈。