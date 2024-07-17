from django.shortcuts import render

from goods.models import Categories

def index(request):
    
    context = {
        'title': 'Home',
        'content': 'Furniture store HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About',
        'content': 'About us',
        'text_on_page': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Consequuntur.',
    }
    return render(request, 'main/about.html', context)
