from django.http import HttpResponse
from recipes.models import RecipeDump, Category
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def render(request, template, context):
    return render_to_response(template,context,context_instance = RequestContext(request))

def hello(request):
    return HttpResponse("Hello world")

def base(request):
    return render(request, 'base.html', {})

def category(request, category_slug=None):
    p = RecipeDump.objects.filter(category__slug__exact = category_slug)
    if p.count() == 0:
        raise Http404
    return render(request, 'category.html', {'category_dishes': p}) 

def detail(request, recipe_id=None):
    p = RecipeDump.objects.filter(slug=recipe_id)
    if p.count() == 0:
        raise Http404
    return render(request, 'detail.html', {'recipe': p[0]})    
