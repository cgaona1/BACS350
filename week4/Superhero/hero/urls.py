from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('hero/', views.HeroListView.as_view(), name='hero'),
    path('hero/<int:pk>', views.HeroDetailView.as_view(), name='hero'),
]
