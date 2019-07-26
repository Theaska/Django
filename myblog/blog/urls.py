from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^view1/', views.view1, name='view1'),
    path('view2/', views.view2, name='view2'),
]