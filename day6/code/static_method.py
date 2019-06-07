# encoding: UTF-8

# staticmethod 静态方法和类方法
# 
from math import sqrt
class Triangle(object):

	def __init__(self, a, b, c):
		self._a = a
		self._b = b
		self._c = c

	@staticmethod
	def is_volid(a, b, c):
		return a + b > c and a + c > b and b + c > a

	def perimate(self):
		return int(self._a + self._b + self._c)

	def area(self):
		half = self.perimate() / 2

		return int(sqrt(half * (half - self._a) * (half - self._b) * (half - self._c)))

def main():
	a, b, c = 3, 4, 5

	# 静态类和类方法都是通过给类发消息来调用的
	if Triangle.is_volid(a, b, c):
		triangle1 = Triangle(a, b, c)

		p = triangle1.perimate()

		area = triangle1.area()

		print(p)
		# 也可以通过给类发消息来调用对象方法，但要传入接收消息的对象作为参数
		print(Triangle.perimate(triangle1))
		print(area)

	else:
		print('不能组成一个三角形')


if __name__ == '__main__':
	main()