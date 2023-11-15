
from  django.urls import path 
from Keerthi.views import *
app_name='cutie'

urlpatterns=[
    path('Nandu/',Nandu,name='Nandu'),
    path('sweety/',sweety,name='sweety'),
]
