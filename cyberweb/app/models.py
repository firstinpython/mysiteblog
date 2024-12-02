from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import file_image
# Create your models here.


class UserModel(AbstractUser):
    avatar = models.FileField(upload_to="media",validators=[file_image])


class PostModel(models.Model):
    CHOICES = (
        ('rf','rofl'),
        ('bad','bad'),
        ('gd','good')
    )
    title = models.CharField(verbose_name="title blog",max_length=120)
    content = models.TextField(verbose_name="content blog", max_length=300)
    status = models.CharField(max_length=120,choices=CHOICES)
    author = models.ForeignKey(to=UserModel,on_delete=models.CASCADE)
    created_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.created_time}"