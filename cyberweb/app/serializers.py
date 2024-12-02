from rest_framework.serializers import ModelSerializer
from .models import UserModel, PostModel, CommentsModel


class UserRegistr(ModelSerializer):
    class Meta:
        fields = ("username", "password")
        model = UserModel


class AuthorSerializer(ModelSerializer):
    class Meta:
        fields = ("username", "avatar")
        model = UserModel


class PostListSerializer(ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        fields = ("title", "content", "status", "author")
        model = PostModel


class PostSerializer(ModelSerializer):
    class Meta:
        fields = ("title", "content", "status", "author")
        model = PostModel


class CommentSerializer(ModelSerializer):
    class Meta:
        fields = ("post_model", "author", "content")
        model = CommentsModel

class CommentListSerializer(ModelSerializer):
    class Meta:
        fields = ("author","content")
        model = CommentsModel

