from django.shortcuts import render


def index(request):
    """A view that displays an idex page"""
    return render(request, 'index.html')