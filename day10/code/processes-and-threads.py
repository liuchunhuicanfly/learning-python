# encoding: utf-8

from multiprocessing import Process, Pool, Queue
from os import getpid
from random import randint, random
from time import time, sleep


# 使用多进程与不使用多进程对比

# 不使用多进程
# def download_task(filename):
# 	print('开始下载%s...' % filename)
# 	time_to_download = randint(5, 10)
# 	sleep(time_to_download)
# 	print('%s下载完成! 耗时%d秒' % (filename, time_to_download))

# def main():
# 	start_time = time()
# 	download_task('test1.txt')
# 	download_task('test2.txt')
# 	end_time = time()
# 	print('总共耗时%.2f秒' % (end_time - start_time))
"""
开始下载test1...
test1下载完成! 耗时9秒
开始下载test2...
test2下载完成! 耗时7秒
总共耗时16.00秒
"""

# 使用多进程
# def download_task(filename):
# 	print('启动下载进程，进程号[%d].' % getpid())
# 	print('开始下载%s...' % filename)
# 	time_to_download = randint(5, 10)
# 	sleep(time_to_download)
# 	print('%s下载完成! 耗时%d秒' % (filename, time_to_download))

# def main():
# 	start_time = time()
# 	process_1 = Process(target=download_task, args=('test1.txt',))
# 	启动进程
# 	process_1.start()
# 	process_2 = Process(target=download_task, args=('test2.txt',))
# 	process_2.start()
# 	等待进程执行结束
# 	process_1.join()
# 	process_2.join()
# 	end_time = time()
# 	print('总共耗时%.2f秒' % (end_time - start_time))
"""
启动下载进程，进程号[6102].
开始下载test1.txt...
启动下载进程，进程号[6103].
开始下载test2.txt...
test1.txt下载完成! 耗时7秒
test2.txt下载完成! 耗时9秒
总共耗时9.01秒
"""

# 进程池(Pool)
# def download_task(filename):
# 	print('启动下载进程，进程号[%d].' % getpid())
# 	print('开始下载%s...' % filename)
# 	time_to_download = randint(5, 10)
# 	sleep(time_to_download)
# 	print('%s下载完成! 耗时%d秒' % (filename, time_to_download))

# def main():
# 	start_time = time()
# 	pool_list = Pool(4)
# 	for filename in ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'test5.txt']:
# 		pool_list.apply_async(download_task, args=(filename,))
# 	# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
# 	pool_list.close()
# 	pool_list.join()
# 	end_time = time()
# 	print('总共耗时%.2f秒' % (end_time - start_time))
"""
启动下载进程，进程号[6231].
开始下载test1.txt...
启动下载进程，进程号[6232].
开始下载test2.txt...
启动下载进程，进程号[6233].
开始下载test3.txt...
启动下载进程，进程号[6234].
开始下载test4.txt...
test2.txt下载完成! 耗时5秒
启动下载进程，进程号[6232].
开始下载test5.txt...
test1.txt下载完成! 耗时6秒
test4.txt下载完成! 耗时9秒
test3.txt下载完成! 耗时10秒
test5.txt下载完成! 耗时5秒
总共耗时10.05秒
"""

# 进程间通信
def write(q):
	print('Process to write: [%d]' % getpid())
	for val in ['A', 'B', 'C']:
		print('Put %s to queue...' % val)
		q.put(val)
		sleep(randint(5, 10))

def read(q):
	print('Process to read: [%d]' % getpid())
	while True:
		value = q.get(True)
		print('Get %s form queue.' % value)

def main():
	start_time = time()
	# 创建Queue
	q = Queue()
	process_write = Process(target=write, args=(q,))
	process_read = Process(target=read, args=(q,))
	# 启动写入进程
	process_write.start()
	# 启动读取进程
	process_read.start()

	process_write.join()
	process_read.terminate()
	end_time = time()
	print('总共耗时%.2f秒' % (end_time - start_time))

if __name__ == '__main__':
	main()










