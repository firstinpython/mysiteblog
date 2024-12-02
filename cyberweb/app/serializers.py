from rest_framework.serializers import ModelSerializer
from .models import UserModel, PostModel


class UserRegistr(ModelSerializer):
    class Meta:
        fields = ("username", "password")
        model = UserModel


class AuthorSerializer(ModelSerializer):
    class Meta:
        fields = ("username", "avatar")
        model = UserModel


class PostSerializer(ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        fields = ("title", "content", "status", "author")
        model = PostModel
