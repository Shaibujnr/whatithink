from django.db import models
import os
from bs4 import BeautifulSoup
from PIL import Image
from whatithink.settings import MEDIA_URL
MEDIA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "media/uploads")


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default="New Post Title", unique=True)
    content = models.TextField(default="New Post Content")
    date_posted = models.DateTimeField(auto_now_add=True)

    @property
    def get_preview_image(self):
        soup = BeautifulSoup(self.content,'html.parser')
        summary_image = soup.find(id='si')
        if not summary_image:
            return MEDIA_URL+"defaults/preview.png"
        image_source = summary_image['src']
        return image_source if summary_image else MEDIA_URL+"defaults/preview.png"

    @property
    def get_summary(self):
        soup = BeautifulSoup(self.content,'html.parser')
        summary_text = soup.find(id="st")
        return summary_text.string if summary_text else "Default Post Summary …"

    def __str__(self):
        return "%s" % self.title

    class Meta:
        get_latest_by = "date_posted"
        ordering = ["-date_posted"]


class Comment(models.Model):
    post = models.ForeignKey(Post)
    message = models.TextField(default="New Post Comment")

    def __str__(self):
        return "%s" % self.message[:15] + "..."
