# html模板制作
#### 前台html模板jinja2
> 仅为html模板及页面路由，不涉及数据库读写、表单、逻辑处理、访问限制
1. <details><summary>知识点1：url_for指定静态资源</summary>

    1. 静态资源存放目录为: app/static/
    ```html
    <link rel="shortcut icon" href="{{ url_for("static", filename="base/images/logo.png") }}">
    <link rel="stylesheet" href="{{ url_for("static", filename="base/css/bootstrap.min.css") }}">
1. <details><summary>知识点2：url_for路由</summary>

    1. 路由生成器url_for()跳转到home蓝图模块下的index
    ```html
    <a class="curlink" href="{{ url_for("home.index") }}"><span class="glyphicon glyphicon-film"></span>&nbsp;电影</a>    
1. <details><summary>知识点3： jinja2语法</summary>

    ```python 
    # 父模板: app/templates/home/base.html
    {% block css %}{% endblock %}        # 样式块
    {% include "menu.html" %}            # 公用菜单 
    {% block content %}{% endblock %}    # 内容块
    {% block js %}{% endblock %}         # js脚本块

    # 其他页面继承父模板
    {% extends "home/base.html" %}
    # 按业务需求
    {% block css %}... ...{% endblock %}
    {% block content %}... ...{% endblock %}
    {% block js %}... ...{% endblock %}
1. <details><summary>公用模板 base.html（一般包含header、footer）</summary>

    1. app/templates/home/base.html 包含header、footer、search、nav、js块等
    ```html
    <!doctype html>
    <html lang="zh-CN">
    <head>
        ... ...
        <title>微电影</title>
        <link rel="shortcut icon" href="{{ url_for("static", filename="base/images/logo.png") }}">
        ... ...
        <style>
            .navbar-brand>img {
                display: inline;
            ... ...
        </style>
        {% block css %}{% endblock %}
    </head>
    <body>
    <!--搜索-->
    <a class="btn btn-default" href="{{ url_for("home.search") }}"><span class="glyphicon glyphicon-search"></span>&nbsp;搜索</a>
    <!-- 导航 -->
    <nav>... ..</nav>
    <!--内容-->
    {% block content %}{% endblock %}
    <!--底部-->
    <footer>
    <p>©&nbsp;2017&nbsp;flaskmovie.imooc.com&nbsp;京ICP备 13046642号-2</p>
    </footer>
    <!--底部-->
    <script src="{{ url_for("static", filename="base/js/jquery.min.js") }}"></script>
    ... ...
    </script>
    {% block js %}{% endblock %}
    </body>
    </html>
1. <details><summary>extends继承公用模板</summary>

    1. app/templates/home/login.html 继承base.html的一切元素
    ```html
    {% extends "home/base.html" %}

    {% block content %}
    <form role="form">
        <input id="input_contact" class="form-control input-lg" placeholder="用户名/邮箱/手机号码" name="contact" type="text" autofocus>
        <input id="input_password" class="form-control input-lg" placeholder="密码" name="password" type="password" value="">
        <a href="user.html" class="btn btn-lg btn-success btn-block">登录</a>
    </form>
    {% endblock %}
1. <details><summary>include菜单模板、js块、css块</summary>

    ```html
    {% extends "home/base.html" %}
    {% block css %}
    <style>
    .col-lg-1, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9,
    ... ...
    }
    </style>
    {% endblock %}
    {% block content %}
    {% include "home/user_menu.html" %}
    <div class="col-md-9">
        <div class="panel panel-warning">
            <div class="panel-heading">
                <h3 class="panel-title"><span class="glyphicon glyphicon-map-marker"></span>&nbsp;会员中心</h3>
        ... ...
    </div>
    {% endblock %}
1. <details><summary>iframe内嵌模板的处理</summary>

    1. 跟普通模板同样处理即可
    1. 静态资源需要注意（添加独立文件夹以区分）
1. <details><summary>jwplayer播放器页面play.html</summary>

    1. play继承base.html；内嵌css播放代码；js播放器代码
    1. 其他页面链接播放器 {{ url_for("home.play") }}
    ```html
    {% extends "home/base.html" %}

    {% block css %}
    <!--播放页面-->
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='jwplayer/skins/stormtrooper.css') }}">
    <script type="text/javascript" src="{{ url_for('static', filename='ueditor/ueditor.config.js') }}"></script>
    <script type="text/javascript" src="{{ url_for('static', filename='ueditor/ueditor.all.js') }}"></script>
    <script type="text/javascript" src="{{ url_for('static', filename='ueditor/lang/zh-cn/zh-cn.js') }}"></script>
    <script>
        SyntaxHighlighter.all();
    </script>
    <!--播放页面-->
    <style>
        .col-lg-10,.col-lg-11,.col-lg-12,.col-lg-2,.col-lg-3,.col-lg-4,.col-lg-5,.col-lg-6,.col-lg-7,.col-lg-8,
        .col-lg-9,.col-md-1,.col-md-10,.col-md-11,.col-md-12,.col-md-2,.col-md-3,.col-md-4,.col-md-5,.col-md-6,
        .col-md-7,.col-md-8,.col-md-9,.col-sm-1,.col-sm-10,.col-sm-11,.col-sm-12,.col-sm-2,.col-sm-3,.col-sm-4,
        .col-sm-5,.col-sm-6,.col-sm-7,.col-sm-8,.col-sm-9,.col-xs-1,.col-xs-10,.col-xs-11,.col-xs-12,.col-xs-2,
        .col-xs-3,.col-xs-4,.col-xs-5,.col-xs-6,.col-xs-7,.col-xs-8,.col-xs-9 {
            padding-right: 3px;
            padding-left: 3px;
        }
    </style>
    {% endblock %}
    {% block content %}
    <!--内容-->
    <div class="container" style="margin-top:76px">
        <div class="row">
            ... ...
        </div>
    </div>
    <!--内容-->
    {% endblock %}

    {% block js %}
    <!--播放页面-->
    <script src="{{ url_for('static', filename='jwplayer/jwplayer.js') }}"></script>
    <script>
        var ue = UE.getEditor('input_content', {
            toolbars: [
                ['fullscreen', 'emotion', 'preview', 'link']
            ],
            initialFrameWidth: "100%",
            initialFrameHeight: "100",
        });
    </script>
    <script type="text/javascript">
        jwplayer.key = "P9VTqT/X6TSP4gi/hy1wy23BivBhjdzVjMeOaQ==";
    </script>
    <script type="text/javascript">
        jwplayer("moviecontainer").setup({
            flashplayer: "{{ url_for('static', filename='jwplayer/jwplayer.flash.swf') }}",
            playlist: [{
                file: "{{ url_for('static', filename='video/htpy.mp4') }}",
                title: "环太平洋"
            }],
            modes: [{
                type: "html5"
            }, {
                type: "flash",
                src: "{{ url_for('static', filename='jwplayer/jwplayer.flash.swf') }}"
            }, {
                type: "download"
            }],
            skin: {
                name: "vapor"
            },
            "playlist.position": "left",
            "playlist.size": 400,
            height: 500,
            width: 774,
        });
    </script>
    <!--播放页面-->
    {% endblock %}
1. <details><summary>定义404页面</summary>

    1. 逻辑: 在app/__init__.py中定义整个app的 page_not_found函数
    ```python
    #coding:utf8
    from flask import Flask  # 用于生成app对象
    from flask import render_template  # 渲染404页面
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

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("home/404.html"), 404
    ```
    1. 编写404模板 app/templates/home/404.html
    ```html
    <!doctype html>
    <html lang="zh-cn">
    <head>
        <meta charset="utf-8">
        <title>消失在宇宙星空中的404页面</title>
        <link href="{{ url_for('static', filename='404/404.css') }}" rel="stylesheet" type="text/css">
    </head>
    <body>
    <!-- 代码 开始 -->
    <div class="fullScreen" id="fullScreen">
        <img class="rotating" src="{{ url_for('static', filename='404/spaceman.svg') }}">
        <div class="pagenotfound-text">
            <h1>迷失在太空中！</h1>
            <h2><a href="{{ url_for("home.index") }}">返回首页</a></h2>
        </div>
        <canvas id="canvas2d"></canvas>
    </div>
    <script type="text/javascript" src="{{ url_for('static', filename='404/404.js') }}"></script>
    <!-- 代码 结束 -->
    </body>
    </html>
1. <details><summary>页面路由 app/home/views.py</summary>
    
    1. 知识点：render_template, redirect, url_for
    ```
    @home.route("/login/")   # /login/为浏览器显示的路径
    def login():             # 函数名login为 url_for路由时的模块名
        return render_template("home/login.html")
    ```
    1. app/home/views.py
    ```python
    #coding:utf8
    from app.home import home
    from flask import render_template, redirect, url_for
    
    
    @home.route("/")
    def index():
        return render_template("home/index.html")
    
    @home.route("/login/")
    def login():
        return render_template("home/login.html")
    
    @home.route("/logout/")
    def logout():
        return redirect(url_for("home.login"))
    
    @home.route("/register/")
    def register():
        return render_template("home/register.html")
    
    @home.route("/user/")
    def user():
        return render_template("home/user.html")
    
    @home.route("/pwd/")
    def pwd():
        return render_template("home/pwd.html")
    
    @home.route("/comments/")
    def comments():
        return render_template("home/comments.html")
    
    @home.route("/loginlog/")
    def loginlog():
        return render_template("home/loginlog.html")
    
    @home.route("/moviecol/")
    def moviecol():
        return render_template("home/moviecol.html")
    
    @home.route("/search/")
    def search():
        return render_template("home/search.html")
    
    @home.route("/animation/")
    def animation():
        return render_template("home/animation.html")
    
    @home.route("/play/")
    def play():
        return render_template("home/play.html")
---
#### 后台html模板jinja2
> 仅为html模板及页面路由，不涉及数据库读写、表单、逻辑处理、访问限制
1. <details><summary>jinja2语法</summary>

    ```python 
    # 父模板: app/templates/admin/base.html
    {% block css %}{% endblock %}        # 样式块
    {% include "menu.html" %}            # 公用菜单 
    {% block content %}{% endblock %}    # 内容块
    {% block js %}{% endblock %}         # js脚本块

    # 其他页面继承父模板
    {% extends "admin/base.html" %}
    # 按业务需求
    {% block css %}... ...{% endblock %}
    {% block content %}... ...{% endblock %}
    {% block js %}... ...{% endblock %}
1. <details><summary>公用布局模板</summary>

    1. 父模板: app/templates/admin/base.html
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>ETV管理系统</title>
        <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
        <link rel="shortcut icon" href="{{ url_for('static', filename='base/images/logo.png') }}">
        <link rel="stylesheet" href="{{ url_for('static', filename='admin/bootstrap/css/bootstrap.min.css') }}">
        ... ...
        <style>... ...</style>
        {% block css %}{% endblock %}
    </head>
    <body class="hold-transition skin-blue sidebar-mini">
    <!-- 公用部分代码 -->
                {% include "admin/menu.html" %}        
            </section>
        </aside>
        <div class="content-wrapper">
                {% block content %}{% endblock %}
        </div>
        <footer class="main-footer">
            ... ...
            <strong>版权 &copy; 2017-2018 归<a href="">xxx</a>.</strong> 所有
        </footer>
    </div>
    <script src="{{ url_for('static', filename='admin/plugins/jQuery/jQuery-2.2.0.min.js') }}"></script>
    ... ...
    {% block js %}{% endblock %}
    </body>
    </html>
1. <details><summary>子模板index继承base.html</summary>

    1. app/templates/admin/index.html
    ```html
    {% extends "admin/base.html" %}

    {% block css %}

    {% endblock %}

    {% block content %}
    <!--内容-->
    <section class="content-header">
        <h1>微电影管理系统</h1>
        <ol class="breadcrumb">
            <li><a href="#"><i class="fa fa-dashboard"></i> 首页</a></li>
            <li class="active">控制面板</li>
        </ol>
    </section>
    <section class="content" id="showcontent">
        <div class="row">
            <div class="col-md-6">
                <div class="box box-primary">
                    <div class="box-header with-border">
                        <h3 class="box-title">内存使用率</h3>
                    </div>
                    <div class="box-body" id="meminfo" style="height:600px;"></div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="box box-primary">
                    <div class="box-header with-border">
                        <h3 class="box-title">系统设置</h3>
                    </div>
                    <form role="form">
                        <div class="box-body" style="height:600px;">
                            <div class="form-group">
                                <label for="input_speed">限制速率大小</label>
                                <input type="text" class="form-control" id="input_speed" placeholder="请输入限制速率！" value="512">
                            </div>
                            <div class="form-group">
                                <label for="input_mem">限制内存大小</label>
                                <input type="text" class="form-control" id="input_mem" placeholder="请输入限制内存！" value="10m">
                            </div>
                            <div class="form-group">
                                <label for="input_num">限制客户端数量</label>
                                <input type="text" class="form-control" id="input_num" placeholder="请输入限制客户端数量！" value="4">
                            </div>
                            <div class="form-group">
                                <button type="submit" class="btn btn-primary">保存并重启服务</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
    <!--内容-->
    {% endblock %}

    {% block js %}
    <script src="{{ url_for('static', filename='js/echarts.min.js') }}"></script>
    <script>
        var myChart = echarts.init(document.getElementById('meminfo'));
        option = {
            backgroundColor: "white",
            tooltip: {
                formatter: "{a} <br/>{b} : {c}%"
            },
            toolbox: {
                feature: {
                    restore: {},
                    saveAsImage: {}
                }
            },
            series: [{
                name: '内存使用率',
                type: 'gauge',
                detail: {
                    formatter: '{value}%'
                },
                data: [{
                    value: 50,
                    name: '内存使用率'
                }]
            }]
        };
        setInterval(function () {
            option.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0;
            myChart.setOption(option, true);
        },2000);

    </script>
    {% endblock %}
1. <details><summary>菜单模板Active激活样式</summary>

    1. <details><summary>menu.html模板： 根据业务为选中的菜单编上id   m-1  m-1-1</summary>

        ```html
        <ul class="sidebar-menu">
            <li class="header">管理菜单</li>
            <li class="treeview" id="m-1">
                <a href="{{ url_for("admin.index") }}">
                    <i class="fa fa-home" aria-hidden="true"></i>
                    <span>首页</span>
                    <span class="label label-primary pull-right">1</span>
                </a>
                <ul class="treeview-menu">
                    <li id="m-1-1">
                        <a href="{{ url_for("admin.index") }}">
                            <i class="fa fa-circle-o"></i> 控制面板
                        </a>
                    </li>
                </ul>
            </li>
            <li class="treeview" id="m-2">
                <a href="#">
                    <i class="fa fa-tags" aria-hidden="true"></i>
                    <span>标签管理</span>
                    <span class="label label-primary pull-right">2</span>
                </a>
                <ul class="treeview-menu">
                    <li id="m-2-1">
                        <a href="tag_add.html">
                            <i class="fa fa-circle-o"></i> 添加标签
                        </a>
                    </li>
                    <li id="m-2-2">
                        <a href="tag_list.html">
                            <i class="fa fa-circle-o"></i> 标签列表
                        </a>
                    </li>
                </ul>
            </li>
            ... ...
            <li class="treeview" id="m-11">
                <a href="#">
                    <i class="fa fa-user-circle" aria-hidden="true"></i>
                    <span>管理员管理</span>
                    <span class="label label-primary pull-right">2</span>
                </a>
                <ul class="treeview-menu">
                    <li id="m-11-1">
                        <a href="admin_add.html">
                            <i class="fa fa-circle-o"></i> 添加管理员
                        </a>
                    </li>
                    <li id="m-11-2">
                        <a href="admin_list.html">
                            <i class="fa fa-circle-o"></i> 管理员列表
                        </a>
                    </li>
                </ul>
            </li>
        </ul>
        ```
    1. <details><summary>每个调用菜单的子模板都根据自己的id添加js 代码实现active样式</summary>

        ```html
        {% extends "admin/base.html" %}

        {% block content %}
        <!--内容-->
        <section class="content-header">
            <h1>微电影管理系统</h1>
            <ol class="breadcrumb">
                <li><a href="#"><i class="fa fa-dashboard"></i> 标签管理</a></li>
                <li class="active">添加标签</li>
            </ol>
        </section>
        <section class="content" id="showcontent">
            <div class="row">
                <div class="col-md-12">
                    <div class="box box-primary">
                        <div class="box-header with-border">
                            <h3 class="box-title">添加标签</h3>
                        </div>
                        <form role="form">
                            <div class="box-body">
                                <div class="form-group">
                                    <label for="input_name">标签名称</label>
                                    <input type="text" class="form-control" id="input_name" placeholder="请输入标签名称！">
                                </div>
                            </div>
                            <div class="box-footer">
                                <button type="submit" class="btn btn-primary">添加</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </section>
        <!--内容-->
        {% endblock %}
        {% block js %}
        <script>
            $(document).ready(function () {
                $("#m-2").addClass("active");
                $("#m-2-1").addClass("active");
            });
        </script>
        {% endblock %}
1. <details><summary>管理后台页面路由</summary>

    1. app/admin/views.py
    ```python
    #coding:utf8
    from app.admin import admin
    from flask import render_template, redirect, url_for


    @admin.route("/")
    def index():
        return render_template("admin/index.html")

    # 登录
    @admin.route("/login/")
    def login():
        return render_template("admin/login.html")

    # 登出 
    @admin.route("/logout/")
    def logout():
        return redirect(url_for("admin.login"))

    # 添加标签
    @admin.route("/tag/add/")
    def tag_add():
        return render_template("admin/tag_add.html")

    # 标签列表
    @admin.route("/tag/list/")
    def tag_list():
        return render_template("admin/tag_list.html")

    # 添加标签
    @admin.route("/movie/add/")
    def movie_add():
        return render_template("admin/movie_add.html")

    # 标签列表
    @admin.route("/movie/list/")
    def movie_list():
        return render_template("admin/movie_list.html")

    # 添加预告
    @admin.route("/preview/add/")
    def preview_add():
        return render_template("admin/preview_add.html")

    # 预告列表
    @admin.route("/preview/list/")
    def preview_list():
        return render_template("admin/preview_list.html")

    # 用户列表
    @admin.route("/user/list/")
    def user_list():
        return render_template("admin/user_list.html")

    # 查看用户
    @admin.route("/user/view/")
    def user_view():
        return render_template("admin/user_view.html")

    # 评论列表
    @admin.route("/comments/list/")
    def comment_list():
        return render_template("admin/comments.html")

    # 评论列表
    @admin.route("/moviecol/list/")
    def moviecol_list():
        return render_template("admin/moviecol_list.html")

    # 操作日志列表
    @admin.route("/oplog/list/")
    def oplog_list():
        return render_template("admin/oplog_list.html")

    # admin登录日志列表
    @admin.route("/adminloginlog/list/")
    def adminloginlog_list():
        return render_template("admin/adminloginlog_list.html")

    # user会员登录 日志列表
    @admin.route("/userloginlog/list/")
    def userloginlog_list():
        return render_template("admin/userloginlog_list.html")

    # 权限添加
    @admin.route("/auth/add/")
    def auth_add():
        return render_template("admin/auth_add.html")

    # 权限列表
    @admin.route("/auth/list/")
    def auth_list():
        return render_template("admin/auth_list.html")

    # 角色添加
    @admin.route("/role/add/")
    def role_add():
        return render_template("admin/role_add.html")

    # 角色列表
    @admin.route("/role/list/")
    def role_list():
        return render_template("admin/role_list.html")

    # 管理员添加
    @admin.route("/admin/add/")
    def admin_add():
        return render_template("admin/admin_add.html")

    # 管理员列表
    @admin.route("/admin/list/")
    def admin_list():
        return render_template("admin/admin_list.html")



