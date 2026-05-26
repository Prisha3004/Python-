from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>hello world</h1>")

def python(request):
    return HttpResponse("<h1>Python programming</h1>")

def java(request):
    return HttpResponse("<h1>java programming</h1>")

def php(request):
    return HttpResponse("<h1>php programming</h1>")