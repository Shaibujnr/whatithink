from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^latest/$',views.latest),
    url(r'^article/$', views.article)
]
