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