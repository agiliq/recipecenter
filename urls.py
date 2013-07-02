from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', 'recipes.views.base', name='base'),
    url('^category/(?P<category_slug>[\w-]+)/$', 'recipes.views.category', name='category'),
    url('^detail/(?P<slug>[\w-]+)/$', 'recipes.views.detail', name='recipe_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
