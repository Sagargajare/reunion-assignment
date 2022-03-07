from rest_framework.routers import DefaultRouter

from post.serializers import LikeSerializer
from .views import CommentViewSet, FollowViewSet, LikeViewSet, PostViewSet
from django.urls import path, re_path, include
router = DefaultRouter()
router.register("post", PostViewSet, basename="post")
router.register("follow", FollowViewSet, basename="follow")
router.register("comment", CommentViewSet, basename="comment")
router.register("like", LikeViewSet, basename="like")
urlpatterns = [
    path("", include(router.urls)),
    path("all_post/", PostViewSet.as_view({'get': 'list'})),
]
