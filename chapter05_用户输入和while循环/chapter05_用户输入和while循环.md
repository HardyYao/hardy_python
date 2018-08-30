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
	How old are you ? 21
	21大于18，True or False: True

### 4.2 如何使用while循环

for循环用于针对集合中的每个元素的一个代码块，而while循环不断地运行，直到制定的条件不满足为止。

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



### 4.3 小结



### 4.4 题外话

