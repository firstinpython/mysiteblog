from django.urls import path
from .views import UserRegistrView,UserProfileView,PostView,PostListView
#
urlpatterns = [
    path("registr",UserRegistrView.as_view()),
    path("profile",UserProfileView.as_view()),
    path("create_post",PostView.as_view()),
    path("list_posts",PostListView.as_view())
    # path("users/"),
    # path("shop/"),
    # path('basket/')
]