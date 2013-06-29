from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from recipes.models import Recipe
from django.conf import settings


def base(request):
    recipe_list = Recipe.objects.all().order_by('-is_featured', '?')\
        [:settings.NUMBER_OF_ENTRIES_PER_PAGE]
    return render(request, 'index.html', {'recipe_list': recipe_list})


class CategoryView(View):

    def get(self, request, category_slug=None, *args, **kwargs):
        #Recipe.objects.filter(is_featured=True)
        p = Recipe.objects.filter(category__slug__exact=category_slug)
        if p.count() == 0:
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
    def dispatch(self, request, slug=None):
        p = Recipe.objects.filter(slug=slug)
        if p.count() == 0:
            raise Http404
        return render(request, 'detail.html', {'recipe': p[0]})

detail = RecipeDetailView.as_view()
