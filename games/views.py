from django.shortcuts import render

# Create your views here.

def connect4(request):
    return render(request,'games/connect4.html')

def index(request):
    return render(request,'games/index.html')
