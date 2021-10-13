from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, CreateView, UpdateView, DeleteView
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


class HeroCreateView(LoginRequiredMixin ,CreateView):
    template_name = 'hero_add.html'
    model = models.Hero
    fields = ['hero_name', 'hero_description']
    #success_url = reverse_lazy('hero_list')

class HeroUpdateView(LoginRequiredMixin ,UpdateView):
    template_name = 'hero_edit.html'
    model = models.Hero
    fields = ['hero_name', 'hero_description']


class HeroDeleteView(DeleteView):
    template_name = 'hero_delete.html'
    model = models.Hero
    #success_url = reverse_lazy['hero_list']
