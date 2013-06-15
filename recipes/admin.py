from django.contrib import admin
from recipes.models import Recipe, Category


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "is_featured"]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
