# encoding: UTF-8

def fab(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n += 1

for n in fab(5):
	print(n)

'''
打印：
1
1
2
3
5
'''
f = fab(5)
next(f) # 1
next(f) # 1
next(f) # 2
next(f) # 3
next(f) # 5
next(f) # StopIteration:

'''
一个带有 yield 的函数就是一个 generator，
它和普通函数不同，生成一个 generator 看起来像函数调用，
但不会执行任何函数代码，直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，
并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，
每次中断都会通过 yield 返回当前的迭代值。
'''


if __name == '__main__':
	main()






