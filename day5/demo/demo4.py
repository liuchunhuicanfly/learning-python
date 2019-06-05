# encoding: UTF-8

# 设计一个函数返回传入的列表中最大和第二大的元素的值。


def get_max(arr = [21, 234135, 34234, 3242, 211, 876, 4475, 5534]):

  length = len(arr)
  m1 = 0
  m2 = 0

  if length >= 2:
    m1, m2 = (arr[0], arr[1]) if arr[0] > arr[1] else (arr[1], arr[0])
    for index in range(2, len(arr)):
      if arr[index] > m1:
        m2 = m1
        m1 = arr[index]
      elif arr[index] > m2:
        m2 = arr[index]  
  elif length >= 1:
    m1 = arr[0]

  print(m1, m2, sep='\n')

if __name__ == '__main__':
	get_max()
	