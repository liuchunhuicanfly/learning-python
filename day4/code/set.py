# encoding: UTF-8

# 集合
# Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。
def main():
	set1 = {1, 2, 3, 4, 5, 5, 6, 6}
	print(set1) # {1, 2, 3, 4, 5, 6}
	print(len(set1)) # 6

	set2 = set(range(1, 10))
	print(set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

	set1.add(1)
	print(set1) # {1, 2, 3, 4, 5, 6}

	set1.add(7)
	print(set1) # {1, 2, 3, 4, 5, 6, 7}

	set2.update([11, 12])
	print(set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12}

	set2.discard(5)
	print(set2) # {1, 2, 3, 4, 6, 7, 8, 9, 11, 12}

	# remove的元素如果不存在会引发KeyError
	# set2.remove(5) # KeyError
	
	# 遍历集合容器
	for n in set2:
	 	print(n ** 2, end = ' ') # 1 4 9 16 36 49 64 81 121 144

	# 将元组转换成集合
	set3 = set((1, 2, 3, 3, 2, 1))
	print(set3.pop()) # 1
	print(set3) # {2, 3}

	# 集合的交集
	set4 = {1, 2, 3, 4, 5}
	set5 = {4, 5, 6, 7, 8}
	print(set4 & set5) # {4, 5}
	print(set4.intersection(set5)) # {4, 5}

	# 集合的并集
	print(set4 | set5) # {1, 2, 3, 4, 5, 6, 7, 8}
	print(set4.union(set5)) # {1, 2, 3, 4, 5, 6, 7, 8}
	
	# 集合的差集
	print(set4 - set5) # {1, 2, 3}
	print(set5 - set4) # {8, 6, 7}
	print(set4.difference(set5)) # {1, 2, 3}
	print(set5.difference(set4)) # {8, 6, 7}

	# 集合的对称差运算
	print(set4 ^ set5) # {1, 2, 3, 6, 7, 8}
	print(set4.symmetric_difference(set5)) # {1, 2, 3, 6, 7, 8}

	# 判断子集和超集
	print(set4 <= set5) # False
	print({4, 5} <= set5) # True
	print(set4.issubset(set5)) # False
	print({4, 5}.issubset(set5)) # True

	print(set4 >= set5) # False
	print({4, 4, 5, 6, 7, 8, 9, 10} >= set5) # True
	print(set4.issuperset(set5)) # False
	print({4, 4, 5, 6, 7, 8, 9, 10}.issuperset(set5)) # True

	'''
	PS： Python中允许通过一些特殊的方法来为某种类型或数据结构自定义运算符，
	上面的代码中对集合进行运算的时候可以调用集合对象的方法，
	也可以直接使用对应的运算符，例如&运算符跟intersection方法的作用就是一样的，但是使用运算符让代码更加直观。
	'''

if __name__ == '__main__':
	main()