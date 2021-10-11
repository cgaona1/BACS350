from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView
from . import models

# Create your views here.
class HeroView(RedirectView):
    url = '/heros/'


class HeroListView(ListView):
    template_name = 'hero_list.html'
    model = models.Hero


class HeroDetailView(DetailView):
    template_name = 'hero_detail.html'
    model = models.Hero
