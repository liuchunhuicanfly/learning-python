# 列表的生成语法
import sys

def main():
  f = [x for x in range(1, 10)]
  print(f) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

  f = [x + y for x in 'ABCDE' for y in '1234567']
  print(f) # ['A1','A2','A3','A4','A5','A6','A7','B1','B2','B3','B4','B5','B6','B7','C1','C2','C3','C4','C5','C6','C7','D1','D2','D3','D4','D5','D6','D7','E1','E2','E3','E4','E5','E6','E7']

  # 用列表的生成表达式语法创建列表容器
  # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
  f = [x ** 2 for x in range(1, 1000)]
  print(sys.getsizeof(f)) # 9024
  print(f) # ......

  # 请注意下面的代码创建的不是一个列表而是一个生成器对象
  # 通过生成器可以获取到数据但它不占用额外的空间存储数据
  # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
  f = (x ** 2 for x in range(1, 1000))
  print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间 120
  for x in f:
    print(x)


if __name__ == '__main__':
  main()


