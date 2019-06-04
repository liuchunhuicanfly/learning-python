# encoding: UTF-8

# 字典
'''
字典是另一种可变容器模型，类似于我们生活中使用的字典，
它可以存储任意类型对象，与列表、集合不同的是，字典的每个元素都是由一个键和一个值组成的“键值对”，键和值通过冒号分开
'''

def main():
	dict1 = {'name': 'richard', 'age': '26', 'gender': 'man'}

	# 通过键可以获取字典中对应的值
	print(dict1['name']) # richard
	# print(dict1['address']) # KeyError: 'address'

	# 对字典进行遍历(遍历的其实是键再通过键取对应的值)
	for key in dict1:
		print('%s\t--->\t%s' % (key, dict1[key]))
	'''
	name	--->	richard
	age	--->	26
	gender	--->	man
	'''

	# 更新字典中的元素
	dict1['name'] = 'jack'
	print(dict1) # {'name': 'jack', 'age': '26', 'gender': 'man'}
	dict1.update(name = 'rn', age = '23')
	print(dict1) # {'name': 'rn', 'age': '23', 'gender': 'man'}

	print(dict1.get('name')) # rn

	# 删除字典中的元素
	print(dict1.popitem()) # 'gender', 'man')
	print(dict1) # {'name': 'rn', 'age': '23'}
	print(dict1.pop('name', 'jack')) # rn
	print(dict1) # {'age': '23'}

	# 清空字典
	dict1.cleat()
	print(dict1) # {}






if __name__ == '__main__':
	main()