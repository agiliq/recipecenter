from django.http import HttpResponse
from recipes.models import RecipeDump
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext

def render(request, template, context):
    return render_to_response(template,context,context_instance = RequestContext(request))

def hello(request):
    return HttpResponse("Hello world")

def base(request):
    return render(request, 'base.html', 'none')
