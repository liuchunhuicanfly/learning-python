# Virtualenv的使用及Flask的安装
#### Virtualenv的使用
    * 创建虚拟环境:   python3 -m venv  venv  | Windows: py -3 -m venv venv
    * 激活虚拟环境：source venv/bin/activate | . venv/bin/activate | Windows: venv\Scripts\activate
    * 退出虚拟环境：deactivate

#### 安装Flask
##### 在已激活的虚拟环境中：
```
pip install Flask
```

##### 运行Flask应用：
```
export FLASK_APP=app.py
flask run | python3 -m flask run
```

#### 路由 
使用route()装饰器来把函数绑定到URL:
```
@app.route(‘/’)
def index():
    return ‘Index Page’
@app.route(‘/hello’)
def hello():
    return ‘Hello, World’
```

#### 变量规则
通过把URL的一部分标记为<variable_name>就可以在URL中添加变量。标记的部分会作为关键字参数传递给函数。
通过使用<converter:variable_name>，就科技选择性的加上一个转换器，为变量指定规则
```
@app.route(‘/user/<username>’)
def show_user_profile(username):
    # show the user profile for that user
    Return ‘User %s’ % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

##### 转换器类型
| 类型 | 描述 |
| ------ | ------ | 
| string |（缺省值）接受任何不包含斜杠的文本 | 
| int | 接受正整数 | 
| path | 类似string，但可以包含斜杠 | 
| uuid | 接受UUID字符串 |

#### 唯一的URL / 重定向行为
###### 以下两条规则的不同之处在于是否使用尾部的斜杠:
* projects 的 URL 是中规中举的，尾部有一个斜杠，看起来就如同一个文件夹。 访问一个没有斜杠结尾的 URL 时 Flask 会自动进行重定向，帮你在尾部加上一个斜杠。
* about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误。这样可以保持 URL 唯一，并帮助 搜索引擎避免重复索引同一页面。
```
@app.router('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```
















