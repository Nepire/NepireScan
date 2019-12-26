from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def home(request):
    return render(request,'dashboard.html')

def tables(request):
    return render(request,'tables.html')
