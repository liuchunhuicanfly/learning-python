# Pandas

pandas是一个开源的，BSD许可的库， 为Python编程提供高性能，易于使用的数据结构和数据分析工具

### IPython (python 交互shell) 安装
```
pip install ipython
```

### Pandas模块 安装

```
pip install pandas
```

### Pandas、 numpy(多维数组矢量运算库)、matplotlib（2D绘图库） 模块引入
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

### Pandas 的数据类型
Pandas 基于两种数据类型： Series 和 DataFrame

#### Series
一个一维的数据类型，它由一位数组及与之相关的索引组成；
Series的字符串表现形式为：索引在左，值在右；
如果创建时未指定索引，那么pandas会自动创建一个默认的由0开始的整数型索引;
```
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
```

#### DataFrame
一个二维的表格型数据结构, 含有一组有序的列，每列可以是不同的值类型（数值，字符串，布尔值，None...），DataFrame既有行索引又有列索引，可以将它看做由Series组成的字典。
```
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
```


### 常用操作

#### 查看 (View)
```
df.dtypes() # 查看每列的数据类型
df.head(n) # 查看前n行的数据，默认n=5
df.tail(n) # 查看最后n行的数据， 默认n=5
df.index # 返回每一行的索引
df.columns # 返回每列的列标签
df.values # 返回dataFrame的所有数据
df.describe() # 返回每行数据简要的统计分析，如：数量，平均值，标准差，最小值，最大值
```

#### 转置（Transposing）
```
df.T
```

#### 排序（Sorting）
```
df.sort_index(axis=1, ascending=False) # 行列索引进行排序
df.sort_values(by=['B', 'C']) # 通过指定列标签进行值的排序, 可以传入多列排序
```

#### 选择（Selection）














