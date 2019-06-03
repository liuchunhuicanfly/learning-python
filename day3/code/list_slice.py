# 列表的切片操作
def main():
	fruits = ['grape', 'apple', 'strawberry', 'waxberry']
	fruits += ['pitaya', 'pear', 'mango']
	print(fruits) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

	for fruit in fruits:
		print(fruit.title(), end = ' ')
	# print: Grape Apple Strawberry Waxberry Pitaya Pear Mango
	
	num_list = [1, 2, 3, 'jack']
	# for num in num_list:
	# 	print(num.title(), end = ' ')
	# print: AttributeError: 'int' object has no attribute 'title'
	
	# 列表切片
	fruits2 = fruits[1:4]
	print(fruits2) # ['apple', 'strawberry', 'waxberry']

	# fruit3 = fruits  # 没有复制列表只创建了新的引用
	# ？？原list操作是否对新list产生影响
	# fruits.remove('apple')
	# print(fruits) # ['grape', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
	# print(fruits3) # ['grape', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

	# 可以通过完整切片操作来复制列表
  fruits3 = fruits[:]
  fruits.remove('mango')
  print(fruits) # ['grape', 'strawberry', 'waxberry', 'pitaya', 'pear']
	print(fruits3) # ['grape', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

	fruits4 = fruits[-3:-1]
	print(fruits4) # ['pitaya', 'pear']

	# 可以通过反向切片操作来获得倒转后的列表的拷贝
	fruits5 = fruits[::-1]
	print(fruits5) # ['pear', 'pitaya', 'waxberry', 'strawberry', 'grape']


if __name__ == '__main__':
    main()
