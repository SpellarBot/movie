#coding:utf8
from flask_wtf import FlaskForm
from wtforms import TimeField, StringField, PasswordField, SubmitField, FileField, validators, SelectField, TextAreaField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import DataRequired, ValidationError
from app.models import Admin, Tag


class PreviewForm(FlaskForm):
    """预告管理表单"""
    title = StringField(
        "预告标题",
        validators=[DataRequired("请输入预告标题！")],
        render_kw={"class": "form-control", "id": "input_title", "placeholder": "请输入片名！"}
    )
    logo = FileField("预告封面", validators=[DataRequired("请输入预告封面!")])
    submit = SubmitField("提交预告", render_kw={"class": "btn btn-primary"})

tags = Tag.query.all()
class MovieForm(FlaskForm):
    """电影管理表单"""
    title = StringField(
        label="片名",
        validators=[DataRequired("请输入片名！")],
        description="片名",
        render_kw={"class": "form-control", "id": "input_title", "placeholder": "请输入片名！"})

    url = FileField(
        label="文件",
        validators=[FileRequired("请选择文件！")],
        # validators=[DataRequired("请选择文件！")],
        description="文件"
    )

    info = TextAreaField(
        label="简介",
        validators=[
            DataRequired("请输入简介！")
        ],
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": "10",
            "id": "input_info"
        }
    )

    logo = FileField(
        label="封面",
        validators=[
            DataRequired("请上传电影封面!")
        ],
        description="封面",

    )

    star = SelectField(
        label="星级",
        validators=[
            DataRequired("请选择星级!")
        ],
        description="星级",
        coerce=int,
        choices=[(1,"1星"), (2,"2星"), (3,"3星"), (4,"4星"), (5,"5星")],
        render_kw={
            "class": "form-control",
            "id": "input_star"
        }
    )

    area = StringField(
        label="地区",
        validators=[
            DataRequired("请输入地区!")
        ],
        description="地区",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入地区！"
        }
    )

    tag_id = SelectField(
        label="标签",
        validators=[
            DataRequired("请选择标签!")
        ],
        description="标签",
        coerce=int,
        choices=[(v.id, v.name) for v in tags],  
        render_kw={
            "class": "form-control"
        }
    )

    length = StringField(
        label="片长",
        validators=[
            DataRequired("请输入片长!")
        ],
        description="片长",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入片长！"
        }
    )

    release_time = StringField(
        label="上映时间",
        validators=[
            DataRequired("请选择上映时间!")
        ],
        description="上映时间",
        render_kw={
            "class": "form-control",
            "placeholder": "请选择上映时间！",
            "id": "input_release_time"
        }
    )

    submit = SubmitField(
        '提交',
        render_kw={
            "class": "btn btn-primary",  # 前端样式 
        }
    )

# class MovieForm(FlaskForm):
#     """电影管理"""
#     title = StringField("片名", validators=[DataRequired()], render_kw={
#         "class": "form-control", "placeholder": "片名"
#     })
#     url = FileField("选择视频文件", 
#         validators=[FileRequired(), FileAllowed(['avi', 'mp4', 'flv', '视频文件！'])])
#     info = TextAreaField("简介", validators=[DataRequired()], 
#         render_kw={"class": "form-control", "placeholder": "简介", "rows": 10})
#     logo = FileField("选择封面", validators=[FileRequired(), FileAllowed(['jpg', 'png', '图片仅限 ！'])],)
#     star = SelectField(
#         "星级", choices=[(1,"1星"), (2,"2星"), (3,"3星"), (4,"4星"), (5,"5星"), (6,"6星")],
#         coerce=int, render_kw={"class": "form-control" ,"placeholder": "请选择星级！"}
#     )
#     tag_id = SelectField("标签", coerce=int, render_kw={"class": "form-control"},
#         choices=[(v.id, v.name) for v in tags]
#     )
#     area = StringField("地区", validators=[DataRequired()], render_kw={
#         "class": "form-control", "placeholder": "请填写地区！"
#     })
#     length = StringField("时长", validators=[DataRequired()], render_kw={
#         "class": "form-control", "placeholder": "请填写时长！"
#     })
#     release_time = TimeField("上映时间", validators=[DataRequired()], render_kw={
#         "class": "form-control", "placeholder": "请选择上映时间！", "id": "input_release_time"
#     })
#     submit = SubmitField("提交", render_kw={"class": "btn btn-primary"})



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
        