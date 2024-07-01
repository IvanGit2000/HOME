from importlib.resources import contents
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'home',
        'content': 'Main page store = HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False,
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')

