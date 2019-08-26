from datetime import datetime


from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ('male', '男'),
    ('female', '女')
)


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name='昵称', default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=6, verbose_name='性别', choices=GENDER_CHOICES)
    address = models.CharField(max_length=100, verbose_name='地址', default='')
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    image = models.ImageField(upload_to='head_image/%Y/%m/%d', default='default.jpg')

    class Metas:
        verbose_name = '用户信息',
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
