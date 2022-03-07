from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Follow(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
    follower_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user_id', 'follower_id',)

    def __str__(self):
        return self.follower_id.username
class Comment(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    input = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.input
class Like(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user_id', 'post_id',)

    def __str__(self):
        return self.post_id.title
