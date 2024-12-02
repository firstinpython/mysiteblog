from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import file_image
from .validators import random_uuid
# Create your models here.


class UserModel(AbstractUser):
    avatar = models.FileField(upload_to="media",validators=[file_image])


class PostModel(models.Model):
    CHOICES = (
        ('rf','rofl'),
        ('bad','bad'),
        ('gd','good')
    )
    title = models.CharField(verbose_name="title blog",max_length=120,unique=True)
    content = models.TextField(verbose_name="content blog", max_length=300)
    status = models.CharField(max_length=120,choices=CHOICES)
    author = models.ForeignKey(to=UserModel,on_delete=models.CASCADE)
    created_time = models.DateField(auto_now_add=True)
    uid = models.CharField(max_length=10,null=True,unique=True)
    flag_uid = models.CharField(max_length=10, default="True")

    def save(self,*args,**kwargs):
        if self.flag_uid == "True":
            self.uid = random_uuid()
            self.flag_uid = "False"
            super(PostModel,self).save(*args,**kwargs)

    def __str__(self):
        return f"{self.title} | {self.created_time} | {self.uid}"


class CommentsModel(models.Model):
    post_model = models.ForeignKey(to=PostModel, on_delete=models.CASCADE)
    author = models.ForeignKey(to=UserModel,on_delete=models.CASCADE)
    content = models.TextField(verbose_name="content",unique=True)
    created_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} {self.created_time}"

