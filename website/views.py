from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def member_zone(request):
    return render(request, 'member_zone.html', {})