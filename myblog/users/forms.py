from allauth.account.forms import LoginForm, SignupForm
from allauth.socialaccount import forms
from django import forms as django_forms

class MyLoginForm(LoginForm):
    def login(self, request, redirect_url=None):
        return super().login(request, redirect_url=redirect_url)

class MySignupForm(SignupForm):
    def save(self, request):
        user = super(MySignupForm, self).save(request)
        return user

class MySocialSignupForm(forms.SignupForm):
    def save(self):
        user = super(MySocialSignupForm, self).save()
        return user



