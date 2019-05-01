#### 后台管理（逻辑实现）
> 表单设计、逻辑实现、模型读写、访问限制等；
1. <details><summary>管理员登录</summary>

    1. app/_\_init_\_.py中创建db对象

        ```python
        db = SQLAlchemy() # db对象
        ```
    1. app/models.py 中导入db对象

        ```python
        from app import db
        # 或者
        from . import db
        ```
    1. <details><summary>app/models.py的 Admin定义密码验证</summary>

        ```python
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

            def check_pwd(self, pwd):
                from werkzeug.security import check_password_hash
                return check_password_hash(self.pwd, pwd)  
    1. <details><summary>app/admin/forms.py 中定义表单验证</summary>

        ```python
        # 表单模块 pipenv install Flask-WTF  
        # 类型检查包 pipenv install pylint --dev
        # 查看登录界面 需要定义的字段有 account、pwd
        #coding:utf8
        from flask_wtf import FlaskForm
        from wtforms import TextField, PasswordField, SubmitField, validators
        from wtforms.validators import DataRequired, ValidationError
        from app.models import Admin

        class LoginForm(FlaskForm):
            """admin 登录表单 """
            account = TextField(
                label="账号",
                validators=[DataRequired("!")],
                description="描述：账号",
                render_kw={
                    "class": "form-control",
                    "placeholder": "请输入账号！",
                    # "required": "required"  # 添加此项，浏览器会弹出"请填写此字段"
                }
            )
            pwd = PasswordField(
                label="密码",
                validators=[
                    DataRequired("DataRequired: 请输入密码！")
                ],
                description="描述：密码",
                render_kw={
                    "class": "form-control",
                    "placeholder": "请输入密码！",
                    # "required": "required"  
                }
            )
            submit = SubmitField(
                "登录",
                render_kw={
                    "class": "btn btn-primary btn-block btn-flat"
                }
            )

            # 验证账号
            def validate_account(self, field):
                account = field.data
                admin_count = Admin.query.filter_by(name=account).count()
                if admin_count == 0:
                    raise ValidationError("账号不存在！")
        ```
    1. <details><summary>app/templates/admin/login.html 中使用表单字段、信息验证、闪现消息</summary>

        ```html
        <body>
        <!-- 闪现消息 -->
        {% for msg in get_flashed_messages() %} 
        <p class="login-box-msg" style="color:blue">{{ msg }}</p>        
        {% endfor %}
        <form method="POST" id="form-data">
                <!-- form表单及表单err信息 -->
                {{ form.account }}
                {% for err in form.account.errors %}
                <div class="col-md-12">
                    <font style="color:red">{{ err }}</font>
                </div>
                {% endfor %}
                <!-- form表单及表单err信息 -->
                {{ form.pwd }}
                {% for err in form.pwd.errors %}
                <div class="col-md-12">
                    <font style="color:red">{{ err }}</font>
                </div>
                {% endfor %}
                <div class="col-xs-4">
                    <!-- csrf_token必须使用secrte_key -->
                    {{ form.csrf_token }}
                    {{ form.submit }}
                </div>
        ... ...
        </body>
    1. <details><summary>app/admin/views.py中处理登录请求、保存session会话以及访问控制</summary>
        
        1. admin访问控制除了login 登录外，其他全部都要加
        ```python
        #coding:utf8
        from app.admin import admin
        from flask import render_template, redirect, url_for, flash, session, request
        from app.admin.forms import LoginForm
        from app.models import Admin
        from functools import wraps

        # admin访问控制 
        def admin_login_req(func):
            @wraps(func)
            def inner_func(*args, **kwargs):
                if "admin" not in session:    # 判断admin是否在session中
                    return redirect(url_for("admin.login", next=request.url))
                return func(*args, **kwargs)
            return inner_func

        @admin.route("/")
        @admin_login_req                                    # 添加admin访问控制
        def index():
            return render_template("admin/index.html")

        # 登录
        @admin.route("/login/", methods=["GET", "POST"])                     # 访问方法
        def login():
            form = LoginForm()                                               # 实例表单
            if form.validate_on_submit():                                    # 表单的提交 
                data = form.data                                             # 获取表单的值
                admin = Admin.query.filter_by(name=data["account"]).first()  # 根据account的值查询模型Admin
                if admin.check_pwd(data["pwd"]) == False:                    # 调用模型内的check_pwd验证密码  
                    flash("flash:密码错误！", "err")
                    return redirect(url_for("admin.login"))
                session["admin"] = data["account"]                           # 验证成功 保存session会话
                return redirect(url_for("admin.index"))                      # 进入主页
            return render_template("admin/login.html", form=form)

        # 登出 
        @admin.route("/logout/")
        @admin_login_req
        def logout():
            session.pop("admin", None)                   # session中移除admin
            return redirect(url_for("admin.login"))
1. <details><summary>标签管理</summary>

    ```shell
    # macro语言编写的自动生成页码模板（不能使用html注释，使用前删html注释）
    # flash闪现信息： get_flashed_messages(category_filter=["ok"])获取； 可根据"ok"关键字过滤
    # tag_list 通用的列表型读库例子
    ```
    1. <details><summary>建立标签表单 TagForm： app/admin/forms.py</summary>

        ```python
        class TagForm(FlaskForm):
            """标签"""
            name = StringField(
                "标签名称",
                validators=[DataRequired("必须添加标签！")],
                render_kw={"class": "form-control", "placeholder": "请输入标签名称！"}
            )
            submit = SubmitField("提交标签", render_kw={"class": "btn btn-primary"})
    1. <details><summary>添加标签页面</summary>

        1. <details><summary>视图调用表单编写逻辑：app/admin/views.py</summary>

            ```
            # 添加标签
            @admin.route("/tag/add/", methods=["GET", "POST"])
            @admin_login_req
            def tag_add():
                form = TagForm()
                if form.validate_on_submit():
                    data = form.data
                    tag_count = Tag.query.filter_by(name=data["name"]).count()
                    if tag_count == 1:
                        flash("操作失败：标签已存在！", "err")
                        return redirect(url_for("admin.tag_add"))
                    tag = Tag(name = data["name"])
                    db.session.add(tag)
                    db.session.commit()
                    flash("操作成功！", "ok")
                    return redirect(url_for("admin.tag_list", page=1))  # 跳转到标签列表（必须指定page）
                return render_template("admin/tag_add.html", form=form)
        1. <details><summary>前端模板调用form控件:app/templates/admin/tag_add.html</summary>

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
                            <form role="form" method="post">
                                <div class="box-body">
                                    {% for msg in get_flashed_messages(category_filter=["err"]) %}
                                        <div class="alert alert-danger alert-dismissible">
                                            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                            <h4><i class="icon fa fa-ban"></i>{{ msg }}</h4>
                                        </div>    
                                    {% endfor %}
                                    {% for msg in get_flashed_messages(category_filter=["ok"]) %}
                                    <div class="alert alert-danger alert-dismissible">
                                            <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                            <h4><i class="icon fa fa-ban"></i>{{ msg }}</h4>
                                        </div>       
                                    {% endfor %}
                                    <div class="form-group">
                                        <label for="input_name">{{ form.name.label }}</label>
                                        {{ form.name }}
                                        {% for err in form.name.errors %}
                                            <p class="login-box-msg" style="color:blue">{{ err }}</p>        
                                        {% endfor %}
                                    </div>
                                </div>
                                <div class="box-footer">
                                    {{ form.csrf_token }}
                                    {{ form.submit }}
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
    1. <details><summary>标签列表页面</summary>

        1. <details><summary>页码模板(通用): app/templates/ui/page_number.html</summary>

            1. 使用macro语言编写，使用时需要去掉HTML注释，或使用macro语法注释
            ```python
            <!-- macro 语言定义page函数,需求两个参数 -->

            <!-- 调用方法 ： 
                {% import "ui/page_number.html" as pn %}  先引入 并别名pn
                {{ pn.page(page_data, 'admin.tag_list') }} -->

            {% macro page(data, url) -%} 
            <!-- if 判断data是否存在，存在则显示页码 -->
            {% if data %}
            <ul class="pagination pagination-sm no-margin pull-right">
                <!-- 首页参数必定为page=1 -->
                <li><a href="{{ url_for(url, page=1) }}">首页</a></li>

                <!-- 判断是否有上一页面 -->
                {% if data.has_prev %}
                <!-- 使用data.prev_num获取上页页码 -->
                <li><a href="{{ url_for(url, page=data.prev_num) }}">上一页</a></li>
                {% else %}
                <!-- 无上一页，则添加class 不显示 -->
                <li class="disabled"><a href="#">上一页</a></li>
                {% endif %}
                
                <!-- 页码生成器：iter_pages() -->
                {% for v in data.iter_pages() %}
                    <!-- 判断是否当前页，是则calss="active" -->
                    {% if v == data.page %}
                        <li class="active"><a href="#">{{ v }}</a></li>
                    {% else %}
                        <li"><a href="{{ url_for(url, page=v) }}">{{ v }}</a></li>
                    {% endif %}
                {% endfor %}

                <!-- 判断是否有下一页面 -->
                {% if data.has_next %}
                <!-- 使用data.prev_next获取上页页码 -->
                <li><a href="{{ url_for(url, page=data.prev_next) }}">下一页</a></li>
                {% else %}
                <!-- 无上一页，则添加class 不显示 -->
                <li class="disabled"><a href="#">下一页</a></li>
                {% endif %}

                <!-- 尾页参数data.pages 获取最后页码 -->
                <li><a href="{{ url_for(url, page=data.pages) }}">尾页</a></li>
            </ul>
            {% endif %}
            {%- endmacro %}
        1. <details><summary>视图调用表单编写逻辑：app/admin/views.py</summary>
        
            ```python
            # 标签列表
            @admin.route("/tag/list/<int:page>/", methods=["GET"])    # 指定路由规则 整型的page参数
            @admin_login_req
            def tag_list(page=None):
                if page is None: 
                    page = 1
                page_data = Tag.query.order_by(
                    Tag.id                    # 按时间反序：Tag.ctime.desc() 
                ).paginate(page=page, per_page=2)       # 分页数量
                return render_template("admin/tag_list.html", page_data=page_data)
        1. <details><summary>前端模板调用form控件:app/templates/admin/tag_list.html</summary>

            ```html
            {% extends "admin/base.html" %}

            <!-- 导入页码模板并别名为pn -->
            {% import "ui/page_number.html" as pn %}

            {% block content %}
            <!--内容-->
            <section class="content-header">
                    <h1>微电影管理系统</h1>
                    <ol class="breadcrumb">
                        <li><a href="#"><i class="fa fa-dashboard"></i> 标签管理</a></li>
                        <li class="active">标签列表</li>
                    </ol>
                </section>
                <section class="content" id="showcontent">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="box box-primary">
                                <div class="box-header">
                                        {% for msg in get_flashed_messages(category_filter=["ok"]) %}
                                        <div class="alert alert-danger alert-dismissible">
                                                <button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
                                                <h4><i class="icon fa fa-ban"></i>{{ msg }}</h4>
                                            </div>       
                                        {% endfor %}
                                    <h3 class="box-title">标签列表</h3>
                                    <div class="box-tools">
                                        <div class="input-group input-group-sm" style="width: 150px;">
                                            <input type="text" name="table_search" class="form-control pull-right"
                                                placeholder="请输入关键字...">

                                            <div class="input-group-btn">
                                                <button type="submit" class="btn btn-default"><i class="fa fa-search"></i>
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="box-body table-responsive no-padding">
                                    <table class="table table-hover">
                                        <tbody>
                                        <tr>
                                            <th>编号</th>
                                            <th>名称</th>
                                            <th>添加时间</th>
                                            <th>操作事项</th>
                                        </tr>
                                        {% for v in page_data.items %}
                                        <tr>
                                            <td>{{ v.id }}</td>
                                            <td>{{ v.name }}</td>
                                            <td>{{ v.ctime }}</td>
                                            <td>
                                                <a class="label label-success">编辑</a>
                                                &nbsp;
                                                <a class="label label-danger">删除</a>
                                            </td>
                                        </tr>
                                        {% endfor %}
                                        </tbody>
                                    </table>
                                </div>
                                <div class="box-footer clearfix">
                                    {{ pn.page(page_data, 'admin.tag_list') }}
                                </div>
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
                    $("#m-2-2").addClass("active");
                });
            </script>
            {% endblock %}
1. <details><summary>电影管理</summary>

    ```shell
    # 上传文件
    1. <details><summary>建立电影管理表单 MovieForm: app/admin/forms.py</summary>
    1. <details><summary>添加电影</summary>
    1. <details><summary>电影列表</summary>

---
1. <details><summary></summary>
    1. <details><summary>temp</summary>
