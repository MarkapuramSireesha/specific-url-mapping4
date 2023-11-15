
from  django.urls import path 
from  Hari.views import *
app_name='anything'

urlpatterns=[
    path('Nikee/',Nikee,name='Nikee'),
    path('nick/',nick,name='nick'),
]
