from django.shortcuts import render
from django.http import HttpResponse

def view1(request):
    return HttpResponse("HI! I'M THE FIRST VIEW!")

def view2(request):
    return HttpResponse("HI! I'M THE SECOND VIEW!")