# encoding: utf-8

import time
# 读写文本文件
# def main():
# 	file = open('../res/望海潮-东湖形胜.txt', 'r', encoding='utf-8')
# 	print(file.read())
# 	file.close()

# 通过try, except, finally代码块处理异常
# def main():
# 	file = None
# 	try:
# 		file = open('../res/望海潮-东湖形胜.txt', 'r', encoding='utf-8')
# 		print(file.read())
# 	except FileNotFoundError:
# 		print('无法打开指定文件')
# 	except LookupError:
# 		print('未知的编码格式')
# 	except UnicodeDecodeError:
# 		print('读写文件时解码错误')
# 	finally:
# 		if file:
# 			file.close()
# 	print(file)

# 通过 try, with, except代码块处理异常
# def main():
# 	file = None
# 	try:
# 		with open('../res/望海潮-东湖形胜.txt', 'r', encoding='utf-8') as file:
# 			print(file.read())
# 	except FileNotFoundError:
# 		print('无法打开指定文件')
# 	except LookupError:
# 		print('未知的编码格式')
# 	except UnicodeDecodeError:
# 		print('读写文件时解码错误')
# 	print(file)


# for in 逐行读取及readlines 按行读取到一个列表容器
def main():
	file = None
	
	# 读取整个文件
	with open('../res/望海潮-东湖形胜.txt', 'r', encoding='utf-8') as file:
			print(file.read())

	# 逐行读取
	with open('../res/望海潮-东湖形胜.txt', 'r', encoding='utf-8') as file:
		for line in file:
			print(line, end = '')
			time.sleep(0.5)
	print()

	# 按行读取到一个列表容器
	with open('../res/望海潮-东湖形胜.txt', 'r', encoding='utf-8') as file:
		lines = file.readlines()
	print(lines)	


if __name__ == '__main__':
	main()









