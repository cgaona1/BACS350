from django.urls import path
from django.urls.conf import include, include
from . import views

urlpatterns = [
    path('', views.HeroView.as_view()),     #Redirect url   
    path('heroes/',                  views.HeroListView.as_view(),       name='hero_list'),
    path('heroes/<int:pk>',          views.HeroDetailView.as_view(),     name='hero_detail'),
    path('heroes/hero_add',          views.HeroCreateView.as_view(),     name='hero_add'),
    path('heroes/<int:pk>/',         views.HeroUpdateView.as_view(),     name='hero_edit'),
    path('heroes/<int:pk>/delete',   views.HeroDeleteView.as_view(),     name='hero_delete'),
]
