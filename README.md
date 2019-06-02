# Python及数据分析学习大纲

## Python 语言基础

### 函数和模块的使用
* 函数的作用 - 代码的坏味道 / 用函数封装功能模块
* 定义函数 - def语句 / 函数名 / 参数列表 / return语句 / 调用自定义函数
* 调用函数 - Python内置函数 / 导入模块和函数
* 函数的参数 - 默认参数 / 可变参数 / 关键字参数 / 命名关键字参数
* 函数的返回值 - 没有返回值 / 返回单个值 / 返回多个值
* 作用域问题 - 局部作用域 / 嵌套作用域 / 全局作用域 / 内置作用域 / 和作用域相关的关键字
* 用模块管理函数 - 模块的概念 / 用自定义模块管理函数 /命名冲突的时候会怎样（同一个模块和不同的模块）

### 字符串和常用数据结构
* 字符串的使用 - 计算长度 / 下标运算 / 切片 / 常用方法
* 列表基本用法 - 定义列表 / 用下表访问元素 / 下标越界 / 添加元素 / 删除元素 / 修改元素 /
* 切片 / 循环遍历
* 列表常用操作 - 连接 / 复制(复制元素和复制数组) / 长度 / 排序 / 倒转 / 查找
* 生成列表 - 使用range创建数字列表 / 生成表达式 / 生成器
* 元组的使用 - 定义元组 / 使用元组中的值 / 修改元组变量 / 元组和列表转换
* 集合基本用法 - 集合和列表的区别 / 创建集合 / 添加元素 / 删除元素 / 清空
* 集合常用操作 - 交集 / 并集 / 差集 / 对称差 / 子集 / 超集
* 字典的基本用法 - 字典的特点 / 创建字典 / 添加元素 / 删除元素 / 取值 / 清空
* 字典常用操作 - keys()方法 / values()方法 / items()方法 / setdefault()方法

### 面向对象
* 类和对象 - 什么是类 / 什么是对象 / 面向对象其他相关概念
* 定义类 - 基本结构 / 属性和方法 / 构造器 / 析构器 / __str__方法
* 使用对象 - 创建对象 / 给对象发消息
* 面向对象的四大支柱 - 抽象 / 封装 / 继承 / 多态
* 基础练习 - 定义学生类 / 定义时钟类 / 定义图形类 / 定义汽车类
* 属性 - 类属性 / 实例属性 / 属性访问器 / 属性修改器 / 属性删除器 / 使用__slots__
* 类中的方法 - 实例方法 / 类方法 / 静态方法
* 运算符重载 - __add__ / __sub__ / __or__ /__getitem__ / __setitem__ / __len__ / __repr__ / __gt__ / __lt__ / __le__ / __ge__ / __eq__ / __ne__ / __contains__
* 类(的对象)之间的关系 - 关联 / 继承 / 依赖
* 继承和多态 - 什么是继承 / 继承的语法 / 调用父类方法 / 方法重写 / 类型判定 / 多重继承 / 
* 菱形继承(钻石继承)和C3算法
* 综合案例 - 工资结算系统 / 图书自动折扣系统 / 自定义分数类

### 文件和异常
* 读文件 - 读取整个文件 / 逐行读取 / 文件路径
* 写文件 - 覆盖写入 / 追加写入 / 文本文件 / 二进制文件
* 异常处理 - 异常机制的重要性 / try-except代码块 / else代码块 / finally代码块 /
* 内置异常类型 / 异常栈 / raise语句
* 数据持久化 - CSV文件概述 / csv模块的应用 / JSON数据格式 / json模块的应用

### 字符串和正则表达式
* 字符串高级操作 - 转义字符 \ 原始字符串 \ 多行字符串 \ in和 not in运算符 \ is开头的方法 \ join和split方法 \ strip相关方法 \ pyperclip模块 \ 不变字符串和可变字符串 \ * StringIO的使用
* 正则表达式入门 - 正则表达式的作用 \ 元字符 \ 转义 \ 量词 \ 分组 \ 零宽断言 \贪婪匹配与惰性匹配懒惰 \ 使用re模块实现正则表达式操作（匹配、搜索、替换、捕获）
* 使用正则表达式 - re模块 \ compile函数 \ group和groups方法 \ match方法 \ search方法 \ * findall和finditer方法 \ sub和subn方法 \ split方法
* 应用案例 - 使用正则表达式验证输入的字符串

### 网络应用开发
* 访问网络API - 网络API概述 / 访问URL / requests模块 / 解析JSON格式数据
* 文件传输 - FTP协议 / ftplib模块 / 交互式FTP应用
* 电子邮件 - SMTP协议 / POP3协议 / IMAP协议 / smtplib模块 / poplib模块 / imaplib模块
* 短信服务 - twilio模块 / 国内的短信服务

### 图像和文档处理
* 用Pillow处理图片 - 图片读写 / 图片合成 / 几何变换 / 色彩转换 / 滤镜效果
* 读写Word文档 - 文本内容的处理 / 段落 / 页眉和页脚 / 样式的处理
* 读写Excel文件 - xlrd模块 / xlwt模块
* 生成PDF文件 - pypdf2模块 / reportlab模块

## Python语言进阶

* 常用数据结构
* 函数的高级用法 - “一等公民” / 高阶函数 / Lambda函数 / 作用域和闭包 / 装饰器
* 面向对象高级知识 - “三大支柱” / 类与类之间的关系 / 垃圾回收 / 魔术属性和方法 / 混入 /
* 元类 / 面向对象设计原则 / GoF设计模式
* 迭代器和生成器 - 相关魔术方法 / 创建生成器的两种方式 /
* 并发和异步编程 - 多线程 / 多进程 / 异步IO / async和await

## 数据库基础&进阶

### 关系型数据库-Mysql
* 关系型数据库概述
    * MySQL的安装和使用
    * SQL的使用
    * DDL - 数据定义语言 - create / drop / alter
    * DML - 数据操作语言 - insert / delete / update / select
    * DCL - 数据控制语言 - grant / revoke
* 相关知识
    * 范式理论 - 设计二维表的指导思想
    * 数据完整性
    * 数据一致性
* 在Python中操作MySQL

### NoSQL
* NoSQL概述
* Redis概述
* Mongo概述

## Flask实战
* Flask入门
* 模板的使用
* 表单的处理
* 数据库操作
* 项目实战

## Django实战
* 快速上手
    * Web应用工作原理和HTTP协议
    * Django框架概述
    * 5分钟快速上手
    * 使用视图模板
* 深入模型
    * 关系型数据库配置
    * 管理后台的使用
    * 使用ORM完成对模型的CRUD操作
    * Django模型最佳实践
    * 模型定义参考
* 静态资源和Ajax请求
    * 加载静态资源
    * 用Ajax请求获取数据
* 表单的应用
    * 表单和表单控件
    * 跨站请求伪造和CSRF令牌
    * Form和ModelForm
    * 表单验证
* Cookie和Session
    * 实现用户跟踪
    * cookie和session的关系
    * Django框架对session的支持
    * 视图函数中的cookie读写操作
* 中间件的应用
    * 什么是中间件
    * Django框架内置的中间件
    * 自定义中间件及其应用场景
* 日志和调试
    * 配置日志
    * 配置和使用Django-Debug-Toolbar
* 文件上传和富文本编辑
    * 文件上传表单控件和图片文件预览
    * 服务器端如何处理上传的文件
    * 富文本编辑器概述
    * wangEditor的使用
* 文件下载和报表
    * 通过HttpResponse修改响应头
    * 使用StreamingHttpResponse处理大文件
    * 使用xlwt生成Excel报表
    * 使用reportlab生成PDF报表
    * 使用ECharts生成前端图表
* RESTful架构和DRF入门
* RESTful架构和DRF进阶
* 使用缓存
    * 网站优化第一定律
    * 在Django项目中使用Redis提供缓存服务
    * 在视图函数中读写缓存
    * 使用装饰器实现页面缓存
    * 为数据接口提供缓存服务
* 短信和邮件
    * 常用短信网关平台介绍
    * 使用螺丝帽发送短信
    * Django框架对邮件服务的支持
* 异步任务和定时任务
    * 网站优化第二定律
    * 配置消息队列服务
    * 在项目中使用celery实现任务异步化
    * 在项目中使用celery实现定时任务
* 单元测试和项目上线
    * Python中的单元测试
    * Django框架对单元测试的支持
    * 使用版本控制系统
    * 配置和使用uWSGI
    * 动静分离和Nginx配置
    * 配置HTTPS

## 数据处理和机器学习
* 机器学习基础
* Pandas的应用
    * 数据加载、存储与文件格式
    * 数据清洗和准备
    * 数据规整：聚合、合并和重塑
    * 绘图和可视化
    * 数据聚合与分组运算
    * 时间序列
* NumPy和SciPy的应用
* Matplotlib和数据可视化
* k最近邻(KNN)分类
* 决策树
* 贝叶斯分类
* 支持向量机(SVM)
* K-均值聚类
* 回归分析
* 大数据分析入门
* Tensorflow入门










