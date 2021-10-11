from django.urls import path
from . import views

urlpatterns = [
    path('', views.HeroListView.as_view(), name='index'),
    path('<int:pk>', views.HeroDetailView.as_view(), name='details')
]
