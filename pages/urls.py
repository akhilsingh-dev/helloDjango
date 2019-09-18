#pages/urls.py
from django.urls import path
from .views import HomePageView,AboutPageView

#These are the patterns which are kinda exchangeable
#If user types nothing, call homePageView and name it "home"
urlpatterns = [
    path('',HomePageView.as_view(),name='home'), 
    path('about/',AboutPageView.as_view(),name='about')
]

