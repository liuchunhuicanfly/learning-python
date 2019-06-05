# encoding: UTF-8

# 在屏幕上显示跑马灯文字

import os
import time

def main():
	content = '我爱你.................'
	while True:
		# 清理屏幕输出
		os.system('clear')

		print(content)

		# sleep 200s
		time.sleep(0.3)

		content = content[1:] + content[0]

if __name__ == '__main__':
	main()
	