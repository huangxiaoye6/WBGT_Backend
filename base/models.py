from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name='账号',max_length=11, unique=True,null=False,blank=False)
    password=models.CharField(verbose_name='密码',max_length=64,null=False,blank=False)
    uid=models.CharField(verbose_name='用户唯一标识',max_length=64,null=False,blank=False)
    objects = models.Manager()

    class Meta:
        db_table = 'user'

class Content(models.Model):
    title=models.CharField(verbose_name='网页名称',max_length=64,blank=True,null=True)
    imgURL=models.ImageField(verbose_name='图片',upload_to='img',null=True,blank=True)
    class Meta:
        db_table = 'content'