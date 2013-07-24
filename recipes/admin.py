from django.contrib import admin

from .models import Recipe, Category


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "is_featured"]
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
