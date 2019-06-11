# encoding: utf-8

import requests
import json

# # 写入JSON文件 dict -> JSON Object
# def main():
# 	dict1 = {
#     'name': 'Richard',
#     'age': 26,
#     'qq': 123456789,
#     'friends': ['Jack', 'Rose'],
#     'cars': [
#       {
#       	'band': 'Audi',
#       	'max_speed': 280
#       },
#       {
#       	'brand': 'Benz', 
#       	'max_speed': 320
#       }
#     ]
# 	}

# 	try:
# 		with open('../res/test.json', 'w', encoding = 'utf-8') as file:
# 			json.dump(dict1, file)

# 	except IOError as err:
# 		print(err)
# 		print('写文件时发生错误')

# 	print('保存数据完成')


# Python dict -> JSON String
# def main():
# 	dict1 = {
#     'name': 'Richard',
#     'age': 26,
#     'qq': 123456789,
#     'friends': ['Jack', 'Rose'],
#     'cars': [
#       {
#       	'band': 'Audi',
#       	'max_speed': 280
#       },
#       {
#       	'brand': 'Benz', 
#       	'max_speed': 320
#       }
#     ]
# 	}

# 	try:
# 		with open('../res/test4.txt', 'w', encoding = 'utf-8') as file:
# 			string = json.dumps(dict1)
# 			file.write(string)

# 	except IOError as err:
# 		print(err)
# 		print('写文件时发生错误')

# 	print('保存数据完成')


# JSON Object -> Python dict
# def main():
# 	try:
# 		with open('../res/test.json', 'r', encoding = 'utf-8') as file:
# 			dict1 = json.load(file)
# 			print(dict1)
# 	except IOError as err:
# 		print(err)
# 		print('读取文件时发生错误')

# 	print('数据读取完成')


# JSON String -> Python dict
# def main():
# 	try:
# 		with open('../res/test.json', 'r', encoding = 'utf-8') as file:
# 			data = file.read()
# 			dict1 = json.loads(data)
# 			print(dict1)
# 	except IOError as err:
# 		print(err)
# 		print('读取文件时发生错误')

# 	print('数据读取完成')

# JSON String -> Python dict
def main():
	resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
	dict1 = json.loads(resp.text)
	print(dict1['code'])

if __name__ == '__main__':
	main()










