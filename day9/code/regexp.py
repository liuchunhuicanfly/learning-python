# encoding: utf-8

import re
# 字符串及正则匹配
def main():

	# example1: 验证输入用户名和QQ号是否有效并给出对应的提示信息
	# 要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
	# username = input('username: ') # richard
	# qq = input('qq: ') # 123567
	# valid1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
	# if not valid1:
	# 	print('请输入有效的用户名')
	# valid2 = re.match(r'^[1-9]\d{4,11}$', qq)
	# if not valid2:
	# 	print('请输入有效的QQ号')
	# if valid1 and valid2:
	# 	print(valid1) # <re.Match object; span=(0, 7), match='richard'>
	# 	print(valid2) # <re.Match object; span=(0, 7), match='1234567'>
	# 	print('你输入的信息是有效的!')

	# example2: 提取字符串中的手机号
	# 使用零宽度正回顾后发断言（断言自身出现的位置的后面能匹配表达式exp）和零宽度正预测先行断言（断言自身出现的位置的前面能匹配表达式exp）
	pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
	sentence = '''
	  重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
	  不是15600998765，也是110或119，王大锤的手机号才是15600998765。
		'''
  # 查找所有匹配并保存到一个列表中
	# match_list = re.findall(pattern, sentence)
	# print(match_list) # ['13512346789', '15600998765', '15600998765']

	# 查找字符串所有与正则表达式匹配的模式 返回一个迭代器
	# for item in re.finditer(pattern, sentence):
	#   print(item)
	#   print(item.group())
	"""
  <re.Match object; span=(31, 42), match='13512346789'>
	13512346789
	<re.Match object; span=(53, 64), match='15600998765'>
	15600998765
	<re.Match object; span=(84, 95), match='15600998765'>
	15600998765
	"""

	# 通过search函数指定搜索位置找出所有匹配
	m = re.search(pattern, sentence)
	while m:
		print(m)
		print(m.group())
		m = pattern.search(sentence, m.end())
	"""
	<re.Match object; span=(31, 42), match='13512346789'>
	13512346789
	<re.Match object; span=(53, 64), match='15600998765'>
	15600998765
	<re.Match object; span=(84, 95), match='15600998765'>
	15600998765
	"""

if __name__ == '__main__':
	main()










