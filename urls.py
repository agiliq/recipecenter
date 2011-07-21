from django.conf.urls.defaults import patterns, include, url
from recipes import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from djangoratings.views import AddRatingFromModel
from django.conf import settings
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    
    url('^hello/$', 'recipes.views.hello', name='hello'),
    url('^base/$', 'recipes.views.base', name='base'),
    # Examples:
    # url(r'^$', 'recipecenter.views.home', name='home'),
    # url(r'^recipecenter/', include('recipecenter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
