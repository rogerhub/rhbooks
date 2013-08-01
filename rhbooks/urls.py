from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('books.views',
    url(r'^$', 'home'),
    url(r'^search', 'search'),
    url(r'^top', 'top'),
    url(r'^latest', 'latest'),
    url(r'^hit', 'hit'),
    url(r'^api/addbook', 'api_addbook'),
    url(r'^api/verify', 'api_verify'),
)
urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
