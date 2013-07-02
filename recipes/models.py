from django.core.urlresolvers import reverse
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

    class Meta:
        verbose_name_plural = "categories"


class Recipe(models.Model):
    category = models.ForeignKey(Category, null=True, blank=True)
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.CharField(max_length=100, null=True, blank=True)
    added_by = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    is_featured = models.BooleanField('Featured',
                                      default=False,
                                      help_text='Designates whether this\
                                      recipe should be treated as featured.')

    def __unicode__(self):
        return self.name

    def title(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe_detail", args=[self.slug])
