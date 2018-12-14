from django.shortcuts import render


# Create your views here.
def jinja_engine(request):
    return render(request, 'template_engine/index.html')
