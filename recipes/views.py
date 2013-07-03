from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.conf import settings

from .models import Recipe


class RecipeIndexView(ListView):

    context_object_name = 'recipe_list'
    template_name = 'index.html'

    def get_queryset(self):
        return Recipe.objects.all().order_by(
                '-is_featured', '?')[:settings.NUMBER_OF_ENTRIES_PER_PAGE]

base = RecipeIndexView.as_view()


class CategoryView(ListView):

    template_name = 'category.html'
    paginate_by = settings.NUMBER_OF_ENTRIES_PER_PAGE
    allow_empty = False  # 404 page should be shown for wrong category

    def get_queryset(self):
        return Recipe.objects.filter(
                category__slug=self.kwargs.get('category_slug'))

    def get_context_data(self, **kwargs):
        #Did this because the template uses context `category_dishes`
        #If we change the template to use `page_obj`, we can remove this
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category_dishes'] = context['page_obj']
        return context

category = CategoryView.as_view()


class RecipeDetailView(DetailView):
    context_object_name = 'recipe'
    model = Recipe
    template_name = 'detail.html'

detail = RecipeDetailView.as_view()
