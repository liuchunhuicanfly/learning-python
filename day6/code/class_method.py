# encoding: UTF-8

# 类方法
# 类方法的第一个参数约定名为cls， 它代表的是当前类相关的信息的对象（类本身也是一个对象，有的地方称之为类的元数据兑现）
# 通过cls参数可以获取和类想相关的信息并且创建出类的对象
from time import time, localtime, sleep
class Clock(object):

	def __init__(self, h = 0, m = 0, s = 0):
		self._h = h
		self._m = m
		self._s = s
	
	@classmethod
	def now(cls):
		ctime = localtime(time())
		print(ctime)
		return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)


	def run(self):
		self._s += 1

		if self._s == 60:
			self._s = 0
			self._m += 1
			if self._m == 60:
				self._m = 0
				self._h += 1
				if self._h == 24:
					self._h = 0

	def show(self):
		return '%02d:%02d:%02d' % (self._h, self._m, self._s)


def main():
	# 通过类方法创建对象并获取当前时间
	clock = Clock.now()
	while True:
		show = clock.show()
		print(show)
		sleep(1)
		clock.run()



if __name__ == '__main__':
	main()