#coding:utf8
from app.admin import admin
from flask import render_template, redirect, url_for, flash, session, request
from app.admin.forms import LoginForm, TagForm
from app.models import Admin, Tag
from functools import wraps
from app import db

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

# 添加电影
@admin.route("/movie/add/")
@admin_login_req
def movie_add():
    return render_template("admin/movie_add.html")

# 电影列表
@admin.route("/movie/list/")
@admin_login_req
def movie_list():
    return render_template("admin/movie_list.html")

# 添加预告
@admin.route("/preview/add/")
@admin_login_req
def preview_add():
    return render_template("admin/preview_add.html")

# 预告列表
@admin.route("/preview/list/")
@admin_login_req
def preview_list():
    return render_template("admin/preview_list.html")

# 用户列表
@admin.route("/user/list/")
@admin_login_req
def user_list():
    return render_template("admin/user_list.html")

# 查看用户
@admin.route("/user/view/")
@admin_login_req
def user_view():
    return render_template("admin/user_view.html")

# 评论列表
@admin.route("/comments/list/")
@admin_login_req
def comment_list():
    return render_template("admin/comments.html")

# 评论列表
@admin.route("/moviecol/list/")
@admin_login_req
def moviecol_list():
    return render_template("admin/moviecol_list.html")

# 操作日志列表
@admin.route("/oplog/list/")
@admin_login_req
def oplog_list():
    return render_template("admin/oplog_list.html")

# admin登录日志列表
@admin.route("/adminloginlog/list/")
@admin_login_req
def adminloginlog_list():
    return render_template("admin/adminloginlog_list.html")

# user会员登录 日志列表
@admin.route("/userloginlog/list/")
@admin_login_req
def userloginlog_list():
    return render_template("admin/userloginlog_list.html")

# 权限添加
@admin.route("/auth/add/")
@admin_login_req
def auth_add():
    return render_template("admin/auth_add.html")

# 权限列表
@admin.route("/auth/list/")
@admin_login_req
def auth_list():
    return render_template("admin/auth_list.html")

# 角色添加
@admin.route("/role/add/")
@admin_login_req
def role_add():
    return render_template("admin/role_add.html")

# 角色列表
@admin.route("/role/list/")
@admin_login_req
def role_list():
    return render_template("admin/role_list.html")

# 管理员添加
@admin.route("/admin/add/")
@admin_login_req
def admin_add():
    return render_template("admin/admin_add.html")

# 管理员列表
@admin.route("/admin/list/")
@admin_login_req
def admin_list():
    return render_template("admin/admin_list.html")