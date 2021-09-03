from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class PageView(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        return{
            'title': 'Test data as dictionary',
            'body': 'This is a test for title and body data',
        }