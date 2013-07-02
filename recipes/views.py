from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.conf import settings

from recipes.models import Recipe


class RecipeBaseView(ListView):

    context_object_name = 'recipe_list'
    template_name = 'index.html'

    def get_queryset(self):
        return Recipe.objects.all().order_by(
                '-is_featured', '?')[:settings.NUMBER_OF_ENTRIES_PER_PAGE]

base = RecipeBaseView.as_view()


class CategoryView(View):

    def get(self, request, category_slug=None, *args, **kwargs):
        p = Recipe.objects.filter(category__slug__exact=category_slug)
        if not p.count():
            raise Http404
        paginator = Paginator(p, settings.NUMBER_OF_ENTRIES_PER_PAGE)
        page = int(request.GET.get('page', 1))
        try:
            contents = paginator.page(page)
        except EmptyPage:
            #If page is out of range, deliver last page of results.
            contents = paginator.page(paginator.num_pages)
        return render(request, 'category.html', {'category_dishes': contents})

category = CategoryView.as_view()


class RecipeDetailView(DetailView):
    context_object_name = 'recipe'
    model = Recipe
    template_name = 'detail.html'

detail = RecipeDetailView.as_view()
