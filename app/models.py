#coding:utf8
from datetime import datetime
from app import db

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

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)          # 哈希工具密码对比 相同返回true


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