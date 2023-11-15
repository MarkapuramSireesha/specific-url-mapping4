from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Nikee(request):
    return render(request,'Nikee.html')
def nick(request):
    return HttpResponse('Mr Nikee')