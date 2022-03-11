from django.shortcuts import render
from django.http import HttpResponse

def reels(request):
    return render(request,'index.html')