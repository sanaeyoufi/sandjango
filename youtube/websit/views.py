from django.shortcuts import render
from django.http import HttpResponse

def base_view(request):
    return render(request,'base.html')

def z_view(request):
    return render(request,'z.html')

def k_view(request):
    return render(request,'k.html')
