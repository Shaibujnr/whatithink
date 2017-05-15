from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import Context
from . import models
import os


# Create your views here.

def home(request):
    if request.method == 'GET':
        latest_posts = models.Post.objects.all()[0]
        t = get_template('home.html')
        html = t.render({"posts":latest_posts})
        return HttpResponse(html, status=200)


def article(request):
    if request.method == 'GET':
        post = models.Post.objects.all()[0]
        t = get_template('article.html')
        html = t.render({'post':post})
        return HttpResponse(html,status=200)
