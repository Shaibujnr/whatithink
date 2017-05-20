from django.contrib import admin
from whatithink.adminsite import myAdminSite
from .models import Post,Comment
from redactor.widgets import RedactorEditor
from django.forms import ModelForm




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


myAdminSite.register(Post,PostModelAdmin)
myAdminSite.register(Comment)

