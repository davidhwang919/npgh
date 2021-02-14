from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'main/home.htm', {'projects':projects})
# Create your views here.

def about(request):
    return render(request, 'main/about.htm')


def help(request):
    return render(request, 'main/help.htm')

def extra(request):
    return render(request, 'main/extra.htm')

def more(request):
    return render(request, 'main/more.htm')
