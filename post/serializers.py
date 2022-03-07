from django.conf import settings
from .models import Comment, Follow, Like, Post
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from json import JSONEncoder
from django.core import serializers as django_serializers


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


UserModel = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField()
    total_comments = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField('get_all_comments')
    likes = serializers.SerializerMethodField('get_all_likes')

    class Meta:
        extra_fields = ["total_likes", "total_comments", "comments", "likes"]
        model = Post
        read_only_fields = ("user_id", )
        fields = ('id', 'user_id', 'title', 'desc',
                  'created_at', *extra_fields)

    def get_total_likes(self, obj):
        return Like.objects.filter(post_id=obj.pk).count()

    def get_all_comments(self, obj):
        return django_serializers.serialize(
            "json", Comment.objects.filter(post_id=obj.pk))

    def get_all_likes(self, obj):

        return django_serializers.serialize(
            "json", Like.objects.filter(post_id=obj.pk))

    def get_total_comments(self, obj):
        return Comment.objects.filter(post_id=obj.pk).count()


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        read_only_fields = ("user_id",)
        fields = ('id', 'user_id', 'follower_id', 'created_at')


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        read_only_fields = ("user_id",)
        fields = ('id', 'user_id', 'post_id', 'input', 'created_at')


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        read_only_fields = ("user_id",)
        fields = ('id', 'user_id', 'post_id', 'created_at')


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    @staticmethod
    def validate_username(username):
        if 'allauth.account' not in settings.INSTALLED_APPS:
            # We don't need to call the all-auth
            # username validator unless its installed
            return username

        from allauth.account.adapter import get_adapter
        username = get_adapter().clean_username(username)
        return username

    class Meta:
        extra_fields = ["followers", "following"]
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)

    def get_followers(self, obj):
        return Follow.objects.filter(follower_id=obj.pk).count()

    def get_following(self, obj):
        return Follow.objects.filter(user_id=obj.pk).count()
