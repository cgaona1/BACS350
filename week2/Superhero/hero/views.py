from django.views.generic import TemplateView

# Create your views here.

class SpidermanView(TemplateView):
    template_name = 'spiderman.html'

class BabyGrootView(TemplateView):
    template_name = 'babygroot.html'

    '''def get_context_data(self, **kwargs):
        return{
            'title': 'Test data as dictionary',
            'body': 'This is a test for title and body data',
        }
    '''