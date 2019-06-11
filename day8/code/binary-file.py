# encoding: utf-8


# 读写二进制文件
def main():
	try:
		with open('../res/file-open-mode.png', 'rb') as file:
			data = file.read()
			print(type(data))
			# print(data)
	except FileNotFoundError:
		print('指定文件无法打开')
	except IOError as err:
		print(err)
		print('读写文件时发生错误')

if __name__ == '__main__':
	main()