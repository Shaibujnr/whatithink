from django.contrib import admin
from .models import Post,Comment
from redactor.widgets import RedactorEditor
from django.db import models
from django.forms import Textarea,ModelForm

# Register your models here.
class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'content': RedactorEditor(),
    }

class PostModelAdmin(admin.ModelAdmin):
    form = PostModelForm



admin.site.register(Post,PostModelAdmin)

admin.site.register(Comment)
