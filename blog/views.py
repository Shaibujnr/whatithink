from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import Context
from . import models
import os
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import redirect


# Create your views here.

def home(request):
    if request.method == 'GET':
        return redirect('/blog/latest/')


def latest(request):
    t = get_template('index.html')
    def generate_paginator(page_num, cols, total_num_of_pages):
        quo = page_num // cols
        rm = page_num % cols
        start_from = (cols * quo) if rm else cols * (quo - 1)
        return list(range(1, total_num_of_pages + 1)[start_from:][:cols])

    if request.method == 'GET':
        cols = 5
        posts_per_page = 1
        page_num_requested = request.GET.get('page', 1)
        try:
            page_num_requested = int(page_num_requested)
        except:
            return redirect('/latest/')
        all_posts = models.Post.objects.all()
        paginator = Paginator(all_posts,posts_per_page)
        paginator_generated = generate_paginator(page_num_requested,cols,paginator.num_pages)
        try:
            posts = paginator.page(page_num_requested)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            posts = paginator.page(1)

        html = t.render({'posts':posts,'paginator_generated':paginator_generated})
        return HttpResponse(html,status=200)


def article(request):
    if request.method == 'GET':
        post = models.Post.objects.all()[0]
        t = get_template('article.html')
        html = t.render({'post': post})
        return HttpResponse(html, status=200)
