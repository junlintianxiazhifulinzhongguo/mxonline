from django.db import models


from apps.users.models import BaseModel
from apps.organizations.models import Teacher

DEGREE_CHOICES = (
    ('cj', '初级'),
    ('zj', '中级'),
    ('gj', '高级')
)


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='所属讲师')
    name = models.CharField(max_length=50, verbose_name='课程名称')
    decs = models.CharField(max_length=150, verbose_name='课程简介')
    learn_times = models.BigIntegerField(default=0, verbose_name='学习时长（分钟数）')
    degree = models.CharField(verbose_name='难度', choices=DEGREE_CHOICES, max_length=2)
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    category = models.CharField(default='后端开发', verbose_name='课程类别', max_length=20)
    tag = models.CharField(verbose_name='课程标签', max_length=10, default='')
    youneed_know = models.CharField(verbose_name='课程须知', max_length=300, default='')
    teacher_tell = models.CharField(verbose_name='老师告诉你', max_length=300, default='')

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=50, verbose_name='章节名称')
    learn_times = models.BigIntegerField(default=0, verbose_name='学习时长（分钟数）')

    class Meta:
        verbose_name = '课程章节'
        verbose_name_plural = verbose_name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name='章节', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='视频名称')
    url = models.CharField(max_length=200, verbose_name='访问地址')
    learn_times = models.BigIntegerField(default=0, verbose_name='学习时长（分钟数）')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=50, verbose_name='名称')
    file = models.FileField(max_length=300, upload_to='course/resource/%Y/%m/%d', verbose_name='下载地址')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
