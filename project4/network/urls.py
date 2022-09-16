
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("makePost", views.makePost, name='makePost'),
    path('getPosts', views.getPosts, name='getPosts'),
    path('getUserPosts/<str:username>', views.getUserPosts),
    path('following', views.following, name='following'),
    path('getFollowing', views.getFollowing, name='getFollowing'),
    path('<str:username>/follow', views.follow, name='follow'),
    path('<str:username>/unfollow', views.unfollow, name='unfollow'),
    path('<str:username>', views.profile, name='profile'),
    path('<int:id>/edit', views.editPost, name='editPost'),
    path('<int:id>/like', views.likePost, name='likePost'),
    path('<int:id>/dislike', views.dislikePost, name='dislikePost'),
    path('<int:id>/isLiked', views.isLiked, name='isLiked'),
]
