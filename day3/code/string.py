def main():
	str = 'hello, world'

	# len() 计算字符串的长度
	print(len(str)) # 12

	# 获得字符串首字母大写的拷贝
	print(str.capitalize()) # Hello, world

	# 获得字符串变大写后的拷贝
	print(str.upper()) # HELLO, WORLD

	# 从字符串中查找子串所在位置
	print(str.find('or')) # 8
	print(str.find('shit')) # -1

	# 与find类似但找不到子串时会引发异常
	print(str.index('or')) # 8
	print(str.index('shit')) # ValueError: substring not found

	# 检查字符串是否以指定的字符串开头
	print(str.startswith('F')) # False
	print(str.startswith('h')) # True

	# 检查字符串是否以指定的字符串结尾
	print(str.endswith('F')) # False
	print(str.endswith('d')) # True

	# 将字符串以指定的宽度居中并在两侧填充指定的字符
	print(str.center(20, '*')) # ****hello, world****

	# 将字符串以指定的宽度靠右放置左侧填充指定的字符
	print(str.rjust(20, '*')) # ********hello, world

	str1 = '12345678'

	# 从字符串中取出指定位置的字符（下标运算）
	print(str1[2]) # 3

	# 字符串切片(从指定的开始索引到指定的结束索引)
	# 不取右边界值
	print(str1[0:2]) # 12

	# 边界值未指定代表取之后或之前所有
	print(str1[2:]) # 345678
	print(str1[:3]) # 123

	# -1 表示最后一个字符的索引
	print(str1[0:-1]) # 12345678

	# :: step 代表步长
	print(str1[2::2]) # 357
	print(str1[2::3]) # 36

	# 检查字符串是否由数字构成
	print(str.isdigit()) # False
	print(str1.isdigit()) # True

	# 检查字符串是否以字母构成
	print(str.isalpha()) # False
	str2 = 'ABCD'
	print(str2.isalpha()) # True

	# 检查字符串是否以数字和字母构成
	print(str.isalnum()) # False
	print(str1.isalnum()) # True
	print(str2.isalnum()) # True

	# 获得字符串修剪左右两侧空格的拷贝
	str3 = '     jack 1  11    '
	print(str3.strip()) # 'jack 1  11'
	print(str3) # '     jack 1  11    '


# 执行函数
main()























