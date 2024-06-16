from django.shortcuts import render

def index(request):
    context = {
        'title': 'My Blog',
        'heading': 'Welcome to my blog',
    }
    return render(request, 'index.html', context)