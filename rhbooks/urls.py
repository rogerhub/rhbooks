from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('books.views',
    url(r'^$', 'home'),
    url(r'^search', 'search'),
    url(r'^top', 'top'),
    url(r'^latest', 'latest'),
    url(r'^hit', 'hit'),
)
urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'rhbooks.views.home', name='home'),
    # url(r'^rhbooks/', include('rhbooks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
