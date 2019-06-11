# encoding: utf-8


# 写入文件
def  main():
	filenames = ('test1.txt', 'test2.txt', 'txt3.txt')
	fs_list = []

	try:
		for filename in filenames:
			fs_list.append(open('../res/' + filename, 'w', encoding='utf-8'))

		for num in range(100):
			fs_index = 0
			if num < 30:
				fs_index = 0
			elif num < 60:
				fs_index = 1
			else:
				fs_index = 2
			fs_list[fs_index].write(str(num) + '\n')

	except IOError as err:
		print(err)
		print('写文件时发生错误')

	finally:
		for fs in fs_list:
			fs.close()


if __name__ == '__main__':
	main()