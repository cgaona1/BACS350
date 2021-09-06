from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('spiderman/', views.SpidermanView.as_view(), name='spiderman'),
    path('babygroot/', views.BabyGrootView.as_view(), name='babygroot'),
]