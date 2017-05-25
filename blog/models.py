from django.db import models
import os

MEDIA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"media/uploads")

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100,default="New Post Title",unique=True)
    content = models.TextField(default="New Post Content")
    date_posted = models.DateTimeField(auto_now_add=True)

    @property
    def get_preview_image(self):
        return "/media/uploads/preview.png"
    @property
    def get_summary(self):
        return "Android is a privilege separated operating system, " \
               "i.e. each application in android is separated from another " \
               "through a distinct id, and each application file / data is private " \
               "to that application only. Each Android application is started in its own " \
               "process thus are isolated from all other applications (even from system /" \
               " default applications). As …"


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
