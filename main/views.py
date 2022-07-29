from django.shortcuts import render
from .models import Files

def index(response):
    return render(response, 'main/result.html')
