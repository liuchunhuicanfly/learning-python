# encoding: UTF-8
# 继承和多态

from abc import ABCMeta, abstractmethod

"""
在已有类的基础上创建新类，其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，从而减少重复代码的编写。
提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以子类比父类拥有的更多的能力，在实际开发中，我们经常会用子类对象去替换掉一个父类对象
"""
class Person(object):
	"""docstring for Person"""
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
		print('%s正在快乐的玩耍' % self._name)

	def watch_movie(self):
		if self._age > 18:
			print('%s正在看电影' % self._name)
		else:
			print('%s正在看动画片' % self._name)


class Student(Person):
	"""docstring for Student"""
	def __init__(self, name, age, grade):
		super().__init__(name, age)
		self._grade = grade

	@property
	def grade(self):
		return self._grade

	@grade.setter
	def grade(self, grade):
		self._grade = grade

	def study(self, course):
		print('%s正在学习%s' % (self._name, course))


class Teacher(Person):
	"""docstring for Teacher"""
	def __init__(self, name, age, title):
		super().__init__(name, age)
		self._title = title

	@property
	def title(self):
		return self._title
	
	@title.setter
	def title(self, title):
		self._title = title

	def tech(self, course):
		print('%s%s正在讲%s' % (self._name, self._title, course))

"""
重写：子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本
多态：通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为
"""

"""
抽象类
抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它
如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）
"""
class Pet(object, metaclass=ABCMeta):
	"""docstring for Pet"""
	def __init__(self, nickname):
		self._nickname = nickname

	@abstractmethod
	def make_voice(self):
		pass

class Dog(Pet):
	"""docstring for Dog"""
	def make_voice(self):
		print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
	"""docstring for Cat"""
	def make_voice(self):
		print('%s: 喵喵喵...' % self._nickname)
		

def main():
	# student1 = Student('Jack', 12, '初一')
	# teacher1 = Teacher('Rose', 30, '教授')

	# student1.study('Math')
	# teacher1.tech('English')
	
	pets = [Dog('小白'), Cat('阿黄')]
	for pet in pets:
		pet.make_voice()



if __name__ == '__main__':
	main()














