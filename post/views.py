from django.db import IntegrityError
from django.shortcuts import render
from post.models import Comment, Follow, Like, Post
from rest_framework.exceptions import APIException
from post.serializers import CommentsSerializer, FollowSerializer, LikeSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=self.request.user)
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()

    def perform_create(self, serializer, url_path='/create'):
        print(self.request.user)
        try:
            serializer.save(user_id=self.request.user)
        except IntegrityError:
            raise  APIException("Already following")
        
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentsSerializer
    queryset = Comment.objects.all()
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user_id=self.request.user)
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user)


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    def perform_create(self, serializer):
        try:
            serializer.save(user_id=self.request.user)
        except IntegrityError:
            raise APIException("Already liked")
    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user)
