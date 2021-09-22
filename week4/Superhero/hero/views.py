from django.views.generic import ListView, TemplateView
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class HeroListView(ListView):
    model = models.Hero
    template_name = 'hero_list.html'
