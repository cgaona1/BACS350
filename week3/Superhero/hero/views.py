from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class SpidermanView(TemplateView):
    template_name = 'spiderman.html'

    def get_context_data(self, **kwargs):
        return{
            'hero_name': 'spiderman'
        }

class BabyGrootView(TemplateView):
    template_name = 'babygroot.html'

    def get_context_data(self, **kwargs):
        return{
            'hero_name': 'babygroot'
        }
    