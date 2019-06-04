# 列表操作

def main:

	list1 = [1, 2, 3, 5, 200]
	print(list1) # [1, 2, 3, 5, 200]

	list2 = ['hello'] * 5
	print(list2) # ['hello', 'hello', 'hello', 'hello', 'hello']

	# 计算列表长度
	print(len(list1)) # 5
	print(len(list2)) # 5

	# 下标(索引)运算
	print(list1[0]) # 1
	print(list1[-1]) # 200
	print(list1[-3]) # 3
	# print(list1[5]) # IndexError: list index out of range
	
	# 通过下标修改list的值
	list1[2] = 100
	print(list1) # [1, 2, 100, 5, 200]

	# 添加元素
	# append()
	list1.append(1000)
	print(list1) # [1, 2, 100, 5, 200, 1000]
	list.append(111, 222)

	# insert()
	list1.insert(1, 5000)
	print(list1) # [1, 5000, 2, 100, 5, 200, 1000]
	list1.insert(-1, 4000)
	print(list1) # [1, 5000, 2, 100, 5, 200, 4000, 1000]

	# 删除元素
	list1.remove(5000)
	print(list1) # [1, 2, 100, 5, 200, 4000, 1000]

	list3 = [1, 1, 1, 2, 4]
	list3.remove(1)
	print(list3) # [1, 1, 2, 4]

	# list3.remove(5) # ValueError: list.remove(x): x not in list
	
	if 124 in list3:
		list3.remove(124)
	print(list3) # [1, 1, 2, 4]

	del list3[0]
	print(list3) # [1, 2, 4]

	# 清空列表元素
	list3.clear()
	print(list3) #  []


if __name__ == '__main__':
    main()

  























