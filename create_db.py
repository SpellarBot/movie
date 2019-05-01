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