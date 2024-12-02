from django.contrib import admin
from .models import UserModel,PostModel, CommentsModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(PostModel)
admin.site.register(CommentsModel)