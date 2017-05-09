from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20, default="New Post Title")
    content = models.TextField(default="New Post Content")


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField(default="New Post Comment")
