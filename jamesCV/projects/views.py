from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower

from .models import Project, Category

# Create your views here.


def projects(request):
    """ A view to render projects.html and project cards"""
    projects = Project.objects.all()
    categories = Category.objects.all()
    current_categories = None
    category = None

    if 'category' in request.GET:
        current_categories = request.GET['category'].split(',')
        projects = projects.filter(category__name__in=current_categories)
        category = Category.objects.filter(
            name__in=current_categories)

    context = {
        'projects': projects,
        'categories': categories,
        'current_category': category
    }

    return render(request, 'projects/projects.html', context)
