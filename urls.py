from django.conf.urls.defaults import patterns, include, url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url('^hello/$', 'recipes.views.hello', name='hello'),
    url('^$', 'recipes.views.base', name='base'),
    url('^category/(?P<category_slug>[\w-]+)/$', 'recipes.views.category', name='category'),
    url('^detail/(?P<slug>[\w-]+)/$', 'recipes.views.detail', name='recipe_detail'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^search/', include('haystack.urls')),

)

urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
handler404 = 'recipes.views.handler_404'
