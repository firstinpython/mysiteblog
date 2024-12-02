from django.urls import path
from .views import UserRegistrView,UserProfileView,PostView,PostListView,CommentsView,CommentsListView
#
urlpatterns = [
    path("registr",UserRegistrView.as_view()),
    path("profile",UserProfileView.as_view()),
    path("create_post",PostView.as_view()),
    path("list_posts",PostListView.as_view()),
    path("create_comment",CommentsView.as_view()),
    path("list_comments/<str:post_url>",CommentsListView.as_view())
    # path("users/"),
    # path("shop/"),
    # path('basket/')
]