# ETV_project
 > 微电影网站+app 项目
---
#### 开发环境、服务器环境、项目结构、初始化库表
1. <details><summary>环境</summary>

    服务器系统版本 | CentOs7
    ---|---
    开发语言 | python3
    数据库 | mysql8
    前端 | H5
    后端框架 | flask
    web服务 | nginx
    开发工具 | submite Text3
    虚拟环境 | pipenv  
1. <details><summary>开发工具：sublime Text3</summary>

    1. <details><summary>SublimeLinter集成flake8代码分析</summary>

        ```
        set1. flake8 库
            速度非常快，误报率低，用它来做代码分析检查是非常合适的
            命令行安装 ：pip install flake8
            升级命令： pip install --upgrade flake8
        
        set2. Sublime的代码框架：SublimeLinter
            ST3 -> ctrl+shift+p -> install package -> 输入SublimeLinter并完成安装
        set3. SublimeLinter-flake8
            ST3 -> ctrl+shift+p -> install package -> 输入SublimeLinter-flake8并完成安装
            
        set4. 配置错误下划线提示
            ST3 -> Package Settings -> SublimeLinter
            把左边的默认配置全部拷贝到右边的配置里并把开头的default更改为user
            然后把配置中 "mark_style": "outline",更改为："mark_style":“squiggly_underline”
    2. <details><summary>Anaconda 代码保全</summary>

        ```
        ST3 -> ctrl+shift+p -> install package -> 输入Anaconda并完成安装
        ST3 -> Package Settings -> Anaconda
            {
                "anaconda_linting": false,
                "pep8": false
            }
    3. <details><summary>GitGutter: git插件</summary>

        ```
        ST3 -> ctrl+shift+p -> install package -> 输入GitGutter并完成安装
    4. <details><summary>语法配置</summary>

        ```
        ST3 -> 首选项 -> 特定语法
        配置如下：
        "tab_size": 4, 
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true, 
        "ensure_newline_at_eof_on_save": true,
        "rulers": [ 
        72,
        79
        ],
        "word_wrap": true,
        "wrap_width": 80
1. <details><summary>开发工具2：vscode</summary>

    1. <details><summary>py库</summary>
    
        ```
        MS Python                                # 微软py插件
        vscode-icons                             # py图标
        Bracket Pair Colorizer                   # 括号不同颜色
        Chinese                                  # 中文
        Path Autocomplete                        # 自动路径
        Anaconda Extension Pack                  # 代码提示        filesize package for Visual Studio Code  # 显示文件信息大小
        Guides                                   # 函数、类、的缩进扩展线

    1. <details><summary>html库</summary>
        
        ```
        Beautify                                 # 按F1格式化html编码
        Auto Close Tag                           # 自动补完html结束标签
        Auto Rename Tag                          # 自动重命名配对标签
        CSS Peek                                 # 自动跳转css
        Open-In-Browser                          # 
        HTML Boilerplate                         # html默认模板
        Prettier                                 # js、css格式化代码
1. <details><summary>开发环境（服务器）</summary>

    1. <details><summary>mysql 5.7</summary>

        ```
        # 清除本机上的mysql
        mysql -V  # 查看mysql的版本号 
        apt-get autoremove --purge mysql-server-版本号
        apt-get autoremove mysql-server
        apt-get remove mysql-common
        dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P
        
        # 命令行安装mysql
        sudo apt install mysql-server
        mysql -uroot -p  # 安装完成登录不成功，没有密码
        sudo cat /etc/mysql/debian.cnf
            记录下user和password,再以此用户登录mysql设置root密码;
            user = debian-sys-maint 
            password = MP8GmtoM7s5gsi3w
        mysql -udebian-sys-maint -pMP8GmtoM7s5gsi3w  # 成功进入 mysql
        mysql> use mysql;  # 使用mysql库
        mysql> select host,user,plugin,authentication_string from user;  #root用户的plugin为auth_socket，密码为空
        mysql> update user set plugin="mysql_native_password",authentication_string=password('123456') where user="root";  # 更新root密码为：123456
        mysql> flush privileges;  # 更新数据库
        
        $ mysql -uroot -p123456 # 正常使用；    
    
        mysql: [root, 123456, 3306]  # windows 全自动安装即可
        
        create database moves;    # 手动建立数据库（或写进启动脚本）

    2. <details><summary>pipenv： virturlenv与pip的结合</summary>

        ```
        安装：
            pip insall pipenv
            
        创建env:   project目录 -> pipenv --three
        激活env:   pipenv shell
        退出env:   exit
        
        pipenv 常用cmd: 
            pipenv --where # 项目路径
            pipenv --py # Python位置(配置ST3编译器)
            pipenv install flask # 安装模块,如flask、requests
            pipenv graph  # 查看已安装模块
            
            pipenv run python manage.py #运行项目



    3. <details><summary>pipenv 已安装库</summary>
        
        ```
        pipenv install flask              # flask 库
        pipenv install flask-sqlalchemy   # flask调用sqlalchemy 的ORM库
        pipenv install mysql-connector    # mysql连接模块（pymysql在win10报1136）
        pipenv install Flask-Script       # 外部脚本


    4. <details><summary>dos批处理快捷运行</summary>

        ```
        project目录下建立 auto_run.bat
        doskey r=pipenv run python manage.py  # 按r自动运行项目;更多快捷命令自行设置
        @doskey ls=dir /b $*
        @doskey l=dir /od/p/q/tw $*




    
    5. <details><summary>指定ST3的pipenv编译</summary>
    
        ```
        pipenv --py   # 获取env的py解析器路径
        ST3 -> 新建编译系统：
        {
            "env": {"PYTHONIOENCODING": "utf8"},
            "cmd": ["C:\\Users\\Administrator\\.virtualenvs\\etv-bg-BHlTS\\Scripts\\python.exe", "-u", "$file"],
            "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
            "selector": "source.python"
        }
1. <details><summary>目录结构（蓝图构建）</summary>

        etv                         # 最外层项目目录
        │  autorun.bat             # 快捷bat
        │  manage.py               # 程序入口
        │  Pipfile                 # pipenv的配置文件
        |  Pipfile.lock            # pipenv锁定文件
        │  settings.py             # 配置文件
        |
        └─app                      # 项目app (相当于python的包)
            │  __init__.py         # 项目初始化文件
            │  models.py           # 模型 数据库
            ├─static               # 项目静态资源目录
            ├─admin                # 后台模块
            │      forms.py        # 表单
            │      views.py        # 视图
            │      __init__.py     # 后台初始化
            │
            ├─home                 # 前端模块
            │      forms.py        # 表单
            │      views.py        # 视图
            │      __init__.py     # 前端初始化
            │
            └─templates            # html模板
                ├─admin            # 后台html模板
                └─home             # 前端html模板
1. <details><summary>blueprint蓝图</summary>

    1. <details><summary>构建blueprint: app/admin/__init__.py</summary>

        ```
        #coding:utf8
        from flask import Blueprint
        admin = Blueprint("admin", __name__)
        import app.admin.views  # 导入视图
        
    2. <details><summary>构建blueprint: app/home/__init__.py</summary>

        ```
        #coding:utf8
        from flask import Blueprint
        home = Blueprint("home", __name__)
        import app.home.views  # 导入视图

    3. <details><summary>注册蓝图: app/__init__.py</summary>

        ```
        #coding:utf8
        from flask import Flask  # 用于生成app对象
        from flask_sqlalchemy import SQLAlchemy   # 生成db对象 用于数据库操作
        db = SQLAlchemy() # db对象
        from .models import *  # 引入所有模型（！必须写在db对象之后 ）
        
        app = Flask(__name__)   # 实例app对象 __name__即：app的名称，亦可自定
        app.config.from_object('settings.DevelopmentConfig')     # 使用的配置
        db.init_app(app) # 注册db到app
        
        # 调用蓝图
        from app.home import home as home_buleprint
        from app.admin import admin as admin_blueprint
        app.register_blueprint(home_buleprint)
        app.register_blueprint(admin_blueprint, url_prefix="/admin")  # 注册蓝图 url_prefix: 设置访问前缀
    3. <details><summary>调用蓝图: app/home/views.py</summary>

        ```
        #coding:utf8
        from . import home
        
        @home.route("/")
        def index():
            return "<h1 style='color:green'>This is home page.</h1>"

    4. <details><summary>调用蓝图: app/admin/views.py</summary>

        ```
        #coding:utf8
        from . import admin
        
        @admin.route("/")
        def index():
            return "<h1 style='color:blue'>This is admin page.</h1>"
1. <details><summary>编写入口脚本: /manage.py</summary>
    
    ```
    #coding:utf8
    from app import app
    
    if __name__ == '__main__':
        app.run()
1. <details><summary>运行程序、测试</summary> 
    
    ```shell
    pipenv run python manage.py  # 运行项目
    127.0.0.1:5000               # 在浏览器访问以下两个地址测试
    127.0.0.1:5000/admin/
    
1. <details><summary>配置文件: /settings.py</summary>

    ```python
    #-*-coding: UTF-8 -*-
    import os
    
    
    # mysql连接参数
    MYSQL = {
        'DB': 'movie',
        'USR': 'root',
        'PWD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CHARSET': 'charset=utf8',
        'DB_MODULE': 'mysqlconnector'
        # 'DB_MODULE': 'pymysql'     # 此模块在py3 报1366 更换为 mysql-connector
    }
    
    # 上传文件目录
    UPLOAD_DIR = "app/static/uploads/"
    
    # 超管账号
    USER_ADMIN = {
        'name': 'admin',
        'pwd': '123456'
    }
    # sqlalchemy_mysql 连接语句
    LINK = "mysql+%s://%s:%s@%s:%s/%s?%s" \
        % (MYSQL['DB_MODULE'], MYSQL['USR'], MYSQL['PWD'], MYSQL['HOST'], MYSQL['PORT'], MYSQL['DB'], MYSQL['CHARSET'])
            
    class BaseConfig(object):
        DB = 'movie'  # 数据库需要预先在mysql建立
        SQLALCHEMY_DATABASE_URI = LINK
        SQLALCHEMY_POOL_SIZE = 5
        SQLALCHEMY_POOL_TIMEOUT = 30
        SQLALCHEMY_POOL_RECYCLE = -1
        SECRET_KEY = '9b4f9e04d5fe461a957bac1d47c694a0'    # uuid.uuid4().hex
        UP_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),  UPLOAD_DIR)
        DEBUG = False
    
    
    class ProductionConfig(BaseConfig):
        DEBUG = False
    
    
    class DevelopmentConfig(BaseConfig):       
        DEBUG = True
    
    
    class TestingConfig(BaseConfig):
       DEBUG = False
1. <details><summary>模型：app/models.py</summary>

    ```
    #coding:utf8
    from datetime import datetime
    from . import db

    class Auth(db.Model):
        """权限"""
        __tablename__ = "auth"
        id = db.Column(db.Integer, primary_key=True)  # 编号
        name = db.Column(db.String(100), unique=True)
        url = db.Column(db.String(255), unique=True)   # 可访问的url
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)

        def __repr__(self):
            return "<Auth %r>"%self.name


    class Role(db.Model):
        """角色"""
        __tablename__ = "role"
        id = db.Column(db.Integer, primary_key=True)  # 编号
        name = db.Column(db.String(100), unique=True)
        auths = db.Column(db.String(600))
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)

        def __repr__(self):
            return "<Auth %r>"%self.name


    class Admin(db.Model):
        """管理员"""
        __tablename__ = "admin"
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), unique=True)  # unique 表内唯一
        pwd = db.Column(db.String(100))                 # 密码
        is_super = db.Column(db.SmallInteger)    # 是否为超管  0为超管
        role_id = db.Column(db.Integer, db.ForeignKey('role.id')) # 所属角色
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)

        adminlogs = db.relationship('Adminlog', backref='admin')  # 关联adminlog登录表
        oplogs = db.relationship('Oplog', backref='user')  # 关联oplog操作表

        def __repr__(self):
            return "<Admin %r>" % self.name


    class Adminlog(db.Model):
        """会员登录日志"""
        __tablename__ = "adminlog"
        id = db.Column(db.Integer, primary_key=True)  # 记录的id
        admin_id = db.Column(db.Integer, db.ForeignKey('admin.id')) # 所属会员
        ip = db.Column(db.String(100))  # 登录的IP
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)

        def __repr__(self):
            return "<Adminlog %r>" % self.id


    class Oplog(db.Model):
        """操作日志"""
        __tablename__ = "oplog"
        id = db.Column(db.Integer, primary_key=True)  # 记录的id
        admin_id = db.Column(db.Integer, db.ForeignKey('admin.id')) # 所属会员
        ip = db.Column(db.String(100))  # 登录的IP
        reason =db.Column(db.String(600)) # 操作原因
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)

        def __repr__(self):
            return "<Oplog %r>" % self.id


    class User(db.Model):
        """
        会员
        """
        __tablename__ = 'user'
        id = db.Column(db.Integer, primary_key=True)  # 编号
        name = db.Column(db.String(100), unique=True)  # unique 表内唯一
        email = db.Column(db.String(100), unique=True)  # mail
        phone = db.Column(db.String(11), unique=True)
        face = db.Column(db.String(255), unique=True)   # 头像
        uuid = db.Column(db.String(255), unique=True)   # 唯一标识
        info = db.Column(db.Text)                       # 信息
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)
        pwd = db.Column(db.String(100))                 # 密码

        userlogs = db.relationship('Userlog', backref='user')  # 关联Userlog表
        comments = db.relationship('Comment', backref='user')  # 关联评论表
        moviecols = db.relationship('Moviecol', backref='user')  # 关联评论表

        def __repr__(self):
            return "<User %r>"%self.name


    class Userlog(db.Model):
        """会员登录日志"""
        __tablename__ = "userlog"
        id = db.Column(db.Integer, primary_key=True)  # 记录的id
        user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # 所属会员
        ip = db.Column(db.String(100))  # 登录的IP
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)

        def __repr__(self):
            return "<Userlog %r>" % self.id


    class Tag(db.Model):
        """标签"""
        __tablename__ = "tag"
        id = db.Column(db.Integer, primary_key=True)  # 记录id
        name = db.Column(db.String(100), unique=True) # 标题
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)

        movies = db.relationship("Movie", backref='tag')  # 关联查询 tag表

        def __repr__(self):
            return "<Tag %r>" % self.name


    class Movie(db.Model):
        """电影"""
        __tablename__ = "movie"
        id = db.Column(db.Integer, primary_key=True)  # 记录id
        title = db.Column(db.String(255), unique=True)  # 电影标题
        url = db.Column(db.String(255), unique=True)  # 播放的url
        info = db.Column(db.Text)                       # 简介
        logo = db.Column(db.String(255), unique=True)  # 电影海报
        star = db.Column(db.SmallInteger)              # 电影星级
        playnum = db.Column(db.BigInteger)             # 播放数
        commentnum = db.Column(db.BigInteger)           # 评论数
        tag_id = db.Column(db.Integer, db.ForeignKey('tag.id')) # 所属标签 外联tag表的id值
        area = db.Column(db.String(255))        # 地区
        release_time = db.Column(db.Date)           # 发布时间
        length = db.Column(db.String(100))      # 电影长度
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)

        comments = db.relationship("Comment", backref='movie')  # 评论表的外键
        moviecols = db.relationship("Moviecol", backref='movie')

        def __repr__(self):
            return "<Movie %r>" % self.title


    class Preview(db.Model):
        """上映预告"""
        __tablename__ = "preview"
        id = db.Column(db.Integer, primary_key=True)  # 记录id
        title = db.Column(db.String(255), unique=True)  # 电影标题
        logo = db.Column(db.String(255), unique=True)  # 电影海报
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)

        def __repr__(self):
            return "<Preview %r>" % self.title


    class Comment(db.Model):
        """评论"""
        __tablename__ = 'comment'
        id = db.Column(db.Integer, primary_key=True)  # 记录id
        content = db.Column(db.Text)
        movie_id = db.Column(db.Integer,db.ForeignKey('movie.id'))   # move表的id
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # user表的id
        ctime = db.Column(db.DateTime, index=True, default=datetime.now)

        def __repr__(self):
            return "<Comment %r>" % self.id


    class Moviecol(db.Model):
        """电影收藏"""
        __tablename__ = "moviecol"
        id = db.Column(db.Integer, primary_key=True)  # 记录id
        movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))   # move表的id
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # user表的id

        ctime = db.Column(db.DateTime, index=True, default=datetime.now)
        def __repr__(self):
            return "<Moviecol %r>" % self.id
1. <details><summary>初始化建表脚本：/create_tables.py</summary>
    
    1. 运行时需确定mysql服务运行
    1. 运行初始化需要安装模块：mysql-connector、PyMySQL、flask-sqlalchemy
    2. 需要引用db对象，修改app/__init__.py
    ```python
    from flask_sqlalchemy import SQLAlchemy   # 生成db对象 用于数据库操作
    db = SQLAlchemy() # db对象
    from .models import *  # 引入所有模型（！必须写在db对象之后 ）
    
    app = Flask(__name__)   # 实例app对象 __name__即：app的名称，亦可自定
    app.config.from_object('settings.DevelopmentConfig')     # 使用的配置
    db.init_app(app) # 注册db到app
    ```
    3. /create_tables.py   
    ```python
    #-*-coding: UTF-8 -*-
    import os
    from flask import Flask 
    from app import db
    from app import models # 引入模型（添加角色）
    from werkzeug.security import generate_password_hash  # 生成加密密码
    from sys import exit
    from settings import MYSQL  # setting配置文件中mysql的配置字典
    from settings import USER_ADMIN 


    # 建立app
    def create_app():
        app = Flask(__name__)
        app.config.from_object('settings.DevelopmentConfig')
        db.init_app(app) # 注册db到app
        return app

    # 建库
    def CreateDB():
        print('[create movie db OK!]')
        base_mysql = 'mysql -u' + MYSQL['USR'] +' -p' + MYSQL['PWD'] + ' -e' 
        read_mysql = base_mysql + '"create database IF NOT EXISTS %s;"' % MYSQL['DB']
        os.system(read_mysql)
        

    # 添加角色 （）
    role_admin = models.Role(name='超级管理员', auths='') # 超管 id为1 按插入顺序
    role_vip_user = models.Role(name='VIP会员') # id为 2
    role_user = models.Role(name='普通会员')  # 普通会员 id为3
    # 添加 管理员
    admin_egan = models.Admin(
        name=USER_ADMIN['name'],
        pwd=generate_password_hash(USER_ADMIN['pwd']),
        is_super=0,
        role_id=1
    )

    CreateDB()  # 建库
    app = create_app()  # 实例app
    # 每个操作使用上下文管理进行, 不能在同一个with 中进行

    with app.app_context():   
        db.create_all()  # 建表
        # db.drop_all() # 删表

    # 添加基础角色
    with app.app_context():
        db.session.add_all([
            role_admin,
            role_user,
            role_vip_user,
        ])
        db.session.commit()  # 提交

    # 添加管理员
    with app.app_context():
        db.session.add_all([
            admin_egan
        ])
        db.session.commit()  # 提交
