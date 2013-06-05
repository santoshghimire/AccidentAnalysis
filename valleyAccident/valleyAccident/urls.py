from django.conf.urls import patterns, include, url
from accidentApp.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^test/$', 'accidentApp.views.home', name='home'),
    url(r'load_data/',load_data),
    url(r'data/',my_data),
    url(r'load_location/',place_coordinate),
    # url(r'^valleyAccident/', include('valleyAccident.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
