from django.views.generic import ListView, TemplateView
from . import models

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class HeroDetailView(TemplateView):
    model = models.Hero
    template_name = 'hero_detail.html'

    def get_context_data(self, **kwargs):
        hero_id = kwargs['pk']
        hero = models.Hero.objects.get(pk=hero_id)
        return {'hero': hero}


class HeroListView(ListView):
    model = models.Hero
    template_name = 'hero_list.html'
