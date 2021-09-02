from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('test', views.testPageView, name='test')
    ]