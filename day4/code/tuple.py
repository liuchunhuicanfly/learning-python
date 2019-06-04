# encoding: UTF-8

# Python 的元组与列表类似，不同之处在于元组的元素不能修改
def main():
	t = ('石头人', '德玛', '机器人', '剑姬')
	print(t) # ('石头人', '德玛', '机器人', '剑姬')

	# 获取元祖元素
	print(t[0]) # '石头人'
	print(t[3]) # 剑姬

	# 遍历元祖的值
	for n in t:
		print(n)
	'''
	石头人
	德玛
	机器人
	剑姬
	'''

	# 重新给元祖赋值
	# t[0] = '剑圣' # TypeError: 'tuple' object does not support item assignment

	# 变量t重新引用了新的元组原来的元组将被垃圾回收
	t = ('赵信',	20,	True,	'德玛西亚')
  print(t) # ('赵信', 20, True, '德玛西亚')

 	# 将元组转换成列表
 	list1 = list(t)
 	print(list1) # ['赵信', 20, True, '德玛西亚']

 	# 列表可修改元素
 	list1[0] = 'richard'
 	print(list1) # ['richard', 20, True, '德玛西亚']

 	t = (person: {name: 'richard', age: '18'}, 'www')
 	t[0].name = 'jack'

 	# 列表转元祖
 	list2 = [1, 2, 3, 4]
 	tuple1 = tuple(list2)

 	'''
 	元组中的元素是无法修改的
 	如果不需要对元素进行添加、删除、修改的时候，可以考虑使用元组
 	如果一个方法要返回多个值，使用元组也是不错的选择
 	元组在创建时间和占用的空间上面都优于列表

 	In [42]: %timeit [1,2,3,4]
 	56.6 ns ± 1.3 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

 	In [43]: %timeit (1,2,3,4)
 	8.25 ns ± 0.0474 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)

	In [47]: t1 = [1, 2, 3, 4]
 	In [48]: sys.getsizeof(t1)
	Out[48]: 96

	In [49]: t2 = (1, 2, 3, 4)
	In [50]: sys.getsizeof(t2)
	Out[50]: 80

 	'''








if __name == '__main__':
	main();