#coding:utf8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin

class TagForm(FlaskForm):
    """标签"""
    name = StringField(
        "标签名称",
        validators=[DataRequired("必须添加标签！")],
        render_kw={"class": "form-control", "placeholder": "请输入标签名称！"}
    )
    submit = SubmitField("提交标签", render_kw={"class": "btn btn-primary"})

class LoginForm(FlaskForm):
    """admin 登录表单 """
    account = StringField(
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
        