from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^about/$',views.about),
    url(r'^contact/$',views.contact),
    url(r'^portfolio/$',views.portfolio),
    url(r'^services/$',views.services),
    url(r'^thankyou/$',views.thankyou)
]
