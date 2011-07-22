from django.contrib import admin
from recipes.models import RecipeDump, Category

admin.site.register(RecipeDump)
admin.site.register(Category)
