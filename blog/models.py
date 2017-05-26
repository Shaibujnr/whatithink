from django.db import models
import os
from bs4 import BeautifulSoup
from PIL import Image

MEDIA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "media/uploads")


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default="New Post Title", unique=True)
    content = models.TextField(default="New Post Content")
    date_posted = models.DateTimeField(auto_now_add=True)

    @property
    def get_preview_image(self):
        def resize_image(img,size,img_name):
            im2 = img.resize(size,Image.ANTIALIAS)
            im2.save(img_name,quality=90)

        soup = BeautifulSoup(self.content,'html.parser')
        summary_image = soup.find(id='si')
        if not summary_image:
            return "/media/defaults/preview.png"
        image_source = summary_image['src']
        image_file = os.path.join(MEDIA_PATH,image_source.split('/')[-1])
        im1 = Image.open(image_file)
        w,h = im1.size
        pw,ph = 700,300
        if w != pw and h != ph:
            resize_image(im1,(pw,ph),image_file)
        return image_source if summary_image else "/media/defaults/preview.png"

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
