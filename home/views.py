from django.shortcuts import render, request

# Create your views here.
def index(request):
    """A view to return index page"""
    return render(request,'home/index.html')
