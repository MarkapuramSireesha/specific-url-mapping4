from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Nandu(request):
    return render(request,'Nandu.html')
def sweety(request):
   return HttpResponse('<h1> Hello My Bestie</h1>')
