from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def porta(request):
    return HttpResponse("Você está na porta")

def sala(request):
    return HttpResponse("Você está na sala")

def quarto(request):
    return HttpResponse("Você está no quarto")

def post_list(request):
    return render(request, 'blog/post_list.html', {})