# 引入 Pandas, numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 通过一个列表创建Series，若未指定索引，会默认生成整数型索引
s = pd.Series([1, 2, 3, 4])
"""
0    1
1    2
2    3
3    4
dtype: int64
"""

# 创建时添加索引
s = pd.Series([1, 2, 3, 4],index=['a', 'b', 'c', 'd'])
"""
a    1
b    2
c    3
d    4
dtype: int64
"""

# 通过索引选取Series的单个或多个值
s['a']
# 1

s[['a', 'b']]
"""
a    1
b    2
dtype: int64
"""  


# 创建DataFrame

# 通过一个Numpy数组，行索引和列标签创建Dataframe
df = pd.DataFrame(np.random.randn(4, 4), index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])

"""
  A         B         C         D
a -0.671361 -2.121449 -0.203664 -1.132977
b -1.545713  0.215146  0.960608  0.152678
c -1.607124 -0.112761 -0.205079 -0.348997
d -0.310441  1.776197  1.623719 -0.632825
"""

# 通过一个字典对象创建DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4],
	'B': [1, 2, 3, 4],
	'C': [1, 2, 3, 4],
	'D': [1, 2, 3, 4]}, index=['a', 'b', 'c', 'd'])
"""
   A  B  C  D
a  1  1  1  1
b  2  2  2  2
c  3  3  3  3
d  4  4  4  4
"""

# 查看每列的数据类型
# df.dtypes
"""
A    int64
B    int64
C    int64
D    int64
dtype: object
"""

df.head()
"""
   A  B  C  D
a  1  1  1  1
b  2  2  2  2
c  3  3  3  3
d  4  4  4  4
"""




