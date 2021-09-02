from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse("<h1>Hello World!!!</h1><p>Mistake fixed</p>")

def testPageView(request):
    return HttpResponse("<h1>This is a test</h1>" + \
        "<p>Testing new view \"testPageView\" ")