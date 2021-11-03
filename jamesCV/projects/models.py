from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Project(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    link_url = models.URLField(max_length=1024, null=True, blank=True)
    github_url = models.URLField(max_length=1024, null=False, blank=False)
    rating = models.IntegerField(blank=True, null=False)

    def __str__(self):
        return self.name
