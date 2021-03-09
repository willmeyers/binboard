from rest_framework import routers

from .viewsets import PublicPostsViewSet, UserPostsViewSet

public_posts_router = routers.DefaultRouter()
public_posts_router.register('posts/', PublicPostsViewSet)

user_posts_router = routers.DefaultRouter()
user_posts_router.register('user/posts/', UserPostsViewSet)
