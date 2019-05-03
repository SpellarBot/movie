#coding:utf8
from flask_wtf import FlaskForm
from wtforms import TimeField, StringField, PasswordField, SubmitField, FileField, validators, SelectField, TextAreaField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin, Tag


tags = Tag.query.all()
class MovieForm(FlaskForm):
    """电影管理"""
    title = StringField("片名", validators=[DataRequired()], render_kw={
        "class": "form-control", "placeholder": "片名"
    })
    url = FileField("选择视频文件", 
        validators=[FileRequired(), FileAllowed(['avi', 'mp4', 'flv', '视频文件！'])])
    info = TextAreaField("简介", validators=[DataRequired()], 
        render_kw={"class": "form-control", "placeholder": "简介", "rows": 10})
    logo = FileField("选择封面", validators=[FileRequired(), FileAllowed(['jpg', 'png', '图片仅限 ！'])],)
    star = SelectField(
        "星级", choices=[(1,"1星"), (2,"2星"), (3,"3星"), (4,"4星"), (5,"5星"), (6,"6星")],
        coerce=int, render_kw={"class": "form-control" ,"placeholder": "请选择星级！"}
    )
    tag_id = SelectField("标签", coerce=int, render_kw={"class": "form-control"},
        choices=[(v.id, v.name) for v in tags]
    )
    area = StringField("地区", validators=[DataRequired()], render_kw={
        "class": "form-control", "placeholder": "请填写地区！"
    })
    length = StringField("时长", validators=[DataRequired()], render_kw={
        "class": "form-control", "placeholder": "请填写时长！"
    })
    release_time = TimeField("上映时间", validators=[DataRequired()], render_kw={
        "class": "form-control", "placeholder": "请选择上映时间！", "id": "input_release_time"
    })
    submit = SubmitField("提交", render_kw={"class": "btn btn-primary"})



class TagForm(FlaskForm):
    """标签"""
    name = StringField("标签名称", validators=[DataRequired("必须添加标签！")], 
        render_kw={"class": "form-control", "placeholder": "请输入标签名称！"
    })
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
    submit = SubmitField("登录", render_kw={"class": "btn btn-primary btn-block btn-flat"})

    # 验证账号
    def validate_account(self, field):
        account = field.data
        admin_count = Admin.query.filter_by(name=account).count()
        if admin_count == 0:
            raise ValidationError("账号不存在！")
        