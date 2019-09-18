#pages/urls.py
from django.urls import path,include
from .views import homePageView
from django.contrib import admin


#These are the patterns which are kinda exchangeable
#If user types nothing, call homePageView and name it "home"
urlpatterns = [
    path('',homePageView,name='home'), 
]

