from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = "myblog"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:post_id>', views.PostView.as_view(), name='post'),
    path('blog/tagline=<slug:tagline>', views.BlogView.as_view(), name='blog'),
    path('archive/<str:month>', views.MonthArchive.as_view(), name='archive')
]