from django.urls import path
from . import views

urlpatterns = [
    path('', views.HeroView.as_view()),
    path('heros/',                  views.HeroListView.as_view(),       name='hero_list'),
    path('heros/<int:pk>',          views.HeroDetailView.as_view(),     name='hero_detail'),
    path('heros/hero_add',          views.HeroCreateView.as_view(),     name='hero_add'),
    path('heros/<int:pk>/',         views.HeroUpdateView.as_view(),     name='hero_edit'),
    path('heros/<int:pk>/delete',   views.HeroDeleteView.as_view(),     name='hero_delete'),
]
