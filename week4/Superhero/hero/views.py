from django.views.generic import ListView, TemplateView
from . import models

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class HeroDetailView(TemplateView):
    model = models.Hero
    template_name = 'hero_detail.html'

    def get_context_data(self, **kwargs):
        return {'hero': models.Hero.objects.get(pk=1)}


class HeroListView(ListView):
    model = models.Hero
    template_name = 'hero_list.html'
