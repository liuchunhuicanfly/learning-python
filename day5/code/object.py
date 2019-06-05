# encoding: UTf-8

# 定义类

class Student(object):

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def study(self, course_name):
		print('%s 正在学习 %s.' % (self.name, course_name))

	def is_adult(self, *arg):
		if self.age > 18:
			print('%s成年了' % self.name)
		else:
			print('%s还未成年' % self.name)


# 在Python中，属性和方法的访问权限只有两种，
# 也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
# 但是，Python并没有从语法上严格保证私有属性或方法的私密性，它只是给私有的属性和方法换了一个名字来“妨碍”对它们的访问
class Test(object):
	def __init__(self, foo):
		self.__foo = foo

	def __bar(self):
		print(self.__foo)
		print('__bar')


def main():
	stu1 = Student('jack', 12)
	stu2 = Student('rose', 19)

	stu1.study('math')
	stu2.study('english')

	stu1.is_adult()
	stu2.is_adult()

	test1 = Test('hello')
	# test1.__bar() # AttributeError: 'Test' object has no attribute '__bar'
	# print(test1.__foo) # AttributeError: 'Test' object has no attribute '__foo'
	test2 = Test('hello')
	test2._Test__bar()
	print(test2._Test__foo)





if __name__ == '__main__':
	main()