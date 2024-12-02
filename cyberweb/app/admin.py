from django.contrib import admin
from .models import UserModel,PostModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(PostModel)