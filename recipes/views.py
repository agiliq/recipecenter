from django.http import HttpResponse
from recipes.models import Recipe, Category
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from djangoratings.views import AddRatingView


def render(request, template, context):
    return render_to_response(template, context, context_instance=RequestContext(request))


def hello(request):
    return HttpResponse("Angry Birds is like life, the more you play the more you enjoy, the more you calculate, the tougher it get.")


def base(request):
    recipe_list = Recipe.objects.order_by('?')[:12]
    return render(request, 'index.html', {'recipe_list': recipe_list})


def category(request, category_slug=None):
    p = Recipe.objects.filter(category__slug__exact=category_slug)
    if p.count() == 0:
        raise Http404
    paginator = Paginator(p, 12)  # show 20 recipes per page
    page = request.GET.get('page', 1)
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
       # If page is not an integer, deliver first page.
        contents = paginator.page(1)
    except EmptyPage:
      #If page is out of range, deliver last page of results.
        contents = paginator.page(paginator.num_pages)
    return render(request, 'category.html', {'category_dishes': contents})


def detail(request, recipe_id=None):
    p = Recipe.objects.filter(slug=recipe_id)
    if p.count() == 0:
        raise Http404
    return render(request, 'detail.html', {'recipe': p[0]})
