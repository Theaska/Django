from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = "myblog"
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    url(r'^(?P<blog_tag>[A-Za-z0-9-]+)$', views.blog, name='blog'),
    url(r'^archive/(?P<month>[A-Za-z]+)$', views.archive, name='archive')
]