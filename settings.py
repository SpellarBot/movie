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
    SQLALCHEMY_TRACK_MODIFICATIONS = False
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