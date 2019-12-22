import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
    context = {
        'title': 'Index',
    }
    return render(request, 'content/index.html', context) 

def blog(request):
    context = {
        'title': 'Blog',
    }
    return render(request, 'content/blog.html', context) 

def blog1(request):
    context = {
        'title': 'Blog1',
    }
    return render(request, 'blog/blog1.html', context) 

def blog2(request):
    context = {
        'title': 'Week2',
    }
    return render(request, 'blog/blog2.html', context) 

def blog3(request):
    context = {
        'title': 'Week3',
    }
    return render(request, 'blog/blog3.html', context) 

def blog4(request):
    context = {
        'title': 'Week4',
    }
    return render(request, 'blog/blog4.html', context) 

def projects(request):
    context = {
        'title': 'Projects',
    }
    return render(request, 'content/projects.html', context) 

def github(request):
    response = requests.get('https://api.github.com/users/acanlord/repos')
    repos = response.json()
    context = {
        'github_repos': repos,
    }
    return render(request, 'content/github.html', context)
    print(repos)
