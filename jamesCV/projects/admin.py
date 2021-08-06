from django.contrib import admin
from projects.models import Project, Category

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
        'image2',
        'link_url',
        'github_url'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
