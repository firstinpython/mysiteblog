from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, UpdateAPIView, RetrieveAPIView
from .serializers import UserRegistr, PostSerializer, PostListSerializer, CommentSerializer,CommentListSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel, PostModel, CommentsModel


# Create your views here.


class UserRegistrView(APIView):
    def post(self, request):
        serializer = UserRegistr(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserProfileView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserRegistr


class PostView(CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostListView(ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializer


class CommentsView(APIView):
    queryset = PostModel.objects.all()
    serializer_class = CommentSerializer


class CommentsListView(APIView):
    def get(self, post_url):
        post = PostModel.objects.filter(uid=post_url).first()
        comments = CommentsModel.objects.get(post_model=post)
        serializer = CommentListSerializer(comments)
        return Response(serializer.data)