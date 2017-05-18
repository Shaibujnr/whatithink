from django.db import models
import os

MEDIA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100,default="New Post Title",unique=True)
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
