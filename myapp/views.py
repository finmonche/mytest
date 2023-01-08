from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    name = "豪"
    return render(request, 'index.html', locals())