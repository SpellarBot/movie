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