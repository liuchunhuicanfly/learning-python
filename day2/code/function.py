# 定义函数
#def function_name(): 
	# 函数块
	# 
	# 
	# 
	#	return

# 参数使用默认值
def add(num=2):
    total = 0
    total += num
    return total

# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total



# 用模块管理函数
'''
Python中每个文件就代表了一个模块（module），
我们在不同的模块中可以有同名的函数，
在使用函数的时候我们通过import关键字导入指定的模块就可以区分到底要使用的是哪个模块中的foo函数
'''



# 模块除了定义函数之外还中有可以执行代码
def foo():
    pass

def bar():
    pass

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()


# global关键字 指示全局变量
# nonlocal关键字 指示变量来自于嵌套作用域









