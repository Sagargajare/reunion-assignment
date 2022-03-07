from django.contrib import admin

from post.models import Like, Post, Follow, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)
