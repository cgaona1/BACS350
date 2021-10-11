from django.urls import path
from . import views

urlpatterns = [
    path('', views.HeroView.as_view()),
    path('heros/', views.HeroListView.as_view(), name='hero_list'),
    path('<int:pk>', views.HeroDetailView.as_view(), name='hero_details')
]
