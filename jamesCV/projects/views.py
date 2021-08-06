from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower

from .models import Project, Category

# Create your views here.


def projects(request):
    """ A view to render projects.html and project cards"""
    projects = Project.objects.all()


    context = {
        'projects': projects
    }

    return render(request, 'projects/projects.html', context)
