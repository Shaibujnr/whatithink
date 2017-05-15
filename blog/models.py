from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20, default="New Post Title")
    content = models.TextField(default="New Post Content")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s"%self.title

    class Meta:
        get_latest_by = "date_posted"
        ordering = ["-date_posted"]


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField(default="New Post Comment")

    def __str__(self):
        return "%s"%self.message[:15]+"..."
