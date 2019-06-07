# encoding: UTF-8

# __slots__
# __slots__变量可以限定自定义类型的对象只能绑定某些属性
# __slots__的限定只对当前类的对象生效，对子类并不起任何作用

class Person(object):

	# 限制Person对象只能绑定_name, _age 和 _gender 属性
	__slots__ = ('_name', '_age', '_gender')

	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def name(self):
		return self._name

	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self, age):
		self._age = age
	

	def play(self):
		if self._age > 18:
			print('%s正在打篮球' % self._name)
		else:
			print('%s正在打羽毛球' % self._name)

def main():
	person = Person('大锤', 23)
	
	person.play()

	print(person.age)

	person.age = 20

	print(person.age)

	person._gender = 'man'

	print(person._gender)

	# person.city = 'chengdu' # 'Person' object has no attribute 'city'
	





if __name__ == '__main__':
	main()