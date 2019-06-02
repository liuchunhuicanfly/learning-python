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

#### Apply 函数
```
# mean()

df.apply(np.cumsum) # 数据累加

df.apply(lambda x: x.max() - x.min()) # 计算每列最大值，最小值之差
```

#### 直方图（Histogramming）
```
s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()
```

#### 字符处理（String）
```
# 转化为小写
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()
```

#### 合并（Merge）
```
# 使用 concat() 连接pandas对象 
df = pd.DataFrame(np.random.randn(10, 4))
# 切片
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

# join 合并
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key')
```

#### 添加（Append）
```
# append()
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
s = df.iloc[3]
df.append(s, ignore_index=True) # ignore_index 是否忽略行索引
```

#### 分组（Grouping）
###### 分组常常意味着可能包含以下的几种的操作中一个或多个:
* 依据一些标准分离数据
* 对组单独地应用函数
* 将结果合并到一个数据结构中

```
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
    'foo', 'bar', 'foo', 'foo'],
   'B' : ['one', 'one', 'two', 'three',
    'two', 'two', 'one', 'three'],
   'C' : np.random.randn(8),
   'D' : np.random.randn(8)})

# 对单个分组应用函数，数据被分成了 bar 组与 foo 组，分别计算总和。
df.groupby('A').sum()

# 依据多个列分组会构成一个分级索引
df.groupby(['A','B']).sum()
'''
bar one -1.814470 2.395985
    three -0.595447 0.166599
    two -0.392670 -0.136473
foo one -1.195665 -0.616981
    three 1.928123 -1.623033
    two 2.414034 1.600434
'''
```

#### 形变（Reshaping）
```
#  stack() 压缩列的级别， 将列添加为分级索引

# unstack() 解压dataFrame索引，默认解压最后一级索引
```

#### 透视表（Pivot Tables）
```
# 生成数据透视表
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
   'B' : ['A', 'B', 'C'] * 4,
   'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
   'D' : np.random.randn(12),
   'E' : np.random.randn(12)})
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']) # 选中一列数据进行展示，以其他列分别作为索引和列，
'''
C             bar       foo
A     B
one   A -0.859045 -0.685425
      B -0.642739  0.345685
      C  0.085087  0.749008
three A -1.754995       NaN
      B       NaN -3.274415
      C  0.258929       NaN
two   A       NaN -1.438146
      B -0.716127       NaN
      C       NaN  0.457345
'''
```

#### 时间序列（Time Series）
```
# pandas 拥有既简单又强大的频率变换重新采样功能，下面的例子从 1次/秒 转换到了 1次/5分钟：
rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample('5Min').sum()
'''
2012-01-01    25083
Freq: 5T, dtype: int64
'''

# 本地化时区表示
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
'''
2012-03-06    0.464000
2012-03-07    0.227371
2012-03-08   -0.496922
2012-03-09    0.306389
2012-03-10   -2.290613
Freq: D, dtype: float64
'''

ts_utc = ts.tz_localize('UTC')
'''
2012-03-06 00:00:00+00:00    0.464000
2012-03-07 00:00:00+00:00    0.227371
2012-03-08 00:00:00+00:00   -0.496922
2012-03-09 00:00:00+00:00    0.306389
2012-03-10 00:00:00+00:00   -2.290613
Freq: D, dtype: float64
'''

# 转换为其他时区
ts_utc.tz_convert('US/Eastern')
'''
2012-03-05 19:00:00-05:00    0.464000
2012-03-06 19:00:00-05:00    0.227371
2012-03-07 19:00:00-05:00   -0.496922
2012-03-08 19:00:00-05:00    0.306389
2012-03-09 19:00:00-05:00   -2.290613
Freq: D, dtype: float64
'''

# 转换为时间跨度表示的形式
rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
'''
2012-01-31   -1.134623
2012-02-29   -1.561819
2012-03-31   -0.260838
2012-04-30    0.281957
2012-05-31    1.523962
Freq: M, dtype: float64
'''

# 转换为时间戳
ps = ts.to_period()
# 转换为时间戳
ps.to_timestamp()
```

#### 分类（Categoricals）
```
df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})

# 将 raw_grades 转换成 Categoricals 类型
df["grade"] = df["raw_grade"].astype("category")
'''
0    a
1    b
2    b
3    a
4    a
5    e
Name: grade, dtype: category
Categories (3, object): [a, b, e]
'''

# 重命名分类
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])

# 根据分类的顺序对数据进行排序
df.sort_values(by="grade")
'''
id raw_grade      grade
5   6         e   very bad
1   2         b       good
2   3         b       good
0   1         a  very good
3   4         a  very good
4   5         a  very good
'''
# 根据分类分组计数
df.groupby("grade").size()
'''
grade
very bad     1
bad          0
medium       0
good         2
very good    3
dtype: int64
'''
```

#### 绘图（Plotting）
```
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

```

#### 文件读取和生成（CSV, HDF5, Excel）
```
# 从 csv 文件读取数据
pd.read_csv('foo.csv')

# 保存到 csv 文件
df.to_csv('foo.csv')

# 读取 excel 文件
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])

# 保存到 excel 文件
df.to_excel('foo.xlsx', sheet_name='Sheet1')

# 读取 HDF5
pd.read_hdf('foo.h5','df')

# 保存 HDF5
df.to_hdf('foo.h5','df')
```

##### PS: 更多方法请至官方文档进行查询 
[Pandas](http://pandas.pydata.org/)
[Pandas中文文档](https://www.pypandas.cn)











