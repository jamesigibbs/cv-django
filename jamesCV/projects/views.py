from django.shortcuts import render

# Create your views here.


def projects(request):
    """ A view to render projects.html and project cards"""

    context = {}

    return render(request, 'projects/projects.html', context)
