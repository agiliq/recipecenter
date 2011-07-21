from django.http import HttpResponse
from recipes.models import RecipeDump, Category
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

recipesobj = RecipeDump.objects.all()
categobj = Category.objects.all() 

def render(request, template, context):
    return render_to_response(template,context,context_instance = RequestContext(request))

def hello(request):
    return HttpResponse("Hello world")

def base(request):
    return render(request, 'base.html', {'recipesobj':recipesobj,'categobj':categobj})

def datadisp(request):
    return render(request, 'base.html', none)
 

def detail(request, recipe_id=None):
    try:
        p = RecipeDump.objects.filter(slug=recipe_id)[0]
    except IndexError:
        raise Http404
    return render(request, 'detail.html', {'recipe': p})    
