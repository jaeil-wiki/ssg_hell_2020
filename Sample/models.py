from django.db import models

# Create your models here.
from django.db.models import Model, CharField, DateTimeField
from django.utils.datetime_safe import datetime


class Post(Model):
    title = CharField(verbose_name='제목', max_length=50)
    content = CharField(verbose_name='내용', max_length=1000)
    author = CharField(verbose_name='작성자', max_length=20)
    created_at = DateTimeField(verbose_name='작성일자', default=datetime.now)
