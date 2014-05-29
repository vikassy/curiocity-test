from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from cc101 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_curiocity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.testing, name='testing'),
    url(r'^cc101/$', views.cc101_view, name='cc101_view'),
    url(r'^lab/$', views.cclab_view, name='cclab_view')
)
