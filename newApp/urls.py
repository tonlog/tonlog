from django.conf.urls import patterns, include, url
from newApp import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$','blog.views.index'),#to the index page.


    (r'^search/onBlog$','blog.views.searchBlog'),
    (r'^contactUs/$','blog.views.contactUs'),
    (r'^contactUs/thx/$', 'blog.views.thankU'),
    # Examples:
    # url(r'^$', 'newApp.views.home', name='home'),
    # url(r'^newApp/', include('newApp.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_PATH}),
)
