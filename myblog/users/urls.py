from django.urls import path
from .views import MySignUp, MyLoginView, logout_view
from django.conf import settings

app_name = "users"
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('signup/', MySignUp.as_view(), name='signup'),
    path('logout/', logout_view, name='logout')
]