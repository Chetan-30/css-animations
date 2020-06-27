from django.contrib import admin
from django.urls import path , include
from intern3 import views

app_name = 'intern3'

urlpatterns =[
    path('',views.base,name='base'),
]