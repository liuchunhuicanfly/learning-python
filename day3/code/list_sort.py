# 列表的排序
def main():
	arr1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
	arr2 = sorted(arr1)
	# sorted函数返回列表排序后的拷贝不会修改传入的列表
  # 函数的设计就应该像sorted函数一样尽可能不产生副作用
  print(arr2) # ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']

  arr3 = [1, 2, 3, 'apple', 'zoo', 'internationalization']
  arr4 = sorted(arr3) # '<' not supported between instances of 'str' and 'int'
 
 	# 倒序
  arr5 = sorted(arr1, reverse=True)
  print(arr5) # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']

  # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
  arr6 = sorted(arr1, key=len)
  print(arr6) # ['zoo', 'apple', 'orange', 'blueberry', 'internationalization']

  # ?? 相同长度排序
  arr7 = ['orang', 'apple', 'zoorr', 'internationalization', 'blueberry']
  arr8 = sorted(arr7, key = len)
  print(arr8) # ['orang', 'apple', 'zoorr', 'blueberry', 'internationalization']

  # 给列表对象发出排序消息直接在列表对象上进行排序
  arr1.sort(reverse=True)
  print(arr1) # ['zoo', 'orange', 'internationalization', 'blueberry', 'apple']