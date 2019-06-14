# encoding: utf-8

from threading import currentThread, Thread, Lock
from time import time, sleep
from random import randint

# def download_task(filename):
# 	print('线程 %s 开始下载%s...' % (currentThread().name, filename))
# 	time_to_download = randint(5, 10)
# 	sleep(time_to_download)
# 	print('线程 %s 下载完成! 耗费了%d秒' % (currentThread().name, time_to_download))

# 单线程
# def main():
# 	start_time = time()
# 	print('线程 %s is running...' % currentThread().name)
# 	t = Thread(target = download_task, args = ('test1.txt',), name = 'DownloadThread')
# 	t.start()
# 	t.join()
# 	end_time = time()
# 	print('线程 %s ended. 共耗时 %.2f' % (currentThread().name, end_time - start_time))
"""
线程 MainThread is running...
线程 DownloadThread 开始下载test1.txt...
线程 DownloadThread 下载完成! 耗费了8秒
线程 MainThread ended. 共耗时 8.00
"""

# 多线程
# def main():
# 	start_time = time()
# 	print('线程 %s is running...' % currentThread().name)
# 	t1 = Thread(target = download_task, args = ('test1.txt',), name = 'DownloadThread1')
# 	t1.start()
# 	t2 = Thread(target = download_task, args = ('test2.txt',), name = 'DownloadThread2')
# 	t2.start()
# 	t1.join()
# 	t2.join()
# 	end_time = time()
# 	print('线程 %s ended. 共耗时 %.2f' % (currentThread().name, end_time - start_time))
"""
线程 MainThread is running...
线程 DownloadThread1 开始下载test1.txt...
线程 DownloadThread2 开始下载test2.txt...
线程 DownloadThread1 下载完成! 耗费了6秒
线程 DownloadThread2 下载完成! 耗费了8秒
线程 MainThread ended. 共耗时 8.00
"""

# 使用继承创建线程
# class DownloadTask(Thread):
# 	def __init__(self, filename, threadname):
# 		super().__init__()
# 		self._filename = filename
# 		self._name = threadname

# 	def run(self):
# 		print('线程 %s 开始下载%s...' % (currentThread().name, self._filename))
# 		time_to_download = randint(5, 10)
# 		sleep(time_to_download)
# 		print('线程 %s 下载完成! 耗费了%d秒' % (currentThread().name, time_to_download))

# def main():
# 	start_time = time()
# 	print('线程 %s is running...' % currentThread().name)
# 	t1 = DownloadTask('test1.txt', 'DownloadThread1')
# 	t1.start()
# 	t2 = DownloadTask('test2.txt', 'DownloadThread2')
# 	t2.start()
# 	t1.join()
# 	t2.join()
# 	end_time = time()
# 	print('线程 %s ended. 共耗时 %.2f' % (currentThread().name, end_time - start_time))
"""
线程 MainThread is running...
线程 DownloadThread1 开始下载test1.txt...
线程 DownloadThread2 开始下载test2.txt...
线程 DownloadThread1 下载完成! 耗费了5秒
线程 DownloadThread2 下载完成! 耗费了9秒
线程 MainThread ended. 共耗时 9.00
"""

# Lock

class Account(object):
	"""docstring for Account"""
	# 无锁
	# def __init__(self):
	# 	super(Account, self).__init__()
	# 	self._balance = 0

	# def deposit(self, money):
	# 	new_balance = self._balance + money
	# 	sleep(0.1)
	# 	self._balance = new_balance
	
	# 有锁
	def __init__(self):
		super(Account, self).__init__()
		self._balance = 0
		self._lock = Lock()

	def deposit(self, money):
		# 先获取锁才能执行后续的代码
		self._lock.acquire()
		try: 
			new_balance = self._balance + money
			sleep(0.01)
			self._balance = new_balance
		finally:
			# 在finally中执行释放锁的操作保证正常异常锁都能释放
			self._lock.release()


	@property
	def balance(self):
		return self._balance
	
class AddMoneyThread(Thread):
	def __init__(self, name, account, money):
		super().__init__()
		self._name = name
		self._account = account
		self._money = money

	def run(self):
		print('线程%s running...' % currentThread().name)
		self._account.deposit(self._money)
		


def main():
	start_time = time()
	account = Account()
	threads = []
	for _ in range(1000):
		t = AddMoneyThread('Thread%s' % str(_ + 1), account, 1)
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

	end_time = time()
	print('共耗时: %.2f' % (end_time - start_time))
	print('账户余额为： %d元' % account.balance)
"""
无锁
线程Thread1 running...
线程Thread2 running...
....
线程Thread999 running...
线程Thread1000 running...
共耗时: 0.20
账户余额为： 1元

有锁
线程Thread1 running...
线程Thread2 running...
....
线程Thread999 running...
线程Thread1000 running...
共耗时: 11.68
账户余额为： 1000元
"""

if __name__ == '__main__':
	main()












