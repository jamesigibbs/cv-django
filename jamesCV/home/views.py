from django.shortcuts import render

# Create your views here.


def home(request):
    """ A view to render index.html"""

    return render(request, 'home/index.html', {})
