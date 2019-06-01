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
一个二维的表格型数据结构, 含有一组有序的列，每列可以是不同的值类型（数值，字符串，布尔值，None, NaN...），DataFrame既有行索引又有列索引，可以将它看做由Series组成的字典。
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
df.T # 行列互换
```

#### 排序（Sorting）
```
df.sort_index(axis=1, ascending=False) # 行列索引进行排序
df.sort_values(by=['B', 'C']) # 通过指定列标签进行值的排序, 可以传入多列排序
```

#### 选取（Selection）
```
df['A'] # 通过列标签选取， 读取的数据类型为Series
df[['A', 'B', 'C']] # 选取多列，读取的数据类型为Dataframe
df[0: 2] # 通过指定行索引范围选取, 选取范围为 0<= index < 2,；边界只存在一个的话代表向前或向后选取所有；
df[[0, 1, 2]] # 选取多行
df[['a':'b']] # 指定行标签选取多行
```

##### loc：通过label（行列名）来选取数据
```
df.loc['a'] # 指定行标签选取单行
df.loc[:,['A','B']] # 指定列标签选取单列或多列
df.loc['a': 'b', ['A','B']]) # 指定多行，多列
df.loc['a',['A','B']] # 指定单行，多列
df.loc[:, :] # 选取所有行列
df.loc['a','A'] # 选取单个值
df.at['a','A'] # 选取单个值，相较于loc更加高效
```

##### iloc: 通过 position（行列位置）来选取数据
```
df.iloc[0] # 选取单行
df.iloc[0:3, 1:3] # 指定范围，选取多行，多列
df.iloc[[1,2,4],[0,2]] # 选取多行，多列
df.iloc[1:3, :] # 指定范围，选取多行
df.iloc[:,1:3] # 指定范围，选取多列
df.iloc[1, 1] # 选取单个值
df.iat[1, 1] # 选取单个值，相较于iloc更加高效
```

#### 布尔值索引（Boolean Indexing）: 
```
df[df.A > 0] # 通过单列的值筛选数据， 返回的数据类型为Dataframe
df[df > 0] # 从整个Dataframe筛选匹配数据，如果布尔条件不存在的话用NaN替换， 返回的数据类型为Dataframe

# 用isin()方法进行筛选
df2 = df.copy()
df2['E'] = ['one','two','three','four']
df2[df2['A'].isin(['one','two'])]
```

#### 列操作 (Setting)
```
# 通过索引添加新列
newSeries = pd.Series(['q', 'w', 'e', 'r'], index=['a', 'b', 'c', 'd'])
df['F'] = newSeries

# 通过标签设置值
df.at['a', 'A'] = 0

# 通过位置属性设置值
df.iat[0, 0] = 0

# 通过分配NumPy数组设置整列
df.loc[:,'A'] = np.array([2] * len(df))

# 设置条件取反
df2 = df.copy()
df2[df2 > 0] = -df2

# 行列加减乘除
df['F'] + 'SSS' # 字符串列可以直接加上字符串，对整列进行操作
df['A'] * 100 # 数字列直接加上或者乘以数字，对整列进行操作
df['A'] * df['B'] # 两列之间可以直接操作

# 新增列
df['G'] = df['F'] + '_ss'
```

#### 空值处理（Missing Data）
```
# 删除空值行
df.dropna(how='any') # 删除带有空值的行
df.dropna(subset=['A', 'B'], how='any') # 在特定的列中判断空值
# all代表全部为空，才会删除该行；any只要一个为空，就删除该行。

# 补全空值
df.fillna(value=5) # 将所有空值赋值为固定的值
df['A'].fillna(value=df['B'], inplace=True) # 将缺失值赋值为其他列的数据

# 找出空值
df.notnull() # 判断是否为空值， <=> notnull()
df[df['A'].notnull()] # 将'A'列为空的行输出
pd.isna(df) # 判断是否为空值， <=> notna()
```

#### 统计函数（statistic）
```
# mean()
df.mean() # 求每列的均值, 自动排除空值
df.mean(1) # 求每行的均值, 自动排除空值
df[['A', 'B']].mean() # 求单列或多列的均值
df[['a', 'b']].mean() # 求单行或多行的均值

# max() 最大值

# min() 最小值

# std() 标准差

# count() 非空数据的数量,

# median() 中位数

# quantile(0.25) # 25%分位数

ps: 传入参数0、1分别显示列，行, 默认为列
```

### PS: 更多方法请至官方文档进行查询 
[Pandas](http://pandas.pydata.org/)
[Pandas中文文档](https://www.pypandas.cn)











