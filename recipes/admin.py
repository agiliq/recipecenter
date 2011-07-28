from django.contrib import admin
from recipes.models import Recipe, Category

admin.site.register(Recipe)
admin.site.register(Category)
